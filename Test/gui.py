from pathlib import Path
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


def on_hover(event):
    canvas.itemconfig("current", fill="#AAAAAA")


def on_leave_box(event):
    canvas.itemconfig("current", fill="#3C3C3C")


def on_leave_titre(event):
    canvas.itemconfig("current", fill="#FFFFFF")


def create_selectable_box(canvas, x, y, title):
    box_width = 159
    box_height = 40

    title_label = canvas.create_text(
        x + 10,
        y + 10,
        text=title,
        anchor="nw",
        fill="#FFFFFF",
        font=("Helvetica Neue", 12, "bold"),
        tags=("selectable",)
    )

    box = canvas.create_rectangle(
        x,
        y,
        x + box_width,
        y + box_height,
        fill="#3C3C3C",
        outline="",
        tags=("selectable",)
    )

    canvas.tag_bind(box, "<Button-1>", lambda event,
                    box=box: select_box(canvas, box))
    canvas.tag_bind(title_label, "<Button-1>", lambda event,
                    box=box: select_box(canvas, box))
    canvas.tag_bind(box, "<Enter>", on_hover)
    # canvas.tag_bind(title_label, "<Enter>", on_hover)
    canvas.tag_bind(box, "<Leave>", on_leave_box)
    # canvas.tag_bind(title_label, "<Leave>", on_leave_titre)


def select_box(canvas, box):
    canvas.itemconfig("selectable", fill="#3C3C3C")
    canvas.itemconfig(box, fill="blue")


create_selectable_box(canvas, 5, 0, "Box 1")
create_selectable_box(canvas, 5, 65, "Box 2")
create_selectable_box(canvas, 5, 130, "Box 3")


button_1 = window.children['!button']  # Récupère le bouton existant

text_messages = Text(window, bd=0, bg="#ffffff", fg="black",
                     font=("Helvetica Neue", 10, "bold"), wrap="word")
text_messages.place(x=210, y=0, width=615, height=450)

scrollbar = Scrollbar(window, command=text_messages.yview)
scrollbar.pack(side=RIGHT, fill=Y)
text_messages.config(yscrollcommand=scrollbar.set)

window.resizable(False, False)
window.mainloop()
