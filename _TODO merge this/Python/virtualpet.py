from tkinter import *

fenetre = Tk()

champ_label = Label(fenetre, text = "Welcome to our shop !")
# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()