import socket
import hashlib


def input_key():
    return input("Command : ")


def menu(menu_tab):
    print("""
  __  __                  
 |  \/  |                 
 | \  / | ___ _ __  _   _ 
 | |\/| |/ _ \ '_ \| | | |
 | |  | |  __/ | | | |_| |
 |_|  |_|\___|_| |_|\__,_|
                          
          """)
    for index, element in enumerate(menu_tab):
        print(f"{index + 1}) {element}")
