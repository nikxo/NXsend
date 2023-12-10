import sqlite3
from tkinter import END


def add_db_msg(table_id, name, msg):
    # stoque les asockets en ligne
    connexion = sqlite3.connect(f"App_Gui/Base/{table_id}.db")

    # Créer un curseur
    curseur = connexion.cursor()

    # Exécution de la requête avec les valeurs passées en tant que paramètres
    curseur.execute(
        "INSERT INTO msg (name, message) VALUES (?, ?)", (name, msg))

    # Validation des changements dans la base de données
    connexion.commit()
    connexion.close()


def create_db(name):
    # stoque les asockets en ligne
    connexion = sqlite3.connect(f"App_Gui/Base/{name}.db")
    # Créer un curseur
    curseur = connexion.cursor()

    request = f"CREATE TABLE msg (id INTEGER PRIMARY KEY,name TEXT,message TEXT)"

    # Créer une table pour stocker les messages associés aux sessions
    curseur.execute(request)

    connexion.commit()
    connexion.close()


def afficher_tout_from_db(text_box, nom_db):
    try:
        connexion = sqlite3.connect(f"App_Gui/Base/{nom_db}.db")
        curseur = connexion.cursor()

        # Sélectionne toutes les données de la table 'msg'
        curseur.execute("SELECT name, message FROM msg")
        rows = curseur.fetchall()

        # Affiche les données de chaque ligne
        for row in rows:
            name, message = row  # Accéder individuellement aux colonnes 'name' et 'message'
            text_box.configure(state='normal')
            # Insère le nom avec le tag 'red'
            text_box.insert(END, name, 'red')
            text_box.insert(END, f"{message}\n")  # Ajoute le message
            # Configure le tag 'red' en rouge
            text_box.tag_config('red', foreground='red')
            text_box.yview_moveto(1)

        # Ferme la connexion à la base de données
        connexion.close()

    except sqlite3.Error as e:
        print(f"Erreur SQLite : {e}")
