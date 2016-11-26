from random import choice, randint
from tkinter import *


class Personnage():
    def __init__(self, nom, sexe, vivant=True, pointsdevie=100, pointsdemagie=100, attaquephysique=10, attaquemagique=10,
        defensephysique=5, defensemagique=5, pourcentageec=5, pourcentagecc=95, degatsec=0.5, degatscc=1.5, pointsdexperience=0, niveau=1,
        listecaracteristiques=[], listeattaques=[], listesorts=[]):
        self.nom, self.sexe, self.vivant = nom, sexe, vivant
        self.pointsdevie, self.pointsdemagie = pointsdevie, pointsdemagie
        self.attaquephysique, self.attaquemagique = attaquephysique, attaquemagique
        self.defensephysique, self.defensemagique = defensephysique, defensemagique
        self.pourcentageec, self.pourcentagecc = pourcentageec, pourcentagecc
        self.degatsec, self.degatscc = degatsec, degatscc
        self.pointsdexperience, self.niveau = pointsdexperience, niveau
        self.listecaracteristiques, self.listeattaques, self.listesorts = listecaracteristiques, listeattaques, listesorts


    def __str__(self):
        if self.sexe == "femme":
            return "Damoiselle " + str(self.nom) + " la " + str(self.__class__.__name__)
        return "Damoiseau " + str(self.nom) + " le " + str(self.__class__.__name__)


    def attaque(self, other, typedattaque, charge=1):
        jet = randint(1, 100)
        if jet <= self.pourcentageec:
            print(self.nom, "a fait un echec critique.")
            degatsphysiques, degatsmagiques = self.attaquephysique * self.degatsec, self.attaquemagique * self.degatsec
        elif jet >= self.pourcentagecc:
            print(self.nom, "a fait un coup critique !")
            degatsphysiques, degatsmagiques = self.attaquephysique * self.degatscc, self.attaquemagique * self.degatscc
        else:
            degatsphysiques, degatsmagiques = self.attaquephysique, self.attaquemagique
        if typedattaque == "physique":
            other.pointsdevie -= degatsphysiques*charge - other.defensephysique
        elif typedattaque == "magique":
            other.pointsdevie -= degatsmagiques*charge - other.defensemagique


    def charge(self):
        """Fais passer le tour du personnage mais ajoute un multiplicateur à sa prochaine attaque."""
        pass


class Archer(Personnage):
    def __init__(self):
        self.pointsdevie = 120
        self.attaquephysique = 8
        self.pourcentageec, self.pourcentagecc = 4, 90
        self.degatsec, self.degatscc = 0.8, 1.75
        self.listecaracteristiques, self.listeattaques = ["Rapide", "Agile", "Moins puissant"], ["Flèche", "Coup de dague"]


class Barde(Personnage):
    pass


class Bouffon(Personnage):
    pass


class Cavalier(Personnage):
    pass


class Centaure(Personnage):
    pass


class Courtisan(Personnage):
    pass


class ChevalierBlanc(Personnage):
    pass


class ChevalierNoir(Personnage):
    pass


class Chronomancien(Personnage):
    pass


class Dwemer(Personnage):
    pass


class Ermite(Personnage):
    pass


class Fee(Personnage):
    pass


class GriffeMort(Personnage):
    pass


class Guerrier(Personnage):
    pass


class JoueurDeFlute(Personnage):
    pass


class LoupGarou(Personnage):
    pass


class MageBlanc(Personnage):
    pass


class MageNoir(Personnage):
    pass


class Marabou(Personnage):
    pass


class Mathematicien(Personnage):
    pass


class Mendiant(Personnage):
    pass


class Medecin(Personnage):
    pass


class Minotaure(Personnage):
    pass


class Naiade(Personnage):
    pass


class Nain(Personnage):
    pass


class Ninja(Personnage):
    pass


class Ogre(Personnage):
    pass


class Poete(Personnage):
    pass


class PercevalDeGalles(Personnage):
    pass


class Pretre(Personnage):
    pass


class Samourai(Personnage):
    pass


class Seigneur(Personnage):
    pass


class Serf(Personnage):
    pass


class Sorciere(Personnage):
    pass


class Voleur(Personnage):
    pass


class Voyageur(Personnage):
    pass


class VoyageurTemporel(Personnage):
    pass