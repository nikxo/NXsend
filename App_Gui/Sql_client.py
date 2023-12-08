import sqlite3
# stoque les asockets en ligne
connexion = sqlite3.connect('Server/message.db')
# Créer un curseur
curseur = connexion.cursor()


def add_db_msg(session, msg):
    curseur.execute(
        "INSERT INTO msg(session_id,message) VALUES(?,?)", (session, msg))


def create_table(name):
    # stoque les asockets en ligne
    connexion = sqlite3.connect(f"App_Gui/Base/{name}")
    # Créer un curseur
    curseur = connexion.cursor()

    # Purger la table "addr"
    curseur.execute("DROP TABLE IF EXISTS ?", name)

    # Créer une table pour stocker les messages associés aux sessions
    curseur.execute('''CREATE TABLE msg (
                    id INTEGER PRIMARY KEY,
                    session_id INTEGER,
                    message TEXT,
                    )''')

    connexion.commit()
