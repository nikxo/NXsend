import socket
import fonction
# Adresse serveur

Menu = ["Connection", "Help", "Settings", "Exit"]

# lancement Menu par defaut
fonction.menu(Menu)

# affectation input_
input_ = fonction.input_key()

if (input_.lower() == 'connection'):
    fonction.connection()
    IP_Server = input('Ip du serveur : ')
    Port_Server = input('Port du serveur : ')
    # Creation Socket de connection
    addr = (f'{IP_Server}', Port_Server.replace("'", ""))
    socket_ = socket.create_connection(addr)
    print(f"Connection Reussi a {IP_Server}:{Port_Server}\n")

input_ = ""
while True:
    try:
        if (input_.lower() == 'menu'):
            fonction.menu(Menu)

        if (input_.lower() == 'connection'):
            fonction.connection()
            IP_Server = input('Ip du serveur : ')
            Port_Server = input('Port du serveur : ')
            # Creation Socket de connection
            addr = (f'{IP_Server}', Port_Server.replace("'", ""))
            socket_ = socket.create_connection(addr)
            print(f"Connection Reussi a {IP_Server}:{Port_Server}\n")

        if (input_.lower() == 'settings'):
            fonction.settings()

        if (input_.lower() == 'settings'):
            fonction.settings()

        if (input_.lower() == 'help'):
            fonction.help()

        if (input_.lower() == 'exit'):
            socket_.close()
            break
        else:
            input_ = fonction.input_key()

    except Exception as e:
        print(str(e))
