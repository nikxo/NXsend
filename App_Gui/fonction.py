import socket
import customtkinter
from queue import Queue
import tkinter as tk
from tkinter import END
from PIL import Image


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
