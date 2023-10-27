import socket
from cryptography.fernet import Fernet
import threading

# Clé secrète partagée pour le chiffrement et le déchiffrement (AES-256)
# Remplacez par la clé partagée
shared_key = b'Dy5LKfiUhddspgn0qB0eH_pvmgkzLfOHkTnzb-yFV_I='

# Adresse IP et port du serveur
server_ip = '127.0.0.1'  # Remplacez par l'adresse IP du serveur
server_port = 12345       # Remplacez par le port du serveur

# Créez une socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adresse IP et port du client à qui vous souhaitez envoyer un message
other_client_ip = '172.20.10.6'  # Remplacez par l'adresse IP du destinataire
other_client_port = 12346      # Remplacez par le port du destinataire

# Fonction pour gérer la réception de messages du serveur


def receive_messages():
    while True:
        encrypted_data = client_socket.recv(4096)
        if not encrypted_data:
            break

        cipher_suite = Fernet(shared_key)
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        print(f"Message reçu : {decrypted_data.decode()}"\n)


# Connexion au serveur
client_socket.connect((server_ip, server_port))
print("Connecté au serveur.")

# Créez un thread pour gérer la réception de messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input("Message :")

    if message.lower() == 'exit':
        break

    # Chiffrez le message avec AES-256
    cipher_suite = Fernet(shared_key)
    encrypted_message = cipher_suite.encrypt(message.encode())

    # Envoyez le message au destinataire (autre client) via le serveur
    client_socket.send(encrypted_message)

# Fermez la connexion client
client_socket.close()
