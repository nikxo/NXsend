import threading
import time
from queue import Queue
import socket
import sqlite3

# Se connecter à la base de données (elle sera créée si elle n'existe pas)
connexion = sqlite3.connect('Server/Server.db')

# Créer un curseur
curseur = connexion.cursor()


stock_tab = {}
stock_tab_addr = {}


def thread_chat(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        dest = peer_conn(data)
        # Faites quelque chose avec les données reçues
        print(f"Données reçues: {data.decode('utf-8')}")
        dest.send(data)
    conn.close()

    print(f"Handler for {addr} finish")


# etablit la connection avec l'adresse specifiée
def setconnect(addr):
    # Creation Socket de connection
    socket_ = socket.create_connection(addr)
    return socket_


# Requete de connection au destinataire
def peer_conn(data):
    while True:
        if (data[0:6]).decode() == 'IDDEST':
            dest = socket_find(data[6:])
            if dest:
                return setconnect(dest)


# stoque les asockets en ligne
def socket_storage(addr, conn):
    curseur.execute("INSERT INTO adresses_ip (adresse, socket) VALUES (?, ?)",
                    (addr, conn))


# verifie si l'adresse specifiée est en ligne
def addr_is_online(addr):
    try:
        curseur.execute("SELECT * FROM online WHERE addresse = ?", (addr))
    except Exception:
        return


# Fait une recherche de socket dans les adresses online
def socket_find(addr):
    try:
        for i in stock_tab:
            return stock_tab[addr]
    except Exception:
        return


# enleve les addresses hors ligne
def remove_offline(addr):
    del stock_tab[addr]
