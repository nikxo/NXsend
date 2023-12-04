import sqlite3

# stoque les asockets en ligne
connexion = sqlite3.connect('Server/Server.db')

# Créer un curseur
curseur = connexion.cursor()


def socket_storage(addr):
    curseur.execute("INSERT INTO addr (adresse, port, status) VALUES (?, ?, ?)",
                    (addr[0], addr[1], "online"))
    connexion.commit()


def addr_is_online(addr):
    if addr_is_in_db(addr):
        curseur.execute(
            "SELECT status FROM addr WHERE adresse LIKE ? AND status = ?", (addr, "online"))
        resultats = curseur.fetchall()  # Récupérer les résultats de la requête
        if resultats:
            return True
        return False


def show_database():
    curseur.execute("SELECT * FROM addr")
    resultats = curseur.fetchall()
    for i in resultats:
        print(i)


def addr_is_in_db(addr):
    curseur.execute("SELECT adresse FROM addr WHERE adresse = ?", (addr,))
    result = curseur.fetchall()
    if result:
        return True
    return False


def get_socket(ip):
    curseur.execute(
        "SELECT adresse, port FROM addr WHERE adresse = ?", (ip,))
    return curseur.fetchall()
