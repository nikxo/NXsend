import customtkinter
from PIL import Image
import os

app = customtkinter.CTk()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.configure(fg_color="#707070")
        self.title("my app")
        self.geometry("1080x920")
        self.minsize(1080, 920)
        self.grid_columnconfigure(0, minsize=250)
        self.grid_columnconfigure(1, weight=20)

        self.grid_rowconfigure(0, weight=1)


class frame_menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=20)
        self.grid_rowconfigure(1, weight=1)

        # Bar des conversations
        self.configure(
            corner_radius=0, fg_color="#3D85C6", width=250)
        self.grid(row=0, sticky="wns")

        # bar de profil
        self.menu_bar = customtkinter.CTkFrame(self)
        self.menu_bar.configure(
            corner_radius=0, fg_color="#4A4A4A", height=50, width=250)
        self.menu_bar.grid(row=1, sticky="ws")


# customtkinter.CTkEntry()


class Conversation(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=20)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0, weight=1)

        # Configure la couleur de premier plan du cadre
        self.configure(fg_color="#7A864C")
        self.grid(row=0, column=1, sticky="wnse")

        typing_elem_class = typing_elem(self)
        typing_elem_class.grid(row=1)


class typing_elem(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(fg_color="#E4EEFF", height=90)

        self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.grid(sticky="wse")

        typing_elem_sub_class = typing_elem_sub(self)
        typing_elem_sub_class.grid(column=0)


# customtkinter.CTkFrame()

class typing_elem_sub(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#CB8584", height=45)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=1)
        self.grid(padx=20, pady=20, sticky="ew")

        typing_elem_entry_class = typing_elem_entry(self)
        typing_elem_entry_class.grid(column=1)


class typing_elem_entry(customtkinter.CTkEntry):
    def __init__(self, master):
        super().__init__(master)
        # Entry bar
        self.configure(border_color="#E4EEFF", border_width=0)
        self.grid(sticky="wnse", padx=40, pady=10)


if __name__ == "__main__":
    app = App()
    Conversation(app)
    frame_menu(app)
    app.mainloop()
