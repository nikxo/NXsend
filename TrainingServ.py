import socket


# Adresse serveur
IP_Server = '172.31.190.240'
Port_Server = 12345
addr = (IP_Server, Port_Server)

# buffer = str(1024)

Server = socket.create_server((IP_Server, Port_Server))

print(f"Serveur a l'ecoute sur {IP_Server}:{Port_Server}")

Client_socket, Client_adresse = Server.accept()
print(f"Connection entrante : {Client_adresse}")


while True:
    try:
        conn, addr = Server.accept()

        data = conn.recv(4096)

        while True:
            if not data:
                print("break")
                break
        print("Received data:", data.decode())
    except Exception as e:
        print(str(e))

    print(data.decode())
