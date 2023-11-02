import socket

ip = '127.0.0.1'
Socket = socket.create_connection((ip, 12345))

message = "test"

Socket.send(message.encode())
