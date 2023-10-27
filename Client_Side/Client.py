import socket
import fonction
# Adresse serveur
IP_Server = '172.31.190.240'
Port_Server = 12345
Menu = ["Help", "Settings", "Exit"]


# Creation Socket de connection
addr = (IP_Server, Port_Server)
socket_ = socket.create_connection(addr)
print(f"Connection Reussi a {IP_Server}:{Port_Server}")

# affectation input_
input_ = fonction.input_key()

while True:
    try:
        if (input_.lower() == 'menu'):
            fonction.menu(Menu)

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
