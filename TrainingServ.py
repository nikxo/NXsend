import socket
import threading


def thread_chat(conn, server):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        # Faites quelque chose avec les données reçues
        print(f"Données reçues: {data.decode('utf-8')}")
        # message
        message = "Message reçu"
        # Répondre au client
        conn.send(message.encode())

    addr.close()


# Adresse serveur
IP_Server = '192.168.0.51'
Port_Server = 4444
addr = (IP_Server, Port_Server)

# creation du serveur
Server = socket.create_server((IP_Server, Port_Server))


print(f"Serveur a l'ecoute sur {IP_Server}:{Port_Server}")

while True:
    conn, addr = Server.accept()
    print(f"Connection entrante : {addr}")
    Handler = threading.Thread(target=thread_chat, args=(conn, Server))
    Handler.start()
