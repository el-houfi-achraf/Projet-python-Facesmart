
import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Création de la table Employe si elle n'existe pas déjà
cursor.execute('''
CREATE TABLE IF NOT EXISTS SuiviTemps (
    idPeriod INTEGER PRIMARY KEY AUTOINCREMENT,
    DateArrivee TEXT,
    DateDepart TEXT,
    id INTEGER,
    FOREIGN KEY (id) REFERENCES Employe (id) ON DELETE CASCADE
)
''')  
cursor.close()

class SuiviTemps:
    def __init__(self, id_emp,checkin=0,checkout=0):
        self.id_emp = id_emp
        self.checkin = checkin
        self.checkout = checkout
        
    def Ajouter_checkin(self):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO SuiviTemps (DateArrivee, id) VALUES (datetime('now'), ?)",(self.id_emp,))
        conn.commit()
        cursor.close()
        
    def Ajouter_checkout(self):
        cursor = conn.cursor()
        cursor.execute("""select max(idPeriod) from SuiviTemps WHERE id= ?""",(self.id_emp,))
        idPeriod=cursor.fetchone()
        idPeriod=idPeriod[0]
        print(idPeriod)
        cursor.execute("UPDATE SuiviTemps SET DateDepart = datetime('now') WHERE idPeriod = ?;",
                       (idPeriod,))
        conn.commit()
        cursor.close()
    @staticmethod  
    def chercherParId(id):
        cursor = conn.cursor()
        cursor.execute("""select * ,ROUND((JULIANDAY(DateDepart) - JULIANDAY(DateArrivee)) * 86400) AS difference from SuiviTemps WHERE id= ?""",(id,))
        return cursor.fetchall()
    
    @staticmethod
    def chercherParDate(Date):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM SuiviTemps WHERE DateDepart > ?;""",(Date,))
        return cursor.fetchall()
        
    
    