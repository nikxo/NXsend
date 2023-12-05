import threading
import time
from queue import Queue
import socket
import Sql
import sqlite3


def thread_chat(conn, addr):

    # stoque les asockets en ligne
    connexion = sqlite3.connect('Server/Server.db')

    # Créer un curseur
    curseur = connexion.cursor()

    def get_socket(ip):
        curseur.execute("SELECT port FROM addr WHERE adresse = ?", (ip,))
        port = curseur.fetchone()
        if port:
            port_value = port[0]  # Extraction de la valeur de port du tuple
            return str(ip), int(port_value)
        return "nope"

    def peer_conn(conn, data):
        while True:
            data = conn.recv(1024)
            data_dc_id = data[0:6].decode('utf-8')
            data_dc = data[6:].decode('utf-8')
            if data_dc_id == 'IDDEST':
                addr = get_socket(data_dc)
                if addr:
                    return setconnect(addr)

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
