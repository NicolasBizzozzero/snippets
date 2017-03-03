# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas


class Maillon:
    """Créé un maillon utilisable avec un élément de la classe 'ListeChainee'."""

    def __init__(self, valeur, suivant=None):
        self.valeur = valeur
        self.suivant = suivant

    def __str__(self):
        """
            L'affichage d'un maillon retournera :
            [self.valeur, self.suivant]
        """
        return "[" + str(self.valeur) + ", " + str(self.suivant) + "]"

    def __eq__(self, other):
        """Deux maillons sont égaux si ils ont la même valeur."""
        if type(other) is Maillon:  # Si le type d'élément qu'on compare à self est un Maillon,
            # alors on returne True si leur valeur est égale.
            return self.valeur == other.valeur
        # Si les deux éléments ne sont pas du même type, alors ils sont
        # différents.
        return False


class ListeChainee:
    """Forme une chaine d'éléments de la classe 'Maillon'."""

    def __init__(self, chaine=None):
        self.premier_element = chaine
        self.dernier_element = None
        compteur = 0
        curseur = chaine
        while curseur:
            compteur += 1
            curseur = curseur.suivant
        self.longueur = compteur

    def __str__(self):
        """
            L'affichage d'une liste chainée retournera :
            [self.premier_element,
            [self.premier_element.suivant,
            [self.premier_element.suivant.suivant,
            [...]]]
        """
        return str(self.premier_element)

    def __eq__(self, other):
        """
            Deux listes chainées sont égales si tous leurs maillons ont
            la même valeur.
        """
        if type(other) is ListeChainee:  # Si le type d'élément qu'on compare à self est une ListeCHainee,
            if self.longueur != other.longueur:  # si leur longueur est différente,
                return False  # alors ils sont différents.
            # Sinon, on doit comparer tous leurs éléments.
            return self.premier_element == other.premier_element
        # Si les deux éléments ne sont pas du même type, alors ils sont
        # différents.
        return False

    def retire_en_tete(self):
        """
            Retire la première valeur au debut de la self chainée et
            retourne la valeur supprimée.
        """
        if self.longueur:  # Si la liste n'est pas vide,
            # alors on stocke la valeur supprimée dans une variable,
            valeur_supprimee = self.premier_element.valeur
            # et on supprime le maillon en tête de liste.
            self.premier_element = self.premier_element.suivant
            if self.longueur == 1:  # On réatribue la bonne valeur au dernier élément de la liste.
                self.dernier_element = None
            self.longueur -= 1  # On modifie la longueur de la liste.
            return valeur_supprimee

    def ajoute_en_fin(self, valeur):
        """Ajoute la valeur 'valeur' en tête de la self chainée."""
        nouveau = Maillon(valeur)
        if not self.longueur:  # Si la liste est vide,
            # alors on ajoute directement le nouveau maillon au debut.
            self.premier_element = nouveau
        else:
            # Sinon on l'ajoute normalement en fin.
            self.dernier_element.suivant = nouveau
        # On réatribue la bonne valeur au dernier élément de la liste.
        self.dernier_element = nouveau
        self.longueur += 1  # On modifie la longueur de la liste.

    def recherche(self, valeur):
        """Return 'True' si 'valeur' est dans la self, 'False' sinon."""
        curseur = self.premier_element  # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
        while curseur:  # Tant qu'il n'est pas vide,
            # on regarde si la valeur qu'on cherche est celle qu'on regarde.
            if valeur == curseur.valeur:
                return True
            curseur = curseur.suivant  # Sinon, on incrémente le curseur.
        # Quand on arrive au bout de la liste, alors la valeur n'est pas
        # dedans.
        return False

    def retire_index(self, index):
        """
            Retire la valeur à la position 'index' de la self et la
            retourne si elle existe. Retourne None sinon.
        """
        if (not self.premier_element) or (self.longueur - 1 < index):  # Si la liste est vide ou si l'index est trop grand,
            return None  # alors on ne retourne rien.
        if not index:  # Si l'index indique le premier élément de la liste,
            return self.retire_en_tete()  # alors on le retire.
        # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
        curseur = self.premier_element
        # On fait avancer le curseur jusqu'à l'élément avant celui qu'on désire
        # retirer.
        while index != 1:
            curseur = curseur.suivant
            index -= 1
        if not curseur.suivant.suivant:  # Si l'élément qu'on retire est le dernier,
            # alors on change l'attribut 'dernier_element' de self.
            self.dernier_element = curseur
        # On récupère la valeur de l'élément qu'on veut retirer,
        valeur = curseur.suivant.valeur
        curseur.suivant = curseur.suivant.suivant  # puis on supprime l'élément,
        self.longueur -= 1  # et on ajuste la valeur.
        return valeur

    def retire_valeur(self, valeur):
        """
            Retire la première occurence de 'valeur' et return
            'True' si elle existe dans 'self', 'False' sinon.
        """
        if not self.premier_element:  # Si la liste est vide,
            return False  # alors on retourne False.
        if self.premier_element.valeur == valeur:  # Si le premier élément a pour valeur 'valeur',
            # alors on le retire.
            self.premier_element = self.premier_element.suivant
            return True
        # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
        curseur = self.premier_element
        while curseur.suivant:  # On parcourt toute la liste.
            if curseur.suivant.valeur == valeur:  # Si on rencontre la valeur 'valeur',
                if not curseur.suivant.suivant:  # Si l'élément après celui qu'on va retirer est vide,
                    # alors on change l'attribut 'dernier_element' de self.
                    self.dernier_element = curseur
                # alors on retire le maillon correspondant.
                curseur.suivant = curseur.suivant.suivant
                return True
            curseur = curseur.suivant  # sinon, on incrémente le curseur.
        return False

    def retire_valeurs(self, valeur):
        """
            Retire toutes les occurences de 'valeur' et return
            'True' si elle existe dans 'self', 'False' sinon.
        """
        if not self.premier_element:  # Si la liste est vide,
            return False  # alors on retourne False.
        existence_valeur = False
        # On retire en boucle les premieres valeurs de la liste egales à
        # 'valeur'.
        while self.premier_element.valeur == valeur:
            self.premier_element = self.premier_element.suivant
            existence_valeur = True
        # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
        curseur = self.premier_element
        while curseur.suivant:  # On parcourt toute la liste.
            if curseur.suivant.valeur == valeur:  # Si on rencontre la valeur 'valeur',
                # alors on retire le maillon correspondant.
                curseur.suivant = curseur.suivant.suivant
                existence_valeur = True
                continue
            curseur = curseur.suivant  # sinon, on incrémente le curseur.
        return existence_valeur

    def copie(self):
        """Retourne une copie de self."""
        liste_a_renvoyer = ListeChainee()
        curseur = self.premier_element
        while curseur:
            liste_a_renvoyer.ajoute_en_fin(curseur.valeur)
            curseur = curseur.suivant
        return liste_a_renvoyer

    def concatenation(self, liste):
        """
            Concatène 'self' avec 'liste' en rajoutant une copie de 'liste'
            dans 'self' et ne retourne rien.
        """
        copie = liste.copie()
        self.dernier_element.suivant = copie.premier_element
        self.dernier_element = copie.dernier_element
        self.longueur += copie.longueur


class ListeChaineeTriee(ListeChainee):
    """Forme une chaine d'éléments de la classe 'Maillon' triés."""

    def ajout(self, valeur):
        """Ajoute 'valeur' dans self."""
        nouveau = Maillon(valeur)
        curseur = self.premier_element
        if self.premier_element.valeur >= valeur:
            self.premier_element, self.premier_element.suivant = nouveau, self.premier_element
            self.longueur += 1
            return
        while curseur.suivant:
            if curseur.suivant.valeur >= valeur:
                curseur.suivant, curseur.suivant.suivant = nouveau, curseur.suivant
                self.longueur += 1
                return
            curseur = curseur.suivant
        curseur.suivant, curseur.suivant.suivant = nouveau, curseur.suivant
        self.dernier_element = nouveau
        self.longueur += 1

    def recherche(self, valeur):
        curseur = self.premier_element
        while curseur:
            if curseur.valeur == valeur:
                return True
            if curseur.valeur > valeur:
                return False
            curseur = curseur.suivant
        return False


if __name__ == "__main__":
    liste = ListeChaineeTriee(
        Maillon(4,
                Maillon(8,
                        Maillon(15,
                                Maillon(16,
                                        Maillon(23,
                                                Maillon(42)))))))

    liste2 = ListeChainee()
    liste2.ajoute_en_fin(4)
    liste2.ajoute_en_fin(8)
    liste2.ajoute_en_fin(15)
    liste2.ajoute_en_fin(16)
    liste2.ajoute_en_fin(23)
    liste2.ajoute_en_fin(42)

    print(liste)
    print(liste2)
    print(liste.recherche(14))
