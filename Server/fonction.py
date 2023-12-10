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

    def addr_is_in_db(addr):
        curseur.execute("SELECT adresse FROM addr WHERE adresse = ?", (addr,))
        result = curseur.fetchall()
        if result:
            return True
        return False

    def addr_is_online(addr):
        if addr_is_in_db(addr):
            curseur.execute(
                "SELECT status FROM addr WHERE adresse LIKE ? AND status = ?", (addr, "online"))
            resultats = curseur.fetchall()  # Récupérer les résultats de la requête
            if resultats:
                return True
            return False

    def get_socket(ip):
        curseur.execute("SELECT port FROM addr WHERE adresse = ?", (ip,))
        port = curseur.fetchone()
        if port:
            port_value = port[0]  # Extraction de la valeur de port du tuple
            return str(ip), int(port_value)
        return "nope"

    def peer_conn(data_dc):
        addr = get_socket(data_dc)
        if addr_is_online(addr[0]):
            return get_socket_storage(addr[0])
        print("offline")

    print(f"Handler start for {addr}")
    dest = None
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data_dc_id = data[0:6].decode('utf-8')
        data_dc = data[6:].decode('utf-8')
        if data_dc_id == 'IDDEST':
            dest = peer_conn(data_dc)
        if not dest:
            print("no socket found")
            break
        print(f"Données reçues: {data.decode('utf-8')}")
        if data.decode('utf-8') != data_dc:
            dest.send(data)
    conn.close()

    print(f"Handler for {addr} finish")


# Requete de connection au destinataire

socket_storage_dic = {}


def socket_storage(addr, conn):
    socket_storage_dic[addr] = conn


def get_socket_storage(addr):
    return socket_storage_dic[addr]

# etablit la connection avec l'adresse specifiée


def setconnect(addr):
    # Creation Socket de connection
    socket_ = socket.create_connection(addr)
    return socket_
