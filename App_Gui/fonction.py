import socket
import customtkinter
from queue import Queue
import tkinter as tk
from tkinter import END
from PIL import Image
import Sql_client as slc
import re
import gui_new
# Etablit la connection au serveur


def setconnect():
    # Creation Socket de connection
    addr = ('147.215.206.144', 4444)
    socket_ = socket.create_connection(addr)
    return socket_


# Definit un pair distant
def peer_conn(conn):
    conn.send(b"IDDEST"
              #   + dest.encode()
              )


# Envoi les messages au serveur
def send_msg(client_socket):
    message = input("Chat : ")
    client_socket.send(message.encode())


# Crée une file d'attente pour stocker les données reçues
received_data_queue = Queue()


# reçois les messages (Thread)
def thread_chat_recv(conn):
    while True:
        data = conn.recv(1024)
        if data:
            print("reçu")
            decoded_data = data.decode('utf-8')
            # Met les données dans la file d'attente pour un traitement ultérieur
            received_data_queue.put(decoded_data)
            return received_data_queue.get()


def ctk_image_send_():
    light_mode_image_send = Image.open(
        "App_new_gen/build/assets/frame0/send-solid-132.png")
    # Remplacez par votre chemin absolu ou relatif
    dark_mode_image_send = Image.open(
        "App_new_gen/build/assets/frame0/send-solid-132.png")

    # Création de l'objet CTkImage
    ctk_image_send = customtkinter.CTkImage(
        light_image=light_mode_image_send,
        dark_image=dark_mode_image_send,
        size=(25, 25)  # Taille de l'image pour le rendu indépendant du scaling
    )
    return ctk_image_send_


def ctk_image_file_():
    light_mode_image_file = Image.open(
        "App_new_gen/build/assets/frame0/plus-regular-204.png")
    # Remplacez par votre chemin absolu ou relatif
    dark_mode_image_file = Image.open(
        "App_new_gen/build/assets/frame0/plus-regular-204.png")

    ctk_image_param = customtkinter.CTkImage(
        light_image=light_mode_image_file,
        dark_image=dark_mode_image_file,
        size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
    )
    return ctk_image_file_


def ctk_image_param_():
    light_mode_image_param = Image.open(
        "App_new_gen/build/assets/frame0/parametres.png")
    # Remplacez par votre chemin absolu ou relatif
    dark_mode_image_param = Image.open(
        "App_new_gen/build/assets/frame0/parametres.png")
    ctk_image_add = customtkinter.CTkImage(
        light_image=light_mode_image_param,
        dark_image=dark_mode_image_param,
        size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
    )
    return ctk_image_param_


def ctk_image_add_():
    light_mode_image_add = Image.open(
        "App_new_gen/build/assets/frame0/ajouter-un-utilisateur.png")
    # Remplacez par votre chemin absolu ou relatif
    dark_mode_image_add = Image.open(
        "App_new_gen/build/assets/frame0/ajouter-un-utilisateur.png")

    ctk_image_add = customtkinter.CTkImage(
        light_image=light_mode_image_add,
        dark_image=dark_mode_image_add,
        size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
    )
    return ctk_image_add_


def verifier_ip(adresse):
    # Modèle d'expression régulière pour vérifier une adresse IP
    modele_ip = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

    # Vérification de correspondance avec l'expression régulière
    correspondance = re.match(modele_ip, adresse)

    if correspondance:
        # Si l'adresse correspond au format IP
        groupes = correspondance.groups()
        # Vérification des parties de l'adresse IP
        if all(0 <= int(groupe) <= 255 for groupe in groupes):
            return True
        else:
            return False
    else:
        return False


def show_msg_ext(text_box, conn, event=None):
    while True:
        nom = "Server: "
        received_data = thread_chat_recv(conn)
        if received_data:
            slc.add_db_msg(gui_new.get_id, nom, received_data)
            text_box.configure(state='normal')
            text_box.insert(END, nom, 'blue')
            text_box.insert(END, f"{received_data}\n")
            text_box.tag_config('blue', foreground='blue')
            text_box.yview_moveto(1)
            text_box.configure(state='disabled')


def show_msg_client(entry, text_box, table_id, name_user, conn, event=None):
    nom = f"{name_user}: "
    message = entry.get()
    if message:
        slc.add_db_msg(table_id, nom, message)
        conn.send(message.encode())
        print("send")
        text_box.configure(state='normal')
        # Insère le nom avec le tag 'red'
        text_box.insert(END, nom, 'red')
        text_box.insert(END, f"{message}\n")  # Ajoute le message
        # Configure le tag 'red' en rouge
        text_box.tag_config('red', foreground='red')
        text_box.yview_moveto(1)  # Fait défiler vers le bas
        text_box.configure(state='disabled')
        entry.delete(0, END)  # Efface le texte dans l'entrée après l'envoi


def center_window(window, parent):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    parent_width = parent.winfo_width()
    parent_height = parent.winfo_height()
    x = (parent_width // 2) - (width // 2) + parent.winfo_x()
    y = (parent_height // 2) - (height // 2) + parent.winfo_y()
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
