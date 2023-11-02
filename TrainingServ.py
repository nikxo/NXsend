import socket

# Adresse serveur
IP_Server = '127.0.0.1'
Port_Server = 12345
addr = (IP_Server, Port_Server)

Server = socket.create_server((IP_Server, Port_Server))


def decodeBuffer(buffer_):
    message = buffer_.decode('utf-8')
    return message


while True:
    Client_socket, Client_adresse = Server.accept()
    print(f"Connection entrante : {Client_adresse}")

    Server.recvmsg(buffer)
    print(decodeBuffer(buffer))
