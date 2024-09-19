import os
import sqlite3

pathBase = "./jour04/base.db"

## optionnel
if not os.path.isfile("./jour04/base.db"):
    # permet de créer le fichier base.db si il n'existe pas
    with open("./jour04/base.db", "w") as f:
            print("le fichier est créé")
else:
      print("le fichier existe déjà")

connexion = sqlite3.connect(pathBase)

cursor = connexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS exemple  (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nom VARCHAR(255) NOT NULL,
dt_creation DATETIME DEFAULT CURRENT_TIMESTAMP 
)
""")

# cursor.execute("""
# INSERT INTO exemple 
# (nom , dt_creation)
# VALUES
# ( 'Alain' , '1988-01-02'),
# ( 'Céline' , '2021-12-15')
# """)

connexion.commit()
# en + bonus
cursor.execute("SELECT * FROM exemple")
lignes = cursor.fetchall()
print(lignes)

connexion.close()