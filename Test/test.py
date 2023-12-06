import customtkinter
from PIL import Image


def create_app():
    app = customtkinter.CTk()
    app.configure(fg_color="#707070")
    app.title("my app")
    app.geometry("1080x920")
    app.minsize(1080, 920)
    app.grid_columnconfigure(0, minsize=250)
    app.grid_columnconfigure(1, weight=20)
    app.grid_rowconfigure(0, weight=1)
    return app


def create_frame_menu(master):
    frame_menu = customtkinter.CTkFrame(master)
    frame_menu.grid_columnconfigure(0, weight=1)
    frame_menu.grid_rowconfigure(0, weight=20)
    frame_menu.grid_rowconfigure(1, weight=1)

    frame_menu.configure(corner_radius=0, fg_color="#3D85C6", width=250)
    frame_menu.grid(row=0, sticky="wns")

    menu_bar = customtkinter.CTkFrame(frame_menu)
    menu_bar.configure(corner_radius=0, fg_color="#4A4A4A",
                       height=50, width=250)
    menu_bar.grid(row=1, sticky="ws")


def create_conversation(master):
    conversation = customtkinter.CTkFrame(master)
    conversation.grid_rowconfigure(0, weight=20)
    conversation.grid_rowconfigure(1, weight=1)
    conversation.grid_columnconfigure(0, weight=1)

    conversation.configure(fg_color="#7A864C")
    conversation.grid(row=0, column=1, sticky="wnse")

    typing_elem = create_typing_elem(conversation)
    typing_elem.grid(row=1)


def create_typing_elem(master):
    typing_elem = customtkinter.CTkFrame(master)
    typing_elem.configure(fg_color="#E4EEFF", height=90)
    typing_elem.grid_rowconfigure(0, weight=1)
    typing_elem.grid_columnconfigure(0, weight=1)
    typing_elem.grid(sticky="wse")

    typing_elem_sub = create_typing_elem_sub(typing_elem)
    typing_elem_sub.grid(column=0)


def create_typing_elem_sub(master):
    typing_elem_sub = customtkinter.CTkFrame(master)
    typing_elem_sub.configure(fg_color="#CB8584", height=45)
    typing_elem_sub.grid_columnconfigure(0, weight=1)
    typing_elem_sub.grid_columnconfigure(1, weight=100)
    typing_elem_sub.grid_columnconfigure(2, weight=1)
    typing_elem_sub.grid(padx=20, pady=20, sticky="ew")

    typing_elem_entry = create_typing_elem_entry(typing_elem_sub)
    typing_elem_entry.grid(column=1)

    typing_elem_button = create_typing_elem_button(typing_elem_sub)
    typing_elem_button.grid(column=0, row=0)


def create_typing_elem_entry(master):
    typing_elem_entry = customtkinter.CTkEntry(master)
    typing_elem_entry.configure(border_color="#E4EEFF", border_width=0)
    typing_elem_entry.grid(sticky="wnse", padx=10, pady=10)


def create_typing_elem_button(master):
    typing_elem_button = customtkinter.CTkButton(master)
    image_ = create_image(typing_elem_button)
    typing_elem_button.configure(
        fg_color="#fcba03", width=2, height=2, image=image_)
    typing_elem_button.grid(sticky="ns")


def create_image(master):
    light_mode_image = Image.open(
        "App_new_gen/build/assets/frame0/plus-regular-204.png")
    dark_mode_image = Image.open(
        "App_new_gen/build/assets/frame0/plus-regular-204.png")
    image_ = customtkinter.CTkImage(master)
    image_.configure(light_image=light_mode_image, size=(20, 20))
    return image_


if __name__ == "__main__":
    app = create_app()
    create_conversation(app)
    create_frame_menu(app)
    app.mainloop()
