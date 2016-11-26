# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas
# TDA TP1
#
# Réponse à la question 2:
# Temps d'execution de 'fibonacci_generale(10)' = 0.0
# Temps d'execution de 'fibonacci_generale(20)' = 0.0
# Temps d'execution de 'fibonacci_generale(40)' = 0.0
# Temps d'execution de 'fibonacci_iterative(10)' = 0.0
# Temps d'execution de 'fibonacci_iterative(20)' = 0.0
# Temps d'execution de 'fibonacci_iterative(40)' = 0.0
# Temps d'execution de 'fibonacci_recursive(10)' = 0.00800016593933
# Temps d'execution de 'fibonacci_recursive(20)' = 0.00999999046326
# Temps d'execution de 'fibonacci_recursive(40)' = 159.855000019
#
# Réponse à la question 3:
# Fibonnaci(4) = 3
# Le temps d'appel de la fonction récursive est plus lent que le temps d'appel des
# autres fonctions car pour le calcul du terme de rang n, elle relance la fonction
# 'fibonacci_recursive' une nombre de fois de l"ordre de ((n - 1) + (n + 2)).
#
# Réponse à la question 5:
# La fonction 'fibonacci_liste_recursive' a été crée.
#
# Réponse à la question 6:
# Fibonnaci(80) = 23416728348467685 , Temps d'execution : 0.0160000324249
# Fibonnaci(90) = 2880067194370816120 , Temps d'execution : 0.018906726533
# Fibonnaci(95) = 31940434634990099905 , Temps d'execution : 0.022903452894
# Cette méthode est beaucoup plus efficace dans le cas du calcul d'un terme
# de la suite de Fibonacci avec un algorithme récursif.

def description_du_script():
    """
        TP3 - exercice 3 : Suite de Fibonacci
        Ce TP porte autour de la construction de la célèbre
        suite de Fibonacci de manière récursive. 
    """
    pass

#### Importation des modules / fonctions ####
from math import sqrt
from time import *

#### Définition des fonctions ####
def fibonacci_generale(nombre):
    """
        Reçoit un entier 'nombre' et retourne le terme 'nombre' de
        la suite de fibonacci calculé avec la formule generale.
    """
    return int(((((1 + sqrt(5)) / 2) ** nombre) - (((1 - sqrt(5)) / 2) ** nombre)) / sqrt(5))

def fibonacci_iterative(nombre):
    """
        Reçoit un entier 'nombre' et retourne le terme 'nombre' de
        la suite de fibonacci calculé de manière iterative.
    """
    terme_precedent, terme = 0, 1
    for compteur in range(nombre):
        terme_precedent, terme = terme, terme + terme_precedent
    return terme_precedent

def fibonacci_recursive(nombre):
    """
        Reçoit un entier 'nombre' et retourne le terme 'nombre' de
        la suite de fibonacci calculé de manière recursive.
    """
    if not nombre:
        return 0
    if nombre == 1:
        return 1
    return fibonacci_recursive(nombre - 1) + fibonacci_recursive(nombre - 2)

def fibonacci_couple_recursive(nombre):
    """
        Reçoit un entier 'nombre' et retourne un couple de termes 'nombre - 1' et
        'nombre' de la suite de fibonacci calculé de manière recursive.
    """
    if not nombre:
        return 0
    if nombre == 1:
        return 1
    return (fibonacci_recursive(nombre - 2) + fibonacci_recursive(nombre - 3) ,fibonacci_recursive(nombre - 1) + fibonacci_recursive(nombre - 2))

def fibonacci_couple_iterative(nombre):
    """
        Reçoit un entier 'nombre' et retourne un couple de termes 'nombre - 1' et
        'nombre' de la suite de fibonacci calculé de manière itérative.
    """
    terme_precedent, terme = 0, 1
    for compteur in range(nombre - 1):
        terme_precedent, terme = terme, terme + terme_precedent
    return terme_precedent, terme

def fibonacci_liste_recursive(nombre, liste = [1, 2]):
    """
        Reçoit un entier 'nombre' et retourne le terme 'nombre' de
        la suite de fibonacci calculé de manière recursive et l'insère dans
        une liste. Si le nombre a déjà été calculé préalablement, il est
        directement retourné depuis la liste.
    """
    if not nombre:
        return 0
    if nombre == 1:
        return 1
    if len(liste) > nombre:
            return liste[nombre]
    liste.append(fibonacci_liste_recursive(nombre - 1) + fibonacci_liste_recursive(nombre - 2))
    return fibonacci_liste_recursive(nombre - 1) + fibonacci_liste_recursive(nombre - 2)

#### Début du programme ####
print(description_du_script.__doc__)
nombre = input("Entrez le nombre à décomposer (['Quitter/quitter'] pour quitter):\n> ")
boucle_de_l_algorithme(nombre)