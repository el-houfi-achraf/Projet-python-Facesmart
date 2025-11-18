import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Tache (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    libelle TEXT NOT NULL,
    Status TEXT NOT NULL
)
''')

class Tache:
    def __init__(self, libelle="", Status=""):
        self.libelle = f'{libelle}'.upper()
        self.Status = f'{Status}'.upper()
 

    def Ajouter_Tache(self):
        try:
            cursor.execute('INSERT INTO Tache (libelle, Status) VALUES (?, ?)',(self.libelle, self.Status))
            conn.commit()
        except sqlite3.Error as e:
            print(f"error: {e}")
            return e
    
    
            
    def modifier(self,libelle):
        try:
            cursor.execute('UPDATE Tache SET libelle = ? , Status = ? WHERE libelle = ?', (self.libelle,self.Status,libelle))
            conn.commit()
        except sqlite3.Error as e:
            print(f"error: {e}")  
            return e
        else:
            return 'Done'  
       
    @staticmethod        
    def read():
        try:
            cursor.execute('SELECT * FROM Tache')
            conn.commit()
        except sqlite3.Error as e:
            print(f"error: {e}")
        else:
            return cursor.fetchall()
    
    @staticmethod
    def chercherParLibelle(Libelle):
        try:
            cursor.execute('SELECT * FROM Tache WHERE libelle = ?', (Libelle,))
            conn.commit()
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"error: {e}")
            
    @staticmethod
    def chercherParID(id_tache):
        try:
            cursor.execute('SELECT * FROM Tache WHERE id = ?', (id_tache,))
            conn.commit()
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"error: {e}")
    
    @staticmethod
    def supprimer(libelle):
     try:
        cursor.execute('DELETE FROM Tache WHERE libelle = ?', (libelle,))
        conn.commit()
     except (sqlite3.Error,sqlite3.IntegrityError )  as error:
        print(error)
        return error
     else:
         return 'Done'

        
"""
    @staticmethod
    def read(id):
        cursor.execute('SELECT * FROM Employe WHERE id = ?', (id,))
        return cursor.fetchone()
    
    

    def update(self, id):
        try:
            cursor.execute('UPDATE Employe SET nom = ?, prenom = ?, email = ?, password = ? WHERE id = ?',
                       (self.nom, self.prenom, self.email, self.password, id))
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
 """   
    

    
    

