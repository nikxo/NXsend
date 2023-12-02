import socket
import threading
import fonction

# Adresse serveur
IP_Server = '192.168.0.51'
Port_Server = 4444
addr_Server = (IP_Server, Port_Server)


# Adresse redirection
IP_Dest = '192.168.0.51'
Port_Dest = 4444
addr_Dest = (IP_Server, Port_Server)


# creation du serveur
Server = socket.create_server((IP_Server, Port_Server))

print(f"Serveur a l'ecoute sur {IP_Server}:{Port_Server}")

while True:
    conn, addr = Server.accept()
    print(f"Connection entrante : {addr}")
    Handler = threading.Thread(
        target=fonction.thread_chat, args=(conn, addr_Server, addr_Dest))
    Handler.start()
