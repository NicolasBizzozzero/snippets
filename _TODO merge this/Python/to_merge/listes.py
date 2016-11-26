# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas, TP1
#
# La fonction 'retire_valeurs_recursif' n'a pas été completée.
#
# Ajouts et modifications :
# - Ajout d'une fonction 'retrait_en_tete'.
# - Ajout d'une fonction 'fusion'.


def nouvelle_liste():
    """Retourne une nouvelle liste vide."""
    return [] # L'utilité de cette fonction est... discutable.


def ajout_en_tete(liste, valeur):
    """Ajoute 'valeur' au debut de 'liste' et retourne la liste."""
    return [valeur, liste]


def ajout_en_fin(liste, valeur):
    """Ajoute 'valeur' de manière itérative à la fin de 'liste' et retourne la liste."""
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    while curseur:
        curseur = curseur[1] # On incrémente le curseur de une place jusqu'à atteindre la fin de la liste
    curseur.append(valeur) # On ajoute alors à la liste la valeur desirée.
    curseur.append(nouvelle_liste()) # Puis on replace un maillon vide en bout de liste.
    return liste


def retrait_en_tete(liste):
    """Retire la première valeur au debut de 'liste' et retourne la liste."""
    if liste: # Si la liste est non vide,
        return liste[1] # Alors la valeur existe, on peut donc la retirer.
    return liste


def affiche(liste):
    """Affiche de manière iterative le contenu de 'liste'."""
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    liste_a_afficher = nouvelle_liste() # Cette liste normale contiendra les valeurs que l'on souhaite afficher
    while curseur: # Tant que le curseur est non vide,
        liste_a_afficher.append(curseur[0]) # on ajoute la valeur qu'il contient dans la liste à afficher,
        curseur = curseur[1] # puis on l'incrémente d'un maillon. 
    print(liste_a_afficher)


def affiche_inverse(liste):
    """Affiche de manière iterative le contenu inversé de 'liste'."""
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    liste_a_afficher = nouvelle_liste() # Cette liste normale contiendra les valeurs que l'on souhaite afficher
    while curseur: # Tant que le curseur est non vide,
        liste_a_afficher.append(curseur[0]) # on ajoute la valeur qu'il contient dans la liste à afficher,
        curseur = curseur[1] # puis on l'incrémente d'un maillon.
    print('[', end='')
    for i in reversed(liste_a_afficher): # On inverse la liste à afficher,
        if i == liste_a_afficher[0]: # On affichera à la main le dernier élement de la liste,
            break # pour un affichage propre,
        print(i, end=', ') # puis on affiche la liste.
    print(liste_a_afficher[0], ']', sep='')


def recherche(liste, valeur):
    """Retourne 'True' si 'valeur' est dans 'liste', 'False' sinon."""
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    while curseur: # Tant qu'il n'est pas vide,
        if valeur in curseur: # si la valeur qu'on recherche est dedans,
            return True # alors on retourne True,
        curseur = curseur[1] # sinon, on incrèmente le curseur d'un maillon. 
    return False # Si toute la liste à été parcourue sans succés, on retourne False.


def taille(liste):
    """Retourne le nombre d'élements présents dans 'liste'."""
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    compteur = 0 # Le compteur désigne le nombre d'élements de la liste.
    while curseur: # Tant que le curseur n'est pas vide,
        compteur += 1 # on incrémente le compteur de 1,
        curseur = curseur[1] # et on incrémente le curseur de un maillon.
    return compteur


def occurence(liste, valeur):
    """Retourne le nombre de fois qu'apparait 'valeur' dans 'liste'."""
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    compteur = 0 # Le compteur désigne le nombre de fois qu'apparait 'valeur' dans la liste.
    while curseur: # Tant que le curseur n'est pas vide,
        if valeur in curseur: # si la valeur est dans le curseur,
            compteur += 1 # alors on incrémente le compteur de 1.
        curseur = curseur[1] # On incrémente le curseur de un maillon.
    return compteur


def fusion(liste1, liste2):
    """
        Fusionne les deux listes passées en argument en ajoutant liste2 dans liste1.
        CETTE FONCTION EFFACE 'liste2' ET MODIFIE 'liste1'.
    """
    while liste2: # Tant que 'liste2' n'est pas vide,
        ajout_en_fin(liste1, liste2[0]) # on ajoute l'élement en tête de liste2 dans la fin de liste1
        liste2 = retrait_en_tete(liste2) # puis on retire ce même element de liste2.
    return liste1 # On retourne la liste1 modifiée.


def retire_index(liste, index):
    """
        Retire la valeur à la position 'index' de 'liste' de manière itérative.
        Retourne la liste modifiée et la valeur retirée sous la forme : liste, valeur.
        Si aucun élement n'existe à la position 'index', la fonction retourne la valeur 'None'
    """
    if taille(liste) < index: # Si l'index donné est plus grand que la taille de la liste,
        return liste, None # on retourne None pour valeur de l'element retiré.
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    liste_modifiee = nouvelle_liste() # On créé la liste qui contiendra la partie gauche de la liste fusionnée.
    for i in range(index-1): # On parcourt 'liste' jusqu'à atteindre l'index donné.
        liste_modifiee = ajout_en_fin(liste_modifiee, curseur[0]) # On ajoute les élements de gauche à fusionner,
        curseur = curseur[1] # et on incremente le curseur d'un maillon.
    valeur_retiree = curseur[0]  # On sauvegarde la valeur à retirer,
    curseur = retrait_en_tete(curseur) # puis on l'enlève.
    liste = fusion(liste_modifiee, curseur) # Enfin, on fusionne les deux morceaux de liste,
    return liste, valeur_retiree # puis on retourne la liste fusionnée ainsi que la valeur retirée.


def retire_valeur(liste, valeur):
    """
        Retire la première occurence de 'valeur' dans 'liste' de manière itérative.
        Retourne la liste modifiée et 'True' si la valeur existe, 'False' sinon sous
        la forme : liste, True/false
    """    
    curseur = liste # Le curseur désigne l'emplacement du maillon sur lequel on travaille.
    liste_modifiee = nouvelle_liste() # On créé la liste qui contiendra la partie gauche de la liste fusionnée.
    while (valeur not in curseur) and (curseur): # On parcourt 'liste' jusqu'à atteindre l'index donné ou la fin de la liste.
        liste_modifiee = ajout_en_fin(liste_modifiee, curseur[0]) # On ajoute les élements de gauche à fusionner,
        curseur = curseur[1] # et on incremente le curseur d'un maillon.
    if curseur: # Si la fin de la liste n'a pas été atteinte,
        curseur = retrait_en_tete(curseur) # on retire valeur de la liste.
        liste = fusion(liste_modifiee, curseur) # et on fusionne les deux morceaux de liste,
        return liste, True # puis on retourne la liste fusionnée ainsi que True puisque la valeur a été retirée.
    return liste, False # Sinon, la fin de la liste a été atteinte et donc elle ne contient pas la valeur.


def retire_valeurs(liste, valeur):
    """
        Retire toutes les occurences de 'valeur' dans 'liste' de manière itérative.
        Retourne la liste modifiée et 'True' si la valeur existe, 'False' sinon sous
        la forme : liste, True/false
    """
    nouvelle_liste, existence_valeur = retire_valeur(liste, valeur) # On effectue une première passe de 'retire_valeur'
    if not existence_valeur: # Si cette première passe n'est pas concluante,
        return nouvelle_liste, False # on retourne False.
    while existence_valeur: # Sinon, on relance la fonction 'retire-valeur' autant de fois que necessaire.
        nouvelle_liste, existence_valeur = retire_valeur(nouvelle_liste, valeur)
    return nouvelle_liste, True # Puis enfin on renvoit True


def ajout_en_fin_recursif(liste, valeur):
    """Ajoute 'valeur' de manière récursive à la fin de 'liste' et retourne la liste."""
    if not liste: # Si la liste est vide, alors on est arrivé à la fin,
        liste.append(valeur) # on peut donc lui ajouter la valeur souhaitée.
        liste.append(nouvelle_liste())
        return liste
    return ajout_en_fin_recursif(liste[1], valeur) # Sinon, on relance la fonction avec le maillon suivant.


def affiche_recursif(liste):
    """Affiche de manière récursive le contenu de 'liste' sans les crochets ni les virgules."""
    if liste: # Si la liste contient encore des élements,
        print(liste[0], end=" ") # on les affiches, 
        affiche_recursif(liste[1]) # puis on, relance la fonction.
    else:
        print() # Sinon, on affiche le saut de ligne.


def affiche_inverse_recursif(liste):
    """Affiche de manière récursive le contenu inversé de 'liste' les crochets ni les virgules ni le saut de ligne de fin."""
    if liste: # Si la liste n'est pas vide,
        affiche_inverse_recursif(liste[1]) # on relance la fonction,
        print(liste[0], end=" ") # puis on affiche tous les élements au fur et à mesure.


def retire_index_recursif(liste, index):
    """
        Retire la valeur à la position 'index' de 'liste' de manière récursive.
        Retourne la liste modifiée et la valeur retirée sous la forme : liste, valeur.
        Si aucun élement n'existe à la position 'index', la fonction retourne la valeur 'None'
    """
    if not liste: # Si la liste est vide,
        return liste, None # on retourne None.
    if not index: # Si l'index est atteint,
        return liste[1], liste[0] # on ignore la valeur correspondante.
    liste[1], valeur = retire_index_recursif(liste[1], index-1) # On relance la fonction en collant ses deux morceaux.
    return liste, valeur


def retire_valeur_recursif(liste, valeur):
    """
        Retire la première occurence de 'valeur' dans 'liste' de manière récursive.
        Retourne la liste modifiée et 'True' si la valeur existe, 'False' sinon sous
        la forme : liste, True/False
    """
    if not liste: # Si la liste est vide,
        return liste, False # on retourne None.
    if valeur == liste[0]: # Si la valeur est dans la liste,
        return liste[1], True # on l'ignore.
    liste[1], val_booleenne = retire_valeur_recursif(liste[1], valeur) # On relance la fonction en collant ses deux morceaux.
    return liste, val_booleenne


def retire_valeurs_recursif(liste, valeur):
    """
        Retire toutes les occurences de 'valeur' dans 'liste' de manière récursive.
        Retourne la liste modifiée et 'True' si la valeur existe, 'False' sinon sous
        la forme : liste, True/False
    """
    pass