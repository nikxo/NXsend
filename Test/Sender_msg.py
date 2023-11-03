import socket

ip = '192.168.0.51'

Client_Socket = socket.create_connection((ip, 4444))

while True:
    message = input("Send : ")
    Client_Socket.send(message.encode())
    while True:
        data = Client_Socket.recv(1024)
        if data:
            print(data.decode('utf-8'))
            break
