import socket
import fonction
# Adresse serveur

Menu = ["Connection", "Help", "Settings", "Exit"]

# lancement Menu par defaut
fonction.menu(Menu)

# recuperation des entrées
input_ = fonction.input_key()


if (input_.lower() == 'connection'):
    fonction.connection()
    socket_ = fonction.setconnect()


input_ = ""
while True:
    try:
        if (input_.lower() == 'menu'):
            fonction.menu(Menu)

        if (input_.lower() == 'connection'):
            fonction.connection()
            socket_ = fonction.setconnect()

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
