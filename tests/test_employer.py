import sqlite3
import os
import importlib

import src.employer as employer


def setup_in_memory_employer_module():
    # Repoint module-level connection and cursor to an in-memory database for isolation
    employer.conn = sqlite3.connect(':memory:')
    employer.cursor = employer.conn.cursor()
    # Create simplified table similar to module
    employer.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employe (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL UNIQUE,
            id_tache INT NOT NULL
        )
    ''')
    employer.conn.commit()


def test_create_returns_false_when_no_image(tmp_path, monkeypatch):
    setup_in_memory_employer_module()

    # Ensure data/ directory doesn't contain expected image
    # Use a temp data dir by monkeypatching the path check
    # Create a temporary data directory and ensure file does not exist
    tmp_data = tmp_path / "data"
    tmp_data.mkdir()

    # Monkeypatch os.path.isfile to look into tmp_data
    real_isfile = os.path.isfile

    def fake_isfile(path):
        # Redirect any data/ checks to our tmp_data
        if path.startswith('data/'):
            redirected = str(tmp_data / path.split('/', 1)[1])
            return real_isfile(redirected)
        return real_isfile(path)

    monkeypatch.setattr(os.path, 'isfile', fake_isfile)

    emp = employer.Employe(nom='John', prenom='Doe', email='j@d.com', password='pwd')
    created = emp.create()
    assert created is False


def test_create_returns_true_when_image_exists(tmp_path, monkeypatch):
    setup_in_memory_employer_module()

    # Prepare a fake image file expected by create()
    tmp_data = tmp_path / "data"
    tmp_data.mkdir()
    image_name = 'JOHN_DOE.png'  # create() uppercases nom/prenom and uses data/{nom}_{prenom}.png
    (tmp_data / image_name).write_bytes(b"PNGDATA")

    # Monkeypatch os.path.isfile to check our tmp_data
    real_isfile = os.path.isfile

    def fake_isfile(path):
        if path.startswith('data/'):
            redirected = str(tmp_data / path.split('/', 1)[1])
            return real_isfile(redirected)
        return real_isfile(path)

    monkeypatch.setattr(os.path, 'isfile', fake_isfile)

    emp = employer.Employe(nom='john', prenom='doe', email='j@d.com', password='pwd')
    created = emp.create()
    # create() returns True when the image exists; note create() closes the connection on success
    assert created is True
    # Reassign a fresh in-memory conn after create() closed it
    employer.conn = sqlite3.connect(':memory:')
    employer.cursor = employer.conn.cursor()
    employer.cursor.execute('CREATE TABLE IF NOT EXISTS Employe (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, prenom TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL UNIQUE, id_tache INT NOT NULL)')
    employer.conn.commit()
