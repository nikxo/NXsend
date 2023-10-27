import socket

# Adresse serveur
IP_Server = "127.0.0.1"
Port_Server = 4444

Server = socket.create_server((IP_Server, Port_Server))


while True:
    Server.listen()
