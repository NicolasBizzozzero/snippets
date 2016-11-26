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
    def __init__(self):
        self.pointsdevie = 
        self.attaquephysique = 
        self.pourcentageec, self.pourcentagecc =
        self.degatsec, self.degatscc =
        self.listecaracteristiques, self.listeattaques, self.listesorts = ["Eloquent", "Agile", "Fragile"], ["Coup de dague", "Coup de luth sur le crâne"], ["Chant ensorceleur"]


class Bouffon(Personnage):
    def __init__(self):
        self.pointsdevie = 
        self.attaquephysique = 
        self.pourcentageec, self.pourcentagecc =
        self.degatsec, self.degatscc =
        self.listecaracteristiques, self.listeattaques = ["Drôle", "Fragile"], ["Bouffonnerie","Jet de grelots"]


class Cavalier(Personnage):
    def __init__(self):
        self.pointsdevie = 
        self.attaquephysique = 
        self.pourcentageec, self.pourcentagecc =
        self.degatsec, self.degatscc = 
        self.listecaracteristiques, self.listeattaques = ["Athlétique", "Puissant"], ["Coup d'épée","Flèche"]
        self.defensephysique = "Bouclier"

       
class Centaure(Personnage):
    def __init__(self):
        self.pointsdevie = 
        self.attaquephysique = 
        self.pourcentageec, self.pourcentagecc =
        self.degatsec, self.degatscc = 
        self.listecaracteristiques, self.listeattaques = ["Rapide", "Puissant"], ["Coup de poing","Flèche"]


class Courtisan(Personnage):
    def __init__(self):
        self.pointsdevie = 
        self.attaquephysique = 
        self.pourcentageec, self.pourcentagecc =
        self.degatsec, self.degatscc = 
        self.listecaracteristiques, self.listeattaques = ["Obséquieux", "Faible"], ["Flatterie"]


class ChevalierBlanc(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Puissant", "Bon", "Courageux"], ["Coup d'epée blanche", "Lance"]
    self.defense = "Ecu blanc"


class ChevalierNoir(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Puissant","Courageux", "Ténébreux"], ["Coup d'epée noire", "Lance"]
    self.defense = "Ecu noir"


class Chronomancien(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Ponctuel", "Rapide"], ["Coup de sabre"], ["Ralentir"]
    

class Dwemer(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Intelligent", "Ambitieux"], ["Coup d'encyclopédie", "Robot guerrier"], ["Sortilège dwemer"]


class Ermite(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Solitaire", "Contemplatif"], ["Lancer de chaussures"]


class Fee(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Vole", "Rapide"], ["Coup de baguette magique dans l'oeil"], ["Sortilège féerique à pailletes"]


class GriffeMort(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Cheum", "Flippant", "Manucure-pédicure au top"], ["Coup de griffe"]


class Guerrier(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Athlétique", "Puissant", "Belliqueux", "Téméraire"], ["Coup d'épée", "Coup de dague", "Coups tout court"]
    self.defense = "Armure"


class JoueurDeFlute(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Fais des fausses notes"], ["Coup de flûte dans l'oeil"], ["Ensorcelement musical"]
    

class LoupGarou(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Poilu", "Puissant"], ["Morsure", "Coup de griffe"]


class MageBlanc(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Vieux", "Sage"], ["Coup de bâton"], ["Magie blanche"]


class MageNoir(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Vieux", "Sage"], ["Coup de bâton"], ["Magie noire"]


class Marabout(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Medium...ou pas"], ["Coup de poing"], ["Jet de bave de crapaud"]


class Mathematicien(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Voit les choses en dimension n"], ["Coup de compas"], ["Par le lemme de Steinitz je t'ensorcèle !"]


class Mendiant(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Pauvre"], ["Coup de couteau suisse"]


class Minotaure(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Puissant"], ["Coup de hache", "Coup de corne"]


class Naiade(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Agile"], ["Coup de poing"], ["Magie de l'eau"]


class Nain(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Petit"], ["Coup de poing"]


class Ninja(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Rusé", "Agile", "Rapide"], ["Ninjutsu", "Shuriken", "Coup de dague"]


class Ogre(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Grand", "Gros", "Peu futé"], ["Coup de poing"]


class Poete(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Rêveur"], ["Coup de rouleau de parchemin"]



class PercevalDeGalles(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques =


class Pretre(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Faible", "Spirituel...ou pas"], ["Coup de Bible"]


class Samourai(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Belliqueux", "Puissant", "Rapide"], ["Coup de katana", "Ju-jitsu"], ["Sauce samouraï magique"]


class Seigneur(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Riche"], ["Coup d'Epée"]


class Serf(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Prolétaire exploité"], ["Coup de fourche"]


class Sorciere(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts= ["Chapeau pointu"], ["Coup de baguette dans l'oeil"], ["Wingardium Leviosa", "Stupéfix", "Expelliarmus"]


class Voleur(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Rapide", "Agile", "Fourbe"], ["Coup de couteau"]


class Voyageur(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques = ["Rapide"], ["Coup de poing"]



class VoyageurTemporel(Personnage):
    self.pointsdevie = 
    self.attaquephysique = 
    self.pourcentageec, self.pourcentagecc =
    self.degatsec, self.degatscc = 
    self.listecaracteristiques, self.listeattaques, self.listesorts = ["Rapide"], ["Coup de poing"], ["Voyage dans le temps"]
