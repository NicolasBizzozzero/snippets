from random import randint
from tkinter import *


class Interface:
    """Interface principale du jeu."""
    def __init__(self, grille=[[randint(0, 1) for i in range(13)] for j in range(19)]):
        """La grille est une liste de listes."""
        self.grille = grille
        self.window = Tk()    # la fenêtre principale
        self.window.resizable(0, 0)    # empêcher les redimensionnements

        # Début de la partie haute de la fenêtre
        self.partie_haute = Frame(self.window, bd=0)
        self.bouton_options = Button(self.partie_haute, text="Options")
        self.bouton_options.pack(fill=X, side=RIGHT, expand=1)
        self.bouton_recommencer = Button(self.partie_haute, text="Recommencer")
        self.bouton_recommencer.pack(fill=X, side=RIGHT, expand=1)
        self.bouton_boutique = Button(self.partie_haute, text="Boutique")
        self.bouton_boutique.pack(fill=X, side=RIGHT, expand=1)
        self.partie_haute.pack(side=TOP, fill=X, expand=1)


        # Début du centre de la fenêtre
        self.partie_centrale = Frame(self.window, bd=0)
        self.zone_graphique = Canvas(self.partie_centrale, width=500, height=400, bg="#FFFFCC")
        self.zone_graphique.pack()
        self.partie_centrale.pack()


        # Finalisations de la fenêtre
        self.window.title("MineSweeper")
        self.window.mainloop()






class Boutique:
    pass


class Argent:
    pass


class Mine:
    pass








GUI = Interface()
for i in range(len(GUI.grille)-1):
    print(GUI.grille[i])