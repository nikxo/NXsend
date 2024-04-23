import sqlite3

IP_Server = '147.215.205.114'
Port_Server = 4444
addr = (IP_Server, Port_Server)

# stoque les asockets en ligne
connexion = sqlite3.connect('Server.db')
# Créer un curseur
curseur = connexion.cursor()

# Purger la table "addr"
curseur.execute("DROP TABLE IF EXISTS addr")

# Créer une table pour stocker les adresses IPv4 avec un int associé et un ID unique
curseur.execute('''CREATE TABLE addr (
                  id INTEGER PRIMARY KEY,
                  adresse TEXT UNIQUE,
                  port TEXT,
                  status TEXT,
                  UNIQUE(id)
                  )''')


connexion.commit()
