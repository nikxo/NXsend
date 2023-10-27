import socket

# Adresse serveur
IP_Server = '127.0.0.1'
Port_Server = 12345
addr = (IP_Server, Port_Server)

Server = socket.create_server((IP_Server, Port_Server))

while True:
    Client_socket, Client_adresse = Server.accept()
    print(f"Connection entrante : {Client_adresse}")
