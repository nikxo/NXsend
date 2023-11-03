import socket
import fonction
import Menu
import sys

# Listes Menu pour affichage
Menu_ = ["Chat", "File Send", "Help", "Settings", "Exit"]
Menu_Chat = ["Settings", "Retour", "Exit"]
Menu_Connect = ["Server Relay", "Autonomous Relay"]

# Listes Menu pour verification
Menu_lower = ["chat", "file send", "help", "settings", "exit"]
Menu_Chat_lower = ["settings", "retour", "exit"]
Menu_Connect_lower = ["server relay", "autonomous relay"]

# Dernier menu
Menu_Hist = []

# Defaut connection page
Menu.connection(Menu_Connect)

# recuperation des entrées
input_ = fonction.input_key()

# Verifie l'entrée utilisateur et ce connecte au server
try:
    input_verify = fonction.type_verif(input_)
    ip_server, port_server, socket_ = fonction.setconnect(input_verify)
except Exception as e:
    print(f"\n{str(e)}")
    sys.exit()


# lancement Menu par defaut
Menu.menu(Menu_, ip_server, port_server)


input_ = ""
while True:
    try:
        if (input_.lower() == 'menu'):
            Menu.menu(Menu_, ip_server, port_server)

        elif (input_.lower() == 'chat'):
            Menu_Hist.append('chat')
            Menu.chat_ascii()
            request = fonction.input_key('chat')
            while True:
                if (request.lower() in [item.lower() for item in Menu_Chat_lower]):
                    if (request.lower() == 'retour'):
                        result = Menu_Hist[-1]
                        Menu.result()

                else:
                    print("invalide")
                    request = fonction.input_key('chat')

        elif (input_.lower() == 'settings'):
            Menu.settings()

        elif (input_.lower() == 'help'):
            Menu.help()

        elif (input_.lower() == 'exit'):
            socket_.close()
            break
        else:
            input_ = fonction.input_key()

    except Exception as e:
        print(str(e))
        sys.exit()
