# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas, TP1

#### Importation des modules/fonctions/procedures ####
from random import randint

#### Définition des fonctions/procédures ####
def liste_aleatoire(taille, seuil):
    """
        Renvoie une liste de taille 'taille' composée
        d'entiers compris entre 0 et 'seuil'.
    """
    return [randint(0, seuil) for i in range(taille+1)]


def tri_bulle(lst):
    """
        1. On parcourt la partie non triée de la liste de la droite vers la gauche ;
        2. On compare chaque valeur avec son voisin de gauche ;
        3. Si nécessaire, on les échange ;
        4. Une fois arrivé à la partie déjà triée, on recommence.    
    """
    # on fait croître la portion triée
    for i in range(len(lst)-1):
        # on fait remonter la bulle
        # dans la portion non triée
        for j in range(len(lst)-1, i, -1):
            if lst[j-1] > lst[j]:
                # échange de voisins mal ordonnés
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


def tri_insertion(lst):
    """
        1. On parcourt la liste de la gauche vers la droite ;
        2. On insère chaque nouvel élément à la bonne place vis-à-vis des éléments
        précédents.
    """
    for i in range(1, len(lst)):
        # sauvegarder l'élément à déplacer
        e = lst[i]
        # décaler les éléments plus grands
        k = i
        while k > 0 and lst[k-1] > e:
            lst[k] = lst[k-1]
            k -= 1
        # insérer e en position k
        lst[k] = e
    return lst


def indice_min(lst, i):
    """
        Complète le tri par selection. Recherche et retourne
        la position de l'element minimal sur l'intervalle [i+1;len(liste)].
    """
    position = i
    minimum = lst[i]
    for p in range(i + 1, len(lst)):
        if lst[p] < minimum:
            minimum = lst[p]
            position = p
    return position


def tri_selection(lst):
    """
        1. On recherche la plus petite valeur dans la partie non triée de la liste ;
        2. On l’insère à la suite de la partie déjà triée du tableau ;
        3. On répète ces deux opérations autant de fois que nécessaire.
    """
    for i in range(len(lst)-1):
        p = indice_min(lst, i)
        lst[i], lst[p] = lst[p], lst[i]
    return lst


def tri_bulle_caillou(lst):
    """
        Effectue une passe du tri bulle puis une passe
        du tri caillou pour chaque élement à trier.
    """
    for i in range(len(lst)-1):
        for j in range(len(lst)-1, i, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
        for k in range(i, len(lst)-1):
            if lst[k+1] < lst[k]:
                lst[k+1], lst[k] = lst[k], lst[k+1]
    return lst


def tri_bulle_caillou_2(lst):
    """
        Version améliorée du tri bulle-caillou mémorisant la position
        la plus à gauche où s'est produit un échange de valeurs lors
        de la dernière passe de "bulle" et mémorisant la position la
        plus à droite où s'est produit un échange de valeurs lors de
        la dernière passe de "caillou".
    """
    position_gauche = 0
    position_droite = len(lst)-1
    for i in range(len(lst)-1):
        for j in range(position_droite, i, -1):
            if lst[j-1] > lst[j]:
                position_gauche = j-1
                lst[j-1], lst[j] = lst[j], lst[j-1]
        for k in range(position_gauche, len(lst)-1):
            if lst[k+1] < lst[k]:
                position_droite = k+1
                lst[k+1], lst[k] = lst[k], lst[k+1]
    return lst


def tri_generique(lst, plus_petit):
    """Effectue un tri à bulles avec la relation d'ordre partielle 'plus_petit'."""
    # on fait croître la portion triée
    for i in range(len(lst)-1):
        # on fait remonter la bulle
        # dans la portion non triée
        for j in range(len(lst)-1, i, -1):
            if plus_petit(lst[j], lst[j-1]):
                # échange de voisins mal ordonnés
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


def ordre_militaire(a, b):
    """
        Utilise la relation d'ordre militaire pour comparer a et b.
        retourne True si a est inferieur à b, False sinon (cette 
        relation d'ordre partielle sert d'exemple pour l'essai de
        la fonction 'tri_generique').
    """
    if len(str(a)) < len(str(b)):
        return True
    if len(str(a)) > len(str(b)):
        return False
    return a < b


def tri_divisibilite(lst):
    """Effectue un tri insertion avec la relation d'ordre partielle de divisibilité."""
    for i in range(1, len(lst)):
        # sauvegarder l'élément à déplacer
        e = lst[i]
        # empecher la division par 0
        if not e:
            continue
        # décaler les éléments plus grands
        k = i
        while k > 0:
            if not lst[k-1] % e:
                lst[k], lst[k-1] = lst[k-1], lst[k]
            k -= 1
    return lst


def tri_ensembles(lst):
    """Effectue un tri bulle avec la relation d'ordre partielle d'inclusion."""
    est_incluse = True
    # on fait croître la portion triée
    for i in range(len(lst)-1):
        # on fait remonter la bulle
        # dans la portion non triée
        for j in range(len(lst)-1, i, -1):
            #on parcourt la liste bulle pour savoir si elle est incluse dans la liste en dessous
            for k in range(len(lst[j-1])):
                # si elle n'est pas incluse, on switch la valeur du booléen 'est_incluse'
                if not lst[j-1][k] in lst[j]:
                    est_incluse = False
                    break
            if est_incluse:
                # échange de voisins mal ordonnés
                lst[j-1], lst[j] = lst[j], lst[j-1]
            else:
                est_incluse = True
    lst.reverse()
    return lst