# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas, TP1
#
# Ajouts :
# - Ajout d'une zone d'affichage d'un compteur de nombre de coups s'actualisant si le joueur clique sur 'Réinitialiser le plateau'.
# - Modification du message de fin de jeu. Le jeu affiche maintenant 'Vous avez gagné !' en cas de victoire (si tout le plateau est vide),
#   et 'Vous avez perdu :(' en cas de défaite (si il ne reste que des pièces de taille 1).
#
# Imports ---------------------------------------------------------------------
from tkinter import Tk, Frame, Button, BOTH, Canvas, TOP, BOTTOM, ALL
import tkinter.font
import random

COULEURS = ["red", "blue", "green", "yellow", "magenta"]


def initialiserPlateau(largeur, hauteur, couleurs = COULEURS):
    """Renvoie un plateau largeur x hauteur aléatoire de blocs de couleurs."""
    return [[random.choice(couleurs) for compteur1 in range(hauteur)] for compteur2 in range(largeur)]


def detecterPiece(plateau, x, y, piece, couleur):
    """Remplit l'ensemble piece, initialement vide, à l'aide des coordonnées
    des entrées du plateau appartenant à la même pièce que plateau[x][y]."""
    piece.add((x, y))
    couleur = plateau[x][y]  # Réxuperation de la couleur de la piece
    if (0 <= y - 1) and (plateau[x][y - 1] == couleur) and ((x, y - 1) not in piece):
        detecterPiece(plateau, x, y - 1, piece, couleur)  # Detecte l'élement au dessus de la zone de recherche
    if (len(plateau) > x + 1) and (plateau[x + 1][y] == couleur) and ((x + 1, y) not in piece):
        detecterPiece(plateau, x + 1, y, piece, couleur)  # Detecte l'élement à droite de la zone de recherche
    if (len(plateau[x]) > y + 1) and (plateau[x][y + 1] == couleur) and ((x, y + 1) not in piece):
        detecterPiece(plateau, x, y + 1, piece, couleur)  # Detecte l'élement en dessous de la zone de recherche
    if (0 <= x - 1) and (plateau[x - 1][y] == couleur) and ((x - 1, y) not in piece):
        detecterPiece(plateau, x - 1, y, piece, couleur)  # Detecte l'élement à gauche de la zone de recherche
    return piece


def mettreAJour(plateau, piece):
    """Modifie plateau de manière à ce que les trous liés à la suppression de la
    pièce donnée fassent chuter les autres blocs. Les coordonnées renseignées
    par piece renseignent des cases déjà à None dans plateau."""
    for ligne_piece, colonne_piece in sorted(piece):
        for compteur in range(colonne_piece, 0, -1):
            plateau[ligne_piece][compteur] = plateau[ligne_piece][compteur - 1]
        plateau[ligne_piece][0] = None


def eliminerColonnesVides(plateau):
    """Effectue les décalages nécessaires à la suppression des colonnes
    vides."""
    # Ajouté pour eviter un retour à droite des pièces à gauche du plateau
    compteur_plateau_plein = 0
    for compteur in range(len(plateau)):  
        if plateau[compteur][-1]:
            compteur_plateau_plein += 1
    if compteur_plateau_plein == len(plateau):
        return None
    x = 0
    for compteur in range(len(plateau)):  # Détection de la première colonne vide
        if not plateau[compteur][-1]:
            x = compteur
            break
    y = x
    while y < (len(plateau) - 1):  # Détection de la première colonne contenant des elements après la/les colonne(s) vide(s)
        if not plateau[y + 1][-1]:
            y += 1
        else:
            plateau[x], plateau[y + 1] = plateau[y + 1], plateau[x]  # Swap des colonnes vides et pleines de manière à décaller les colonnes vides à droite
            x +=1 ; y += 1


def partieFinie(plateau):
    """Renvoie un message de victoire si la partie est gagnée, c'est-à-dire
    si le plateau est vide ou un message de défaite si les seules pièces
    restantes sont de taille 1, et False sinon"""
    if not plateau[0][-1]:  # Si le premier element de la premiere colonne est vide, alors le joueur a gagné
        return "Vous avez gagné !"
    for colonne in range(len(plateau)):  # Parcours du tableau pour verifier si les pièces restantes ont toutes une longueur > 1
        for hauteur in range(len(plateau[0])):
            if plateau[colonne][hauteur]:
                if (len(detecterPiece(plateau, colonne, hauteur, set(), plateau[colonne][hauteur])) > 1) and (colonne != len(plateau)):
                    return False
    return "Vous avez perdu :("  # Sinon, le joueur a perdu la partie


# =============================================================================
# PARTIE A NE PAS MODIFIER ====================================================
# =============================================================================


class KlicketyGUI:
    """Interface pour le jeu Klickety."""
    def __init__(self):
        # initialisation des structures de données ----------------------------
        self.dim_plateau = (10,                 # nombre de colonnes du plateau
                            16)                 # nombre de lignes du plateau
        self.cote_case = 32          # la longueur du côté d'un bloc à dessiner
        self.largeur_plateau = self.cote_case * self.dim_plateau[0]
        self.hauteur_plateau = self.cote_case * self.dim_plateau[1]
        self.plateau = []
        self.compteur_de_coups = 0

        # initialisation des éléments graphiques ------------------------------
        self.window = Tk()                              # la fenêtre principale
        self.window.resizable(0, 0)           # empêcher les redimensionnements
        self.partie_haut = Frame(self.window, width=self.largeur_plateau,
                                              height=self.hauteur_plateau)
        self.partie_haut.pack(side=TOP)
        self.partie_bas = Frame(self.window)
        self.partie_bas.pack(side=BOTTOM)

        # le canevas affichant le plateau de jeu
        self.plateau_affiche = Canvas(self.partie_haut,
                                      width=self.largeur_plateau,
                                      height=self.hauteur_plateau)
        self.plateau_affiche.pack()
        self.plateau_affiche.bind('<ButtonPress-1>', self.clicPlateau)

        # le bouton "Réinitialiser"
        self.btn = Button(self.partie_bas, text='Réinitialiser',
                          command=self.reinitialiserJeu)
        self.btn.pack(fill=BOTH)

        # Zone d'affichage du nombre de coups
        self.nb_coups_affiche = Canvas(self.partie_bas,
                                       width=self.largeur_plateau, height=32)
        self.nb_coups_affiche.create_text(
            self.largeur_plateau // 2, self.cote_case // 2,
            text="Coups effectués: 0", fill="black"
        )
        self.nb_coups_affiche.pack(fill=BOTH)

        # affichage du nombre de blocs restants
        self.nb_blocs_affiche = Canvas(self.partie_bas,
                                       width=self.largeur_plateau, height=32)
        self.nb_blocs_affiche.pack(fill=BOTH)

        self.reinitialiserJeu()

        self.window.title('Klickety')
        self.window.mainloop()

    def rafraichirNombreBlocs(self, piece=None):
        """Rafraîchit l'affichage du nombre de blocs restants, sur base de la
        pièce que l'on vient de retirer."""
        self.nb_blocs_affiche.delete(ALL)
        if piece is None:  # appel initial, tous les blocs sont encore présents
            self.nb_blocs = self.dim_plateau[0] * self.dim_plateau[1]

        else:  # soustraire du nombre de blocs celui de la pièce retirée
            self.nb_blocs -= len(piece)

        self.nb_blocs_affiche.create_text(
            self.largeur_plateau // 2, self.cote_case // 2,
            text="Blocs restants: " + str(self.nb_blocs), fill="black"
        )

    def compteCoups(self, compteur_de_coups):
        """Compte le nombre de coups effectués durant cette partie."""
        self.nb_coups_affiche.delete(ALL)
        self.nb_coups_affiche.create_text(
            self.largeur_plateau // 2, self.cote_case // 2,
            text="Coups effectués: " + str(compteur_de_coups), fill="black"
        )

    def rafraichirPlateau(self):
        """Redessine le plateau de jeu à afficher."""
        # tracer les blocs
        self.plateau_affiche.delete(ALL)
        couleur_fond = "black"
        for i in range(self.dim_plateau[0]):                    # par défaut 10
            for j in range(self.dim_plateau[1]):                # par défaut 16
                case = self.plateau[i][j]
                if case is not None:  # afficher le pion
                    self.plateau_affiche.create_rectangle(
                        i * self.cote_case, j * self.cote_case,
                        (i + 1) * self.cote_case, (j + 1) * self.cote_case,
                        outline=case, fill=case
                    )
                else:
                    self.plateau_affiche.create_rectangle(
                        i * self.cote_case, j * self.cote_case,
                        (i + 1) * self.cote_case, (j + 1) * self.cote_case,
                        outline=couleur_fond, fill=couleur_fond
                    )

        # tracer le contour des pièces
        # 1) tracer les séparations entre deux pièces adjacentes de
        # couleurs différentes dans la même colonne
        for i in range(0, self.dim_plateau[0]):                 # par défaut 10
            colonne = self.plateau[i]
            for j in range(1, self.dim_plateau[1]):             # par défaut 16
                if colonne[j - 1] != colonne[j]:
                    self.plateau_affiche.create_rectangle(
                        (i) * self.cote_case, j * self.cote_case,
                        (i + 1) * self.cote_case, j * self.cote_case,
                        outline=couleur_fond, fill=couleur_fond, width=1
                    )

        # 2) tracer les séparations entre deux pièces adjacentes de
        # couleurs différentes dans la même ligne
        for i in range(1, self.dim_plateau[0]):                 # par défaut 10
            for j in range(0, self.dim_plateau[1]):             # par défaut 16
                if self.plateau[i - 1][j] != self.plateau[i][j]:
                    self.plateau_affiche.create_rectangle(
                        (i) * self.cote_case, j * self.cote_case,
                        (i) * self.cote_case, (j + 1) * self.cote_case,
                        outline=couleur_fond, fill=couleur_fond, width=1
                    )

    def clicPlateau(self, event):
        """Récupère les coordonnées de la case sélectionnée, et joue le coup
        correspondant s'il est permis."""
        # remarque: le canevas de tkinter interprète (i, j) géométriquement
        # (au lieu de (ligne, colonne)), d'où l'inversion de coordonnées dans
        # la ligne ci-dessous
        (i, j) = (event.x // self.cote_case, event.y // self.cote_case)

        if self.plateau[i][j] is not None:
            piece = set()
            detecterPiece(self.plateau, i, j, piece, self.plateau[i][j])
            #print (piece)

            if len(piece) > 1:  # si la pièce est valide, on la retire
                # retirer la piece en mettant ses cases à None
                for (p, q) in piece:
                    self.plateau[p][q] = None

                # faire descendre les blocs situés au-dessus de la pièce
                mettreAJour(self.plateau, piece)

                # tasser le restant du plateau en supprimant les colonnes vides
                eliminerColonnesVides(self.plateau)

                # rafraîchir le plateau pour répercuter les modifications
                self.rafraichirPlateau()

                self.rafraichirNombreBlocs(piece)
                self.compteur_de_coups += 1
                self.compteCoups(self.compteur_de_coups)
                messagevictoire = partieFinie(self.plateau)
                if messagevictoire:
                    self.plateau_affiche.create_text(
                        int(self.plateau_affiche.cget("width")) // 2,
                        self.cote_case // 2,
                        text=messagevictoire,
                        font=tkinter.font.Font(
                            family="Courier", size=12, weight=tkinter.font.BOLD
                        ),
                        fill="red"
                    )

    def reinitialiserJeu(self):
        """Réinitialise le plateau de jeu et les scores."""
        self.reinitialiserPlateau()
        self.rafraichirNombreBlocs()

        # réinitialiser le nombre de coups
        self.compteur_de_coups = 0
        self.nb_coups_affiche.delete(ALL)
        self.nb_coups_affiche.create_text(self.largeur_plateau // 2, self.cote_case // 2, text="Coups effectués: " + str(self.compteur_de_coups), fill="black")

    def reinitialiserPlateau(self):
        """Réinitialise le plateau de jeu."""
        # réinitialiser la matrice
        self.plateau = initialiserPlateau(*self.dim_plateau)

        # réinitialiser l'affichage
        self.plateau_affiche.delete(ALL)

        if self.plateau:
            self.rafraichirPlateau()

#### Debut du programme ####
if __name__ == "__main__":
    KlicketyGUI()