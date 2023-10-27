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
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liste pour stocker les connexions clientes
client_sockets = []

# Verrou pour gérer les opérations de la liste client_sockets de manière sécurisée
client_sockets_lock = threading.Lock()

# Fonction pour gérer une connexion cliente


def handle_client(client_socket):
    while True:
        # Recevez les données chiffrées du client
        encrypted_data = client_socket.recv(4096)  # Taille du tampon

        if not encrypted_data:
            break

        # Créez un objet Fernet avec la clé partagée
        cipher_suite = Fernet(shared_key)

        # Décryptez les données
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        print(f"Données reçues : {decrypted_data.decode()}")

        # Traitez les données ici, par exemple, envoi à d'autres clients
        relay_message(decrypted_data, client_socket)


def relay_message(message, sender_socket):
    with client_sockets_lock:
        for client_socket in client_sockets:
            # Évitez de renvoyer le message à l'expéditeur
            if client_socket != sender_socket:
                try:
                    # Chiffrez le message avec AES-256
                    cipher_suite = Fernet(shared_key)
                    encrypted_message = cipher_suite.encrypt(message)

                    # Envoyez le message chiffré à d'autres clients
                    client_socket.send(encrypted_message)
                except Exception as e:
                    print(f"Erreur lors du relais du message : {str(e)}")


# Écoutez les connexions entrantes
server_socket.bind((server_ip, server_port))
server_socket.listen(5)  # Acceptez jusqu'à 5 connexions en attente

print("En attente de connexions...")

while True:
    # Acceptez la connexion entrante
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    # Ajoutez le client_socket à la liste
    with client_sockets_lock:
        client_sockets.append(client_socket)

    # Créez un thread pour gérer le client
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket,))
    client_thread.start()

# Fermez la socket du serveur
server_socket.close()
