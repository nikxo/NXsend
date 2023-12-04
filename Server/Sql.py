import sqlite3

# stoque les asockets en ligne
connexion = sqlite3.connect('Server/Server.db')

# Créer un curseur
curseur = connexion.cursor()


def socket_storage(addr, conn):
    curseur.execute("INSERT INTO addr (adresse, socket, status) VALUES (?, ?, ?)",
                    (addr, conn, "online"))
    connexion.commit()


def addr_status(addr):
    curseur.execute(
        "SELECT status FROM addr WHERE adresse LIKE ? AND status = ?", (addr, "online"))
    resultats = curseur.fetchall()  # Récupérer les résultats de la requête
    if resultats:
        print("L'adresse est en ligne.")
    else:
        print("L'adresse n'est pas en ligne.")


def show_database():
    curseur.execute("SELECT * FROM addr")
    resultats = curseur.fetchall()
    for i in resultats:
        print(i)
