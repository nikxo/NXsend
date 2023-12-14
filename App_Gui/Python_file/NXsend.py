import customtkinter
import tkinter as tk
from tkinter import END, filedialog
from PIL import Image, ImageTk, ImageDraw
import threading
import fonction as f
import Sql_client as slc
import random
import socket
import os
import signal


Thread = []
sync_resquest_old = None


dark_mode_image_send = Image.open(
    "frame0/send-solid-132.png")
dark_mode_image_file = Image.open(
    "frame0/plus-regular-204.png")
dark_mode_image_param = Image.open(
    "frame0/parametres.png")
dark_mode_image_add = Image.open(
    "frame0/ajouter-un-utilisateur.png")
dark_mode_image_idle = Image.open(
    "frame0/warning.png")
dark_mode_image_profile = Image.open(
    "frame0/def.png")
dark_mode_image_profile_param = Image.open(
    "frame0/def.png")

# Création de l'objet CTkImage
ctk_image_send = customtkinter.CTkImage(
    dark_image=dark_mode_image_send,
    size=(25, 25)  # Taille de l'image pour le rendu indépendant du scaling
)
ctk_image_file = customtkinter.CTkImage(
    dark_image=dark_mode_image_file,
    size=(25, 25)  # Taille de l'image pour le rendu indépendant du scaling
)
ctk_image_param = customtkinter.CTkImage(
    dark_image=dark_mode_image_param,
    size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
)
ctk_image_add = customtkinter.CTkImage(
    dark_image=dark_mode_image_add,
    size=(20, 20)  # Taille de l'image pour le rendu indépendant du scaling
)
ctk_image_idle = customtkinter.CTkImage(
    dark_image=dark_mode_image_idle,
    size=(80, 80)  # Taille de l'image pour le rendu indépendant du scaling
)
ctk_image_profile = customtkinter.CTkImage(
    dark_image=dark_mode_image_profile,
    size=(30, 30)  # Taille de l'image pour le rendu indépendant du scaling
)
ctk_image_profile_param = customtkinter.CTkImage(
    dark_image=dark_mode_image_profile_param,
    size=(50, 50)  # Taille de l'image pour le rendu indépendant du scaling
)


# Contact window
def windows_add():
    def sendBT():
        name = entry_name.get()
        ip = entry_ip.get()
        print(name, ip)
        if name and ip:
            if f.verifier_ip(ip):
                add(name, ip)
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
    f.center_window(toplevel, app)

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

    frame_ip = customtkinter.CTkFrame(
        toplevel, fg_color="#242424", height=35)
    frame_ip.grid(column=0, row=2, padx=15)

    entry_ip = customtkinter.CTkEntry(
        frame_ip, corner_radius=0, border_width=0, fg_color="#242424", justify="center", placeholder_text="Ajouter une ip")
    entry_ip.grid(padx=10, pady=2)

    Boutton = customtkinter.CTkButton(
        toplevel, fg_color="black", text="Add", image=ctk_image_add, command=sendBT)
    Boutton.grid(column=0, row=3, pady=(30, 0))


def show_msg_ext(text_box, conn, stop_event):
    try:
        while not stop_event.is_set():
            nom = "Server: "
            received_data = f.thread_chat_recv(conn)
            if received_data:
                slc.add_db_msg(last_bt_id, nom, received_data)
                text_box.configure(state='normal')
                text_box.insert(END, nom, 'blue')
                text_box.insert(END, f"{received_data}\n")
                text_box.tag_config('blue', foreground='blue')
                text_box.yview_moveto(1)
                text_box.configure(state='disabled')
    except Exception as e:
        print(e)


def create_rounded_image(path, size):
    # Load the image
    image = Image.open(path)
    image = image.resize(size, Image.Resampling.LANCZOS)

    # Create a mask
    mask = Image.new('L', size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0) + size, fill=255)

    # Apply the mask to the image
    rounded_image = Image.new('RGBA', size)
    rounded_image.paste(image, (0, 0), mask)
    return rounded_image


def windows_settings():
    def sendBT():
        global name_user
        global socket_
        name_user = entry_name.get()
        server_ip = entry_ip.get()
        server_port = entry_port.get()
        socket_ = socket.create_connection((server_ip, server_port))
        stop_event = threading.Event()
        Handler_show = threading.Thread(
            target=show_msg_ext, args=(text_box, socket_, stop_event))
        Thread.append((Handler_show, stop_event))
        Handler_show.start()
        toplevel.destroy()

    toplevel = customtkinter.CTkToplevel(app)
    toplevel.configure(fg_color="#2f3030")
    toplevel.geometry("200x300")
    toplevel.maxsize(200, 270)
    toplevel.minsize(200, 270)
    toplevel.after(10, toplevel.lift)
    toplevel.focus_force()
    toplevel.grab_set()
    toplevel.grid_columnconfigure(0, weight=1)
    toplevel.grid_rowconfigure(0, weight=0)
    toplevel.grid_rowconfigure(1, weight=0)
    toplevel.grid_rowconfigure(2, weight=0)
    toplevel.grid_rowconfigure(3, weight=0)
    toplevel.grid_rowconfigure(4, weight=0)
    f.center_window(toplevel, app)

    # label = customtkinter.CTkLabel(
    #     toplevel, text="Settings", font=("Helvetica Neue", 20, "bold"), justify="center")
    # label.grid(column=0, row=0, pady=15)

    # Calcul des coordonnées pour placer le cadre au milieu de la fenêtre
    frame_name = customtkinter.CTkFrame(
        toplevel, fg_color="#242424", height=35)
    frame_name.grid(column=0, row=1, padx=15, pady=(0, 15))

    entry_name = customtkinter.CTkEntry(
        frame_name, corner_radius=0, border_width=0, fg_color="#242424", justify="center", placeholder_text="Ajouter un nom", font=("Helvetica Neue", 12))
    entry_name.grid(padx=10, pady=2)

    frame_ip = customtkinter.CTkFrame(
        toplevel, fg_color="#242424", height=35)
    frame_ip.grid(column=0, row=2, padx=15, pady=(0, 15))

    entry_ip = customtkinter.CTkEntry(
        frame_ip, corner_radius=0, border_width=0, fg_color="#242424", justify="center", placeholder_text="Server ip")
    entry_ip.grid(padx=10, pady=2)

    frame_port = customtkinter.CTkFrame(
        toplevel, fg_color="#242424", height=35)
    frame_port.grid(column=0, row=3, padx=15, pady=(0, 15))

    entry_port = customtkinter.CTkEntry(
        frame_port, corner_radius=0, border_width=0, fg_color="#242424", justify="center", placeholder_text="Server port")
    entry_port.grid(padx=10, pady=2)

    Boutton = customtkinter.CTkButton(
        toplevel, fg_color="black", text="Apply", command=sendBT)
    Boutton.grid(column=0, row=4)

    # Round image button
    profile_button = customtkinter.CTkButton(
        toplevel, image=ctk_image_profile_param, command=sendBT, text="", fg_color="transparent", hover=False, width=40, height=40)  # Replace 'sendBT' with your intended command
    profile_button.grid(column=0, row=0, pady=15)


def on_button_click(button_id, ip):
    global last_bt_id
    global sync_resquest_old

    print("Bouton appuyé!")
    print("ID du bouton:", button_id)

    # if last_bt_id is None:
    #     toggle_visibility()
    #     last_bt_id = button_id

    if last_bt_id == button_id:
        toggle_visibility(False)
        last_bt_id = None
    if last_bt_id != button_id:
        toggle_visibility(True)
        last_bt_id = button_id

    sync = f"IDDEST{ip}"
    if sync != sync_resquest_old:
        sync_resquest_old = sync
        socket_.send(sync.encode())
    text_box.configure(state='normal')
    text_box.delete(1.0, END)
    slc.show_db_msg(text_box, button_id, name_user)
    text_box.configure(state='disabled')
    print(last_bt_id)


def add(name, ip):
    name_var = tk.StringVar()
    name_var.set(name)
    boutton_contact = customtkinter.CTkButton(
        frame_scrollBox, width=177, height=43, textvariable=name_var, fg_color="#242424", hover_color="#2e2e2e", font=("Ubuntu", 12, "bold"), image=ctk_image_profile, compound='left', anchor='w')
    boutton_contact.grid(column=0, padx=5, pady=3, sticky="ew")

    # Génération de l'identifiant du bouton
    boutton_id = str(name) + str(random.randint(1, 1000))
    id_to_widget[boutton_contact] = boutton_id

    # Utilisation d'une fonction lambda pour passer l'ID au clic du bouton
    boutton_contact.bind("<Button-1>", lambda event,
                         id=boutton_id: on_button_click(id, ip))
    slc.create_db(boutton_id)


def toggle_visibility(visible):
    if visible:
        text_box.grid(row=0, sticky="nswe", padx=10)
        frame_talk.grid(row=1, sticky="sew")
        Idel_Label.grid_remove()
    else:
        frame_talk.grid_remove()
        text_box.grid_remove()
        Idel_Label.grid(column=0, row=0)


def stop_all_thread():
    app.destroy()
    for handler, event in Thread:
        event.set()  # Signaler au thread de s'arrêter
        handler.join(timeout=3)  # Attendre que le thread se termine
        socket_.close()
        print("Handlers Close")


try:
    # param
    id_to_widget = {}
    last_bt_id = None
    name_user = "User"
    ip_server = None
    port_server = None
    socket_ = None
    ip_dest = None

    app = customtkinter.CTk()
    app.configure(fg_color="#2f3030")
    app.title("NXsend")
    app.geometry("852x511")
    app.minsize(852, 511)
    app.maxsize(852, 511)
    customtkinter.set_appearance_mode("dark")

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
        frame_menu, width=187, corner_radius=0)
    frame_scrollBox.grid(column=0, row=0, sticky="nsw")

    frame_boutton = customtkinter.CTkFrame(
        frame_menu, corner_radius=0, height=40, fg_color="#242424")
    frame_boutton.grid(column=0, row=1, sticky="sew")
    frame_boutton.grid_rowconfigure(0, weight=1)
    frame_boutton.grid_columnconfigure(0, weight=0)
    frame_boutton.grid_columnconfigure(1, weight=0)

    boutton_add = customtkinter.CTkButton(
        frame_boutton, width=90, height=40, image=ctk_image_add, text="", fg_color="#242424", hover_color="#2e2e2e", command=windows_add)
    boutton_add.grid(column=0, padx=2, pady=2)

    boutton_options = customtkinter.CTkButton(
        frame_boutton, width=90, height=40, image=ctk_image_param, text="", fg_color="#242424", hover_color="#2e2e2e", command=windows_settings)
    boutton_options.grid(column=1, row=0, padx=2, pady=2)

    frame_main_right = customtkinter.CTkFrame(
        app, fg_color="#2f3030", corner_radius=0)

    # Right_container = customtkinter.CTkFrame(app)
    frame_main_right.grid(column=1, row=0, sticky="nsew")
    frame_main_right.grid_columnconfigure(0, weight=1)
    frame_main_right.grid_rowconfigure(0, weight=100)
    frame_main_right.grid_rowconfigure(1, weight=1)

    Idel_Label = customtkinter.CTkLabel(
        frame_main_right, text="Select/Add conversation", text_color="white", font=("Ubuntu", 20, "bold"), image=ctk_image_idle, compound='top')
    Idel_Label.grid(column=0, row=0)

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
        frame_entry, corner_radius=5, width=0, image=ctk_image_send, text="", fg_color="#242424", hover=False, command=lambda: f.show_msg_client(entry, text_box, last_bt_id, name_user, socket_))
    send_button.grid(column=2, row=0)

    entry.bind("<Return>", lambda event: f.show_msg_client(
        entry, text_box, last_bt_id, name_user, socket_))

    # Créer une variable pour suivre l'état actuel de visibilité de l'entrée et du texte
    frame_talk.grid_remove()
    text_box.grid_remove()
    # Définir une fonction pour basculer la visibilité de l'entrée et du texte

    app.protocol("WM_DELETE_WINDOW", stop_all_thread)
    app.mainloop()
except Exception as e:
    print(e)
