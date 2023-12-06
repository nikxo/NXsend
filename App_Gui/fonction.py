import socket
import hashlib
from queue import Queue


# Etablit la connection au serveur
def setconnect():
    # Creation Socket de connection
    addr = ('147.215.206.144', 4444)
    socket_ = socket.create_connection(addr)
    return socket_


# Definit un pair distant
def peer_conn(conn):
    conn.send(b"IDDEST"
              #   + dest.encode()
              )


# Envoi les messages au serveur
def send_msg(client_socket):
    message = input("Chat : ")
    client_socket.send(message.encode())


# Crée une file d'attente pour stocker les données reçues
received_data_queue = Queue()


# reçois les messages (Thread)
def thread_chat_recv(conn):
    while True:
        data = conn.recv(1024)
        if data:
            print("reçu")
            decoded_data = data.decode('utf-8')
            # Met les données dans la file d'attente pour un traitement ultérieur
            received_data_queue.put(decoded_data)
            return received_data_queue.get()
