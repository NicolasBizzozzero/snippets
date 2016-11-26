from random import choice, randint
from tkinter import *
from personnages import *

class Interface():
    def __init__(self):
        self.window = Tk() # La fenêtre principale
        self.window.resizable(0, 0) # Empêcher les redimensionnements

        # Centre de la fenêtre
        self.partie_centrale = Frame(self.window)
        self.zone_graphique = Canvas(self.partie_centrale, width=500, height=400, bg="#FFFFCC")
        self.zone_graphique.pack()
        self.partie_centrale.pack()

        # Partie basse inférieure de la fenêtre
        self.partie_basse_inferieure = Frame(self.window)
        self.bouton_charger = Button(self.partie_basse_inferieure, text="Charger", command=self.charger)
        self.bouton_charger.pack(fill=X, side=RIGHT, expand=1)
        self.partie_basse_inferieure.pack(side=BOTTOM, fill=X)

        # Partie basse supérieure de la fenêtre
        self.partie_basse_superieure = Frame(self.window)
        self.bouton_defendre = Button(self.partie_basse_superieure, text="Se défendre", command=self.defendre)
        self.bouton_defendre.pack(fill=X, side=RIGHT, expand=1)
        self.bouton_attaquer = Button(self.partie_basse_superieure, text="Attaquer", command=self.attaquer)
        self.bouton_attaquer.pack(fill=X, side=RIGHT, expand=1)        
        self.partie_basse_superieure.pack(side=BOTTOM, fill=X)
        
        # Finalisations de la fenêtre
        self.window.title("La grande aventure")
        self.window.mainloop()


    def attaquer(self, other=None, type=None):
        pass


    def defendre(self):
        pass


    def charger(self, attaque=None):
        pass


ensemble_personnages = [
    Archer,
    Barde,
    Bouffon,
    Cavalier,
    Centaure,
    Courtisan,
    ChevalierBlanc,
    ChevalierNoir,
    Chronomancien,
    Dwemer,
    Ermite,
    Fee,
    GriffeMort,
    Guerrier,
    JoueurDeFlute,
    LoupGarou,
    MageBlanc,
    MageNoir,
    Marabou,
    Mathematicien,
    Mendiant,
    Medecin,
    Minotaure,
    Naiade,
    Nain,
    Ninja,
    Ogre,
    PercevalDeGalles,
    Poete,
    Pretre,
    Samourai,
    Seigneur,
    Serf,
    Sorciere,
    Voleur,
    Voyageur,
    VoyageurTemporel]



amina = choice(ensemble_personnages)("Amina", "femme")
nicolas = choice(ensemble_personnages)("Nicolas", "homme")

Interface()