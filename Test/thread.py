import socket
import threading

# Adresse serveur
IP_Server = '192.168.0.51'
Port_Server = 4444
addr = (IP_Server, Port_Server)

# creation du serveur
Server = socket.create_server((IP_Server, Port_Server))
message = "recept"

while True:
    conn, addr = Server.accept()
    print(f"Connection entrante : {addr}")
    data = conn.recv(1024)
    if data:
        print(data.decode())
        conn.send(message.encode())
