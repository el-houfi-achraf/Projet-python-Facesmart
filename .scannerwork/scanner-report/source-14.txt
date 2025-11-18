import sqlite3
import os


conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employe (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL UNIQUE,
    id_tache INT NOT NULL,
    FOREIGN KEY (id_tache) REFERENCES SuiviTemps (id) ON DELETE CASCADE
)
''')

class Employe:
    def __init__(self, nom="", prenom="", email="", password="" ,id_tache=0):
        self.nom = f'{nom}'.upper()
        self.prenom = f'{prenom}'.upper()
        self.email = f'{email}'.upper()
        self.password = f'{password}'.upper()
        self.id_tache=id_tache

    def create(self):
        nom=f"{self.nom}".upper()
        prenom=f"{self.prenom}".upper()
        path = f"data/{nom}_{prenom}.png"
        print(path,f"{self.nom}".upper(),f"{self.prenom}".upper())
        check_file = os.path.isfile(path)
        if(check_file):
            cursor.execute('INSERT INTO Employe (nom, prenom, email,password,id_tache) VALUES (?, ?, ? ,?,?)',
                       (self.nom, self.prenom, self.email,self.password,self.id_tache))
            conn.commit()
            conn.close()
            return True
        else:
            return False
        

    @staticmethod
    def read(id):
        cursor.execute('SELECT * FROM Employe WHERE id = ?', (id,))
        return cursor.fetchone()
    
    

    def update(self, id):
        try:
            cursor.execute('UPDATE Employe SET nom = ?, prenom = ?, email = ?, password = ? ,id_tache = ? WHERE id = ?',
                           (self.nom, self.prenom, self.email, self.password ,self.id_tache, id))
            conn.commit()
        except sqlite3.Error as e:
            return False
        else:
            return True

    @staticmethod
    def delete(id):
     try:
        cursor.execute('DELETE FROM Employe WHERE id =?', (id,))
        conn.commit()
     except (sqlite3.Error,sqlite3.IntegrityError )  as error:
        print(error)
        return error
     else:
         return True
    
    @staticmethod
    def ChercherParNom(nom,prenom):
        cursor = conn. cursor()
        nomE=f'{nom}'.upper()
        prenomE=f'{prenom}'.upper()
        try:
            cursor . execute ("""SELECT * FROM Employe WHERE nom = ? AND prenom= ? """,(nomE,prenomE))
        except sqlite3.Error as error :
            return error
        else:
            return cursor.fetchone()
    
    @staticmethod
    def selectall():
        cursor = conn.cursor()
        cursor . execute ("""SELECT * FROM Employe """)
        return cursor.fetchall()

    @staticmethod
    def modifier_Employer_Tache(id_tache,id_emp):
        try:
            cursor.execute('UPDATE Employe SET id_tache = ? WHERE id = ?',
                           (id_tache, id_emp))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
            return e
        else:
            return 'Done'
    
    @staticmethod
    def chercherParIdtache(id_tache):
        try:
            cursor . execute ("""SELECT id,nom,prenom FROM Employe WHERE id_tache= ? """,(id_tache,))
            conn.commit()
        except sqlite3.Error as e:
            print (e)
        else:
            return cursor.fetchall()
            
    
    
    

