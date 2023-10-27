import socket
from cryptography.fernet import Fernet
import threading

# Adresse serveur
IP_Server = "127.0.0.1"
Port_Server = 4444

# Creation Socket de connection
Sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = socket.create_connection((IP_Server, Port_Server))


if (connection == True):
    print("Connection Succes")
else:
    print("fail")
