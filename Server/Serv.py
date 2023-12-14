import socket
import threading
import fonction as f
import Sql

# Adresse serveur
IP_Server = '147.215.205.186'
Port_Server = 4444
addr_Server = (IP_Server, Port_Server)

# creation du serveur
Server = socket.create_server((IP_Server, Port_Server))
print(f"Serveur a l'ecoute sur {IP_Server}:{Port_Server}")


while True:
    conn, addr = Server.accept()
    print(addr)
    f.socket_storage(addr[0], conn)
    print(f"Connection entrante : {addr}")

    if Sql.addr_is_in_db(addr[0]) == False:
        Sql.socket_storage(addr)
        print(f"{addr}ajouté a la database")

    Handler = threading.Thread(
        target=f.thread_chat, args=(conn, addr))
    Handler.start()
