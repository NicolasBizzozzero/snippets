#### Codeur principal : BIZZOZZERO Nicolas
#### Assistante pas très très compétente : DJELLOUL Amina
from tkinter import *
from random import choice


class Interface:
    def __init__(self):
        self.window = Tk()        # la fenêtre principale
        self.window.resizable(0, 0)        # empêcher les redimensionnements

        # Début de la partie haute de la fenêtre
        self.partie_haute = Frame(self.window, bd=0)
        self.bouton_quitter = Button(self.partie_haute, text="Quitter", command=self.window.destroy)
        self.bouton_quitter.pack(fill=X, side=RIGHT, expand=1)
        self.bouton_boutique = Button(self.partie_haute, text="Boutique", command=self.boutique)
        self.bouton_boutique.pack(fill=X, side=RIGHT, expand=1)
        self.partie_haute.pack(side=TOP, fill=X, expand=1)

        # Début du côté gauche de la fenêtre
        self.partie_gauche = Frame(self.window, bd=0)
        self.partie_gauche.pack(side=LEFT)

        # Début du centre de la fenêtre
        self.partie_centrale = Frame(self.window, bd=0)
        self.zone_graphique = Canvas(self.partie_centrale, width=500, height=400, bg="#FFFFCC")
        #self.zone_graphique.create_text(text="Points de vie: ", fill="black")
        self.zone_graphique.pack()
        self.partie_centrale.pack()

        # Début du côté droit de la fenêtre
        self.partie_droite = Frame(self.window, bd=0)
        self.partie_droite.pack(side=RIGHT)

        # Début de la partie basse de la fenêtre
        self.partie_basse = Frame(self.window, bd=0)
        self.bouton_nettoyer = Button(self.partie_basse, text="Nettoyer", command=self.nettoyer)
        self.bouton_nettoyer.pack(fill=X, side=RIGHT, expand=1)
        self.bouton_nourrir = Button(self.partie_basse, text="Nourrir", command=self.nourrir)
        self.bouton_nourrir.pack(fill=X, side=RIGHT, expand=1)
        self.bouton_entrainer = Button(self.partie_basse, text="Entrainer", command=self.entrainer)
        self.bouton_entrainer.pack(fill=X, side=RIGHT, expand=1)
        self.partie_basse.pack(side=BOTTOM, fill=X)

        # Finalisations de la fenêtre
        self.window.title("Tamagotchi")
        self.window.mainloop()

    ### Définition des boutons ###
    def nourrir(self):
        pass

    def boutique(self):
        pass

    def nettoyer(self):
        pass

    def entrainer(self):
        pass

    ### Définition des fonctions
    def actualisation_points_de_vie():
        pdv = Personnage.POINTSDEVIE
        return pdv

class Personnage:
    def __init__(self):
        self.SEXE = choice(["Mâle", "Femelle"])
        if self.SEXE is "Mâle":
            self.NOM = choice(["Nicolas", "Zeid", "Valentin", "Laurent", "Thomas", "GILBERT"])
        else:
            self.NOM = choice(["Amina", "Gaëlle", "Meghann", "Mélanie Oudart"])
        self.AGE = 0.0
        self.POINTSDEVIE = 100
        self.EXPERIENCE = 0
        self.COMPETENCES = dict()
        self.VETEMENTS = list()

    def apparence(self, sexe, vetements):
        if self.sexe is "Mâle":
            pass
        else:
            pass
        if self.vetements:
            pass
        else:
            pass

Tamagotchi = Personnage()
print(Tamagotchi.SEXE)
print(Tamagotchi.NOM)
Interface()