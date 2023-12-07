import customtkinter
from PIL import Image

light_mode_image_send = Image.open(
    "App_new_gen/build/assets/frame0/send-solid-132.png")
# Remplacez par votre chemin absolu ou relatif
dark_mode_image_send = Image.open(
    "App_new_gen/build/assets/frame0/send-solid-132.png")

light_mode_image_file = Image.open(
    "App_new_gen/build/assets/frame0/plus-regular-204.png")
# Remplacez par votre chemin absolu ou relatif
dark_mode_image_file = Image.open(
    "App_new_gen/build/assets/frame0/plus-regular-204.png")


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

app = customtkinter.CTk()
app.configure(fg_color="#707070")
app.title("my app")
app.geometry("852x511")
app.minsize(852, 511)

# Permet à la colonne principale de s'étendre
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=400)

# Permet à la ligne principale de s'étendre
app.grid_rowconfigure(0, weight=1)

frame_menu = customtkinter.CTkFrame(app)
frame_menu.configure(corner_radius=0, fg_color="#36373D", width=179)

# grille configuration
frame_menu.grid(column=0, row=0, sticky="nsw")
frame_menu.grid_columnconfigure(0, weight=1)
frame_menu.grid_rowconfigure(0, weight=40)
frame_menu.grid_rowconfigure(1, weight=1)


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


def send():
    # Passer en mode normal pour éditer le contenu
    text_box.configure(state='normal')
    text_box.insert(customtkinter.END, "Nouveau contenu\n")
    # Revenir en mode disabled pour empêcher l'édition
    text_box.configure(state='disabled')


frame_talk = customtkinter.CTkFrame(
    frame_main_right, fg_color="#2f3030", corner_radius=0, height=65)
frame_talk.grid(row=1, sticky="sew")
frame_talk.grid_columnconfigure(0, weight=1)

frame_entry = customtkinter.CTkFrame(frame_talk, fg_color="#36373D")
frame_entry.grid(column=0, sticky="we", pady=10, padx=10)
frame_entry.grid_columnconfigure(0, weight=1)
frame_entry.grid_columnconfigure(1, weight=30)
frame_entry.grid_columnconfigure(2, weight=1)
frame_entry.grid_rowconfigure(0, weight=1)


entry = customtkinter.CTkEntry(
    frame_entry, placeholder_text="Envoyer un message", border_width=0, corner_radius=0)
entry.grid(column=1)
entry.grid(pady=5, sticky="ew")

file_button = customtkinter.CTkButton(
    frame_entry, corner_radius=5, width=0, image=ctk_image_file, text="", fg_color="#36373D", hover=False, command=send)
file_button.grid(column=0, row=0)

send_button = customtkinter.CTkButton(
    frame_entry, corner_radius=5, width=0, image=ctk_image_send, text="", fg_color="#36373D", hover=False)
send_button.grid(column=2, row=0)


app.mainloop()
