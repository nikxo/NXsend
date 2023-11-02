import socket

ip = '172.31.190.240'

Ip_Server = "192.168.0.51"
Port_Server = 12345

Socket = socket.create_connection((ip, 12345))
Server = socket.create_server((Ip_Server, Port_Server))

while True:
    message = input("Send : ")
    Socket.send(message.encode())
