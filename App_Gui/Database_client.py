import sqlite3
# stoque les asockets en ligne
connexion = sqlite3.connect('App_Gui/Base/')
# Créer un curseur
curseur = connexion.cursor()

# Purger la table "addr"
curseur.execute("DROP TABLE IF EXISTS msg")

# Créer une table pour stocker les messages associés aux sessions
curseur.execute('''CREATE TABLE msg (
                  id INTEGER PRIMARY KEY,
                  session_id INTEGER,
                  message TEXT,
                  )''')


connexion.commit()
