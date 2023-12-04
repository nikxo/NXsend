import socket
import threading
import fonction as f


# Adresse serveur
IP_Server = '147.215.205.114'
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
    if f.addr_is_online(addr):
        break
    print(f"Connection entrante : {addr}")
    f.socket_storage(addr, conn)
    f.addr_storage(addr)
    Handler = threading.Thread(
        target=f.thread_chat, args=(conn, addr_Server))
    Handler.start()
