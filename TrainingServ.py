import socket


# Adresse serveur
IP_Server = '172.31.190.240'
Port_Server = 12345
addr = (IP_Server, Port_Server)

# buffer = str(1024)

Server = socket.create_server((IP_Server, Port_Server))

print(f"Serveur a l'ecoute sur {IP_Server}:{Port_Server}")

conn, addr = Server.accept()
print(f"Connection entrante : {addr}")
# data = conn.recv(4096)
# print("Received data:", data.decode())

Dest = conn.recv(4096)

try:
    Server.connect(Dest)

except Exception as e:
    print("error dest")

while True:
    try:
        data = conn.recv(4096)
        if data:
            Server.sendto(data, Dest)
    except Exception as e:
        print(str(e))
