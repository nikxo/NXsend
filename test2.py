import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()
root.title("Exemple de Textbox avec Frames Verts")

# Création d'une Text widget
text_box = tk.Text(root, height=20, width=50)
text_box.pack()

# Insertion de 20 représentations de frames verts
for i in range(20):
    text_box.insert(tk.END, "[Frame Vert {}]\n".format(i+1))

# Lancement de la boucle Tkinter
root.mainloop()
