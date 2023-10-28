import socket
import fonction
import Menu
import sys

# List Menu
Menu_ = ["Chat", "File Send", "Help", "Settings", "Exit"]
Menu_Connect = ["Server Relay", "Autonomous Relay"]

# Defaut connection page
Menu.connection(Menu_Connect)

# recuperation des entrées
input_ = fonction.input_key()

# Verifie l'entrée utilisateur et ce connecte au server
try:
    fonction.type_verif(input_)
    ip_server, port_server, socket_ = fonction.setconnect(input_)
except Exception as e:
    print(f"\n{str(e)}")
    sys.exit()


# lancement Menu par defaut
Menu.menu(Menu_, ip_server, port_server)


input_ = ""
while True:
    try:
        if (input_.lower() == 'menu'):
            Menu.menu(Menu, ip_server, port_server)

        if (input_.lower() == 'connection'):
            Menu.connection(Menu_Connect)
            fonction.type_verif(input_)
            socket_ = fonction.setconnect(input_)

        if (input_.lower() == 'settings'):
            Menu.settings()

        if (input_.lower() == 'help'):
            Menu.help()

        if (input_.lower() == 'exit'):
            socket_.close()
            break
        else:
            input_ = fonction.input_key()

    except Exception as e:
        print(str(e))
        sys.exit()
