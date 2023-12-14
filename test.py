import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk


class ChatApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("500x500")
        self.title("ChatBox with Profile Images")

        # Canvas and scrollbar for messages
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill="both", expand=True)

        # This frame will contain all the messages and profile images
        self.messages_container = ctk.CTkFrame(self.canvas)
        self.canvas_frame = self.canvas.create_window(
            (0, 0), window=self.messages_container, anchor="nw")

        self.messages_container.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Load the profile image (replace 'path_to_profile_image.png' with the actual image path)
        # Replace with the correct path to your image
        profile_image_path = "def.png"
        self.profile_image = Image.open(profile_image_path)
        self.profile_image = ImageTk.PhotoImage(
            self.profile_image.resize((50, 50), Image.Resampling.LANCZOS))

        # Add a few example messages
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")
        self.add_message("Hello, this is a test message!", "Username")
        self.add_message("This is another message.", "AnotherUser")

    def add_message(self, text, username):
        # Each message will be in its own frame for layout control
        message_frame = ctk.CTkFrame(self.messages_container)
        message_frame.pack(padx=10, pady=5, fill="x", expand=True)

        # Create a label for the profile image
        profile_label = ctk.CTkLabel(message_frame, image=self.profile_image)
        profile_label.image = self.profile_image  # keep a reference
        profile_label.pack(side="left", padx=10)

        # Create a label for the username and message text
        message_label = ctk.CTkLabel(message_frame, text=f"{username}: {text}")
        message_label.pack(side="left", padx=10)

        # Update the canvas scrollregion
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
