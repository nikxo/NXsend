import socket
import threading
import fonction as f
import sql

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
    print(f"Connection entrante : {addr}")

    if sql.addr_is_in_db(addr[0]) == False:
        sql.socket_storage(addr)
        print(f"{addr}ajouté a la database")

    Handler = threading.Thread(
        target=f.thread_chat, args=(conn, addr))
    Handler.start()
