import sqlite3
from tkinter import END
import fonction as f


def add_db_msg(table_id, name, msg):
    # stoque les asockets en ligne
    connexion = sqlite3.connect(f"Base/{table_id}.db")

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
    connexion = sqlite3.connect(f"Base/{name}.db")
    # Créer un curseur
    curseur = connexion.cursor()

    request = f"CREATE TABLE msg (id INTEGER PRIMARY KEY,name TEXT,message TEXT)"

    # Créer une table pour stocker les messages associés aux sessions
    curseur.execute(request)

    connexion.commit()
    connexion.close()


def show_db_msg(text_box, table_id):
    # stoque les asockets en ligne
    connexion = sqlite3.connect(f"Base/{table_id}.db")
    # Créer un curseur
    curseur = connexion.cursor()

    curseur.execute("SELECT name, message FROM msg")
    rows = curseur.fetchall()
    text_box.configure(state='normal')
    # Affiche les données de chaque ligne
    for row in rows:
        name, message = row  # Accéder individuellement aux colonnes 'name' et 'message'

        # Insère le nom avec le tag 'red'
        text_box.insert(END, name, 'red')
        text_box.insert(END, f"{message}\n")  # Ajoute le message
        # Configure le tag 'red' en rouge
        text_box.tag_config('red', foreground='red')
        text_box.yview_moveto(1)

    text_box.configure(state='disabled')
    connexion.close()
