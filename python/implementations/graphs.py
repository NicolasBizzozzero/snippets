class Sommet():
    name = None

    def __init__(self, name):
        self.name = name


class Arc():
    sommet_interieur = None
    sommet_exterieur = None

    def __init__(self, sommet_interieur, sommet_exterieur):
        self.sommet_interieur = sommet_interieur
        self.sommet_exterieur = sommet_exterieur


class Graphe():
    ensemble_sommets = None
    ensemble_arcs = None

    def __init__(self):
        self.ensemble_sommets = set()
        self.ensemble_arcs = []

    def ajouter_sommet(self, sommet):
        self.ensemble_sommets.add(sommet)

    def ajouter_sommets(self, *sommets):
        for sommet in sommets:
            self.ensemble_sommets.add(sommet)

    def ajouter_arc(self, arc):
        self.ensemble_arcs.append(arc)

    def sommets(self):
        return self.ensemble_sommets

    def arcs(self):
        return self.ensemble_arcs

    def nombre_de_sommets(self):
        return len(self.ensemble_sommets)

    def nombre_arcs(self):
        return len(self.ensemble_arcs)


def parcours_largeur(graphe):
    parcours = set()

    voisins_non_visites = [None] * graphe.nombre_de_sommets()

    return parcours


if __name__ == '__main__':
    graphe = Graphe()
    somA = Sommet("A")
    somB = Sommet("B")
    somC = Sommet("C")
    somD = Sommet("D")
    somE = Sommet("E")
    somF = Sommet("F")
    somG = Sommet("G")
    somH = Sommet("H")
    graphe.ajouter_sommets(somA, somB, somC, somD, somE, somF, somG, somH)
    graphe.ajouter_arc(Arc(somA, somB))
    graphe.ajouter_arc(Arc(somA, somC))
    graphe.ajouter_arc(Arc(somB, somD))
    graphe.ajouter_arc(Arc(somB, somE))
    graphe.ajouter_arc(Arc(somE, somH))
    graphe.ajouter_arc(Arc(somC, somF))
    graphe.ajouter_arc(Arc(somC, somG))
    parcours = tuple(parcours_largeur(graphe))
    print(parcours)
