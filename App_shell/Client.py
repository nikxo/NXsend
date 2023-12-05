import socket
import fonction
import Menu
import sys
import threading
import queue

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

            Handler = threading.Thread(
                target=fonction.thread_chat_recv, args=(socket_,))
            Handler.start()

            Menu.chat_ascii()

            while (input_.lower() != 'return' or 'exit'):
                fonction.send_msg(socket_)

            # Handler.stop()

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
        # Handler.stop()
        print(str(e))
        sys.exit()