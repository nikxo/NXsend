import socket
import hashlib


def input_key(type_key='commande'):
    if (type_key.lower() == 'config'):
        return input("Config : ")
    if (type_key.lower() == 'chat'):
        return input("Chat : ")
    if (type_key.lower() == 'file Send'):
        return input("File Send : ")
    if (type_key.lower() == 'commande'):
        return input("Commande : ")


# def input_key():
#     return input("Commande : ")


def setconnect(type):
    if (type.lower() == 'server relay' or type.lower() == '1'):
        ip_server = input('Ip du serveur : ')
        port_server = input('Port du serveur : ')
        # Creation Socket de connection
        addr = (f'{ip_server}', port_server.replace("'", ""))
        socket_ = socket.create_connection(addr)
        print(f"Connection Reussi a {ip_server}:{port_server}\n")
        return ip_server, port_server, socket_
    elif (type.lower() == 'autonomous relay' or type.lower() == '2'):
        print("\nUnder devlopement")
        print("Switch to Server Relay\n")
        return setconnect('1')


def statconnect(ip_server, port_server):
    print("Connecté à :")
    print(f"Ip du serveur : {ip_server}")
    print(f"Port du serveur : {port_server}\n")


def type_verif(input_, type_key='commande'):
    if input_.lower() not in ['server relay', 'autonomous relay', '1', '2']:
        print("Invalide entry")
        input_ = input_key(type_key)
        type_verif(input_)
    else:
        return input_


def send_msg(socket_):
    socket_.sendall("test")
