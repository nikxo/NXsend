import threading
import time
from queue import Queue
import socket
import sql
import sqlite3


def thread_chat(conn, addr):

    # stoque les asockets en ligne
    connexion = sqlite3.connect('Server/Server.db')

    # Créer un curseur
    curseur = connexion.cursor()

    def get_socket(ip):
        curseur.execute(
            "SELECT adresse, port FROM addr WHERE adresse = ?", (ip,))
        return curseur.fetchall()

    def peer_conn(conn, data):
        while True:
            data = conn.recv(1024)
            print(data)
            if (data[0:6]).decode('utf-8') == 'IDDEST':
                print("pass")
                dest = get_socket(data[6:])
                print("pass")
                return setconnect(dest)

    print(f"Handler start for {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        dest = peer_conn(conn, data)
        print(f"Données reçues: {data.decode('utf-8')}")
        dest.send(data)
    conn.close()
    print(f"Handler for {addr} finish")


# Requete de connection au destinataire


# etablit la connection avec l'adresse specifiée
def setconnect(addr):
    # Creation Socket de connection
    socket_ = socket.create_connection(addr)
    return socket_
