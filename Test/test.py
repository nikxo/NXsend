import customtkinter as ctk

# Fonction appelée lorsque l'utilisateur appuie sur le bouton de connexion


def on_login_button_click():
    username = entry_username.get()
    password = entry_password.get()
    print(f"Username: {username}, Password: {password}")
    # Ici, vous pouvez ajouter la logique pour vérifier les identifiants


# Création de la fenêtre principale
root = ctk.CTk()
root.title('Page de Connexion')
root.geometry('400x300')

# Création du champ d'entrée du nom d'utilisateur
label_username = ctk.CTkLabel(root, text="Nom d'utilisateur:")
label_username.pack(pady=10)
entry_username = ctk.CTkEntry(
    root, placeholder_text="Entrez votre nom d'utilisateur")
entry_username.pack()

# Création du champ d'entrée du mot de passe
label_password = ctk.CTkLabel(root, text="Mot de passe:")
label_password.pack(pady=10)
entry_password = ctk.CTkEntry(
    root, placeholder_text="Entrez votre mot de passe", show='*')
entry_password.pack()

# Création du bouton de connexion
button_login = ctk.CTkButton(
    root, text="Connexion", command=on_login_button_click)
button_login.pack(pady=20)

# Démarrer l'interface graphique
root.mainloop()
