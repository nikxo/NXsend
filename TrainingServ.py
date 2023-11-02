import socket


# Adresse serveur
IP_Server = '192.168.0.51'
Port_Server = 4444
addr = (IP_Server, Port_Server)


Server = socket.create_server((IP_Server, Port_Server))

print(f"Serveur a l'ecoute sur {IP_Server}:{Port_Server}")

conn, addr = Server.accept()
print(f"Connection entrante : {addr}")


Dest = conn.recv(4096)

try:
    Server.connect(Dest)

except Exception as e:
    print("error dest")

while True:
    conn, addr = Server.accept()
    print(f"Connection entrante : {addr}")
    try:
        data = conn.recv(4096)
        if data:
            Server.sendto(data, Dest)
    except Exception as e:
        print(str(e))
