import customtkinter
import tkinter as tk
from tkinter import END
from PIL import Image
import re
import threading
import random
import Sql_client as slc
import sqlite3
light_mode_image_send = Image.open(
    "App_Gui/frame0/send-solid-132.png")
# Remplacez par votre chemin absolu ou relatif
dark_mode_image_send = Image.open(
    "App_Gui/frame0/send-solid-132.png")

light_mode_image_file = Image.open(
    "App_Gui/frame0/plus-regular-204.png")
# Remplacez par votre chemin absolu ou relatif
dark_mode_image_file = Image.open(
    "App_Gui/frame0/plus-regular-204.png")

light_mode_image_param = Image.open(
    "App_Gui/frame0/parametres.png")
# Remplacez par votre chemin absolu ou relatif
dark_mode_image_param = Image.open(
    "App_Gui/frame0/parametres.png")

light_mode_image_add = Image.open(
    "App_Gui/frame0/ajouter-un-utilisateur.png")
# Remplacez par votre chemin absolu ou relatif
dark_mode_image_add = Image.open(
    "App_Gui/frame0/ajouter-un-utilisateur.png")

# Création de l'objet CTkImage
ctk_image_send = customtkinter.CTkImage(
    light_image=light_mode_image_send,
    dark_image=dark_mode_image_send,
    size=(25, 25)  # Taille de l'image pour le rendu indépendant du scaling
)

ctk_image_file = customtkinter.CTkImage(
    light_image=light_mode_image_file,
    dark_image=dark_mode_image_file,
    size=(25, 25)  # Taille de l'image pour le rendu indépendant du scaling
)

ctk_image_param = customtkinter.CTkImage(
    light_image=light_mode_image_param,
    dark_image=dark_mode_image_param,
    size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
)

ctk_image_add = customtkinter.CTkImage(
    light_image=light_mode_image_add,
    dark_image=dark_mode_image_add,
    size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
)

app = customtkinter.CTk()
app.configure(fg_color="#36373D")
app.title("my app")
app.geometry("852x511")
app.minsize(852, 511)


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


def windows():

    def sendBT():
        name = entry_name.get()
        ip = entry_ip.get()
        print(name, ip)
        if name and ip:
            if verifier_ip(ip):
                add(name)
                toplevel.destroy()
            else:
                print("fdp une ip")

    toplevel = customtkinter.CTkToplevel(app)
    toplevel.configure(fg_color="#2f3030")
    toplevel.geometry("200x210")
    toplevel.maxsize(200, 210)
    toplevel.minsize(200, 210)
    toplevel.after(10, toplevel.lift)
    toplevel.focus_force()
    toplevel.grab_set()
    toplevel.grid_columnconfigure(0, weight=1)
    toplevel.grid_rowconfigure(0, weight=0)
    toplevel.grid_rowconfigure(1, weight=0)
    toplevel.grid_rowconfigure(2, weight=0)

    label = customtkinter.CTkLabel(
        toplevel, text="Contact", font=("Helvetica Neue", 20, "bold"), justify="center")
    label.grid(column=0, row=0, pady=15)

    # Calcul des coordonnées pour placer le cadre au milieu de la fenêtre
    frame_name = customtkinter.CTkFrame(
        toplevel, fg_color="#242424", height=35)
    frame_name.grid(column=0, row=1, padx=15, pady=(0, 15))

    entry_name = customtkinter.CTkEntry(
        frame_name, corner_radius=0, border_width=0, fg_color="#242424", justify="center", placeholder_text="Ajouter un nom", font=("Helvetica Neue", 12))
    entry_name.grid(padx=10, pady=2)

    frame_ip = customtkinter.CTkFrame(toplevel, fg_color="#242424", height=35)
    frame_ip.grid(column=0, row=2, padx=15)

    entry_ip = customtkinter.CTkEntry(
        frame_ip, corner_radius=0, border_width=0, fg_color="#242424", justify="center", placeholder_text="Ajouter une ip")
    entry_ip.grid(padx=10, pady=2)

    Boutton = customtkinter.CTkButton(
        toplevel, fg_color="black", text="Add", image=ctk_image_add, command=sendBT)
    Boutton.grid(column=0, row=3, pady=(30, 0))


# Permet à la colonne principale de s'étendre
app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=400)

# Permet à la ligne principale de s'étendre
app.grid_rowconfigure(0, weight=1)

frame_menu = customtkinter.CTkFrame(app)
frame_menu.configure(corner_radius=0, fg_color="#242424", width=179)

# grille configuration
frame_menu.grid(column=0, row=0, sticky="nsw")
frame_menu.grid_columnconfigure(0, weight=1)
frame_menu.grid_rowconfigure(0, weight=40)
frame_menu.grid_rowconfigure(1, weight=0)

frame_scrollBox = customtkinter.CTkScrollableFrame(
    frame_menu, width=172, corner_radius=0)
frame_scrollBox.grid(column=0, row=0, sticky="nsw")

# Dictionnaire pour mapper des IDs à des widgets
id_to_widget = {}
last_bt_id = ""


def on_button_click(button_id):
    global last_bt_id
    print("Bouton appuyé!")
    print("ID du bouton:", button_id)
    last_bt_id = button_id
    text_box.configure(state='normal')
    text_box.delete(1.0, END)
    show_db_msg(button_id)
    text_box.configure(state='disabled')


def add(name):
    name_var = tk.StringVar()
    name_var.set(name)
    boutton_contact = customtkinter.CTkButton(
        frame_scrollBox, width=170, height=40, textvariable=name_var, fg_color="#242424", hover_color="#2e2e2e", font=("Helvetica Neue", 12, "bold"))
    boutton_contact.grid(column=0, padx=2, pady=2, sticky="ew")

    # Génération de l'identifiant du bouton
    boutton_id = str(name) + str(random.randint(1, 1000))
    id_to_widget[boutton_contact] = boutton_id

    # Utilisation d'une fonction lambda pour passer l'ID au clic du bouton
    boutton_contact.bind("<Button-1>", lambda event,
                         id=boutton_id: on_button_click(id))
    slc.create_db(boutton_id)


def show_db_msg(table_id):
    # stoque les asockets en ligne
    connexion = sqlite3.connect(f"App_Gui/Base/{table_id}.db")
    # Créer un curseur
    curseur = connexion.cursor()

    curseur.execute("SELECT name, message FROM msg")
    rows = curseur.fetchall()
    text_box.configure(state='normal')
    # Affiche les données de chaque ligne
    for row in rows:
        name, message = row  # Accéder individuellement aux colonnes 'name' et 'message'

        # Insère le nom avec le tag 'red'
        text_box.insert(END, name, 'red')
        text_box.insert(END, f"{message}\n")  # Ajoute le message
        # Configure le tag 'red' en rouge
        text_box.tag_config('red', foreground='red')
        text_box.yview_moveto(1)

    text_box.configure(state='disabled')


def show_msg_client(table_id, event=None):
    nom = "User: "
    message = entry.get()
    if message:
        print("bf")
        slc.add_db_msg(table_id, nom, message)
        # conn.send(message.encode())
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


def show_msg_ext(event=None):
    while True:
        nom = "Server: "
        received_data = f.thread_chat_recv(conn)
        if received_data:
            text_box.configure(state='normal')
            text_box.insert(END, nom, 'blue')
            text_box.insert(END, f"{received_data}\n")
            text_box.tag_config('blue', foreground='blue')
            text_box.yview_moveto(1)
            text_box.configure(state='disabled')

#  Handler_show = threading.Thread(
#     target=show_msg_ext, args=())
# Handler_show.start()


frame_boutton = customtkinter.CTkFrame(
    frame_menu, corner_radius=0, height=40, fg_color="#242424")
frame_boutton.grid(column=0, row=1, sticky="sew")
frame_boutton.grid_rowconfigure(0, weight=1)
frame_boutton.grid_columnconfigure(0, weight=0)
frame_boutton.grid_columnconfigure(1, weight=0)

boutton_add = customtkinter.CTkButton(
    frame_boutton, width=90, height=40, image=ctk_image_add, text="", fg_color="#242424", hover_color="#2e2e2e", command=windows)
boutton_add.grid(column=0, padx=2, pady=2)

boutton_options = customtkinter.CTkButton(
    frame_boutton, width=90, height=40, image=ctk_image_param, text="", fg_color="#242424", hover_color="#2e2e2e")
boutton_options.grid(column=1, row=0, padx=2, pady=2)

frame_main_right = customtkinter.CTkFrame(
    app, fg_color="#2f3030", corner_radius=0)


Right_container = customtkinter.CTkFrame(app)
frame_main_right.grid(column=1, row=0, sticky="nsew")
frame_main_right.grid_columnconfigure(0, weight=1)
frame_main_right.grid_rowconfigure(0, weight=100)
frame_main_right.grid_rowconfigure(1, weight=1)


text_box = customtkinter.CTkTextbox(
    frame_main_right, fg_color="#2f3030", state='disabled', corner_radius=0)
text_box.grid(row=0, sticky="nswe", padx=10)

frame_talk = customtkinter.CTkFrame(
    frame_main_right, fg_color="#2f3030", corner_radius=0, height=65)
frame_talk.grid(row=1, sticky="sew")
frame_talk.grid_columnconfigure(0, weight=1)

frame_entry = customtkinter.CTkFrame(frame_talk, fg_color="#242424")
frame_entry.grid(column=0, sticky="we", pady=10, padx=10)
frame_entry.grid_columnconfigure(0, weight=0)
frame_entry.grid_columnconfigure(1, weight=30)
frame_entry.grid_columnconfigure(2, weight=0)
frame_entry.grid_rowconfigure(0, weight=1)


entry = customtkinter.CTkEntry(
    frame_entry, placeholder_text="Envoyer un message", border_width=0, corner_radius=0, fg_color="#242424")
entry.grid(column=1)
entry.grid(pady=5, sticky="ew")

file_button = customtkinter.CTkButton(
    frame_entry, corner_radius=5, width=0, image=ctk_image_file, text="", fg_color="#242424", hover=False)
file_button.grid(column=0, row=0)

send_button = customtkinter.CTkButton(
    frame_entry, corner_radius=5, width=0, image=ctk_image_send, text="", fg_color="#242424", hover=False, command=lambda: show_msg_client(last_bt_id))
send_button.grid(column=2, row=0)

entry.bind("<Return>", lambda event: show_msg_client(last_bt_id))

app.mainloop()
