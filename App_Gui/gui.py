from pathlib import Path
import fonction as f
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Entry,  Button, Text, Scrollbar, END, Y, RIGHT, LEFT, BOTH
from tkinter import Canvas, Entry, Button, PhotoImage
from tracemalloc import start
import threading
import socket

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("NKSend")
window.geometry("860x520")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=520,
    width=860,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    179.0,
    520.0,
    fill="#3C3C3C",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    518.0,
    474.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    518.0,
    474.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#3C3C3C",
    fg="#FFFFFF",
    highlightthickness=0,
    font=("Helvetica Neue", 10, "bold"),
)
entry_1.place(
    x=248.0,
    y=456.0,
    width=540.0,
    height=34.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    activebackground="#3C3C3C",  # Couleur d'arrière-plan lors du clic
)
button_1.place(
    x=795.0,
    y=462.0,
    width=24.0,
    height=24.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    activebackground="#3C3C3C",  # Couleur d'arrière-plan lors du clic
)
button_2.place(
    x=218.0,
    y=462.0,
    width=24.0,
    height=24.0
)

conn = f.setconnect()
Handler_recv = threading.Thread(
    target=f.thread_chat_recv, args=(conn,))
Handler_recv.start()
f.peer_conn(conn)


def show_msg_client(event=None):
    nom = "Nico: "
    message = entry_1.get()
    if message:
        conn.send(message.encode())
        text_messages.config(state='normal')
        # Insère le nom avec le tag 'red'
        text_messages.insert(END, nom, 'red')
        text_messages.insert(END, f"{message}\n")  # Ajoute le message
        # Configure le tag 'red' en rouge
        text_messages.tag_config('red', foreground='red')
        text_messages.yview_moveto(1)  # Fait défiler vers le bas
        text_messages.config(state='disabled')
        entry_1.delete(0, END)  # Efface le texte dans l'entrée après l'envoi


def show_msg_ext(event=None):
    while True:
        nom = "Server: "
        received_data = f.thread_chat_recv(conn)
        if received_data:
            text_messages.config(state='normal')
            text_messages.insert(END, nom, 'blue')
            text_messages.insert(END, f"{received_data}\n")
            text_messages.tag_config('blue', foreground='blue')
            text_messages.yview_moveto(1)
            text_messages.config(state='disabled')


Handler_show = threading.Thread(
    target=show_msg_ext, args=())
Handler_show.start()

entry_1.bind("<Return>", show_msg_client)

button_1 = window.children['!button']  # Récupère le bouton existant
button_1.config(command=show_msg_client)  # Met à jour la commande du bouton

text_messages = Text(window, bd=0, bg="#ffffff", fg="black",
                     font=("Helvetica Neue", 10, "bold"), wrap="word")
text_messages.place(x=210, y=0, width=615, height=450)

scrollbar = Scrollbar(window, command=text_messages.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_messages.config(yscrollcommand=scrollbar.set)

window.resizable(False, False)
window.mainloop()
