import sqlite3
import importlib

import src.tache as tache


def setup_in_memory_tache_module():
    # Repoint module-level connection and cursor to an in-memory database for isolation
    tache.conn = sqlite3.connect(':memory:')
    tache.cursor = tache.conn.cursor()
    tache.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Tache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            libelle TEXT NOT NULL,
            Status TEXT NOT NULL
        )
    ''')
    tache.conn.commit()


def test_ajouter_and_read_and_chercher():
    setup_in_memory_tache_module()

    task = tache.Tache(libelle='do something', Status='open')
    res = task.Ajouter_Tache()
    # Ajouter_Tache returns None on success (module doesn't return explicit True)
    assert res is None

    rows = tache.Tache.read()
    assert len(rows) == 1
    inserted = rows[0]
    assert inserted[1] == 'DO SOMETHING'
    assert inserted[2] == 'OPEN'

    # chercherParLibelle
    found = tache.Tache.chercherParLibelle('DO SOMETHING')
    # The method returns a single row tuple when found
    assert found is not None
    assert found[1] == 'DO SOMETHING'

    # chercherParID
    found_by_id = tache.Tache.chercherParID(inserted[0])
    assert found_by_id is not None
    assert found_by_id[0] == inserted[0]


def test_modifier_and_supprimer():
    setup_in_memory_tache_module()

    task = tache.Tache(libelle='old', Status='todo')
    task.Ajouter_Tache()

    # Update to new values using modifier
    # Ensure values are uppercased like the module normally does
    task.libelle = 'NEW'
    task.Status = 'DONE'
    result = task.modifier('OLD')
    assert result == 'Done'

    # Verify update
    rows = tache.Tache.read()
    assert rows[0][1] == 'NEW'
    assert rows[0][2] == 'DONE'

    # Test supprimer
    out = tache.Tache.supprimer('NEW')
    assert out == 'Done'
    rows_after = tache.Tache.read()
    assert rows_after == []
