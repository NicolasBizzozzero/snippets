# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas, TP1
#
# Réponses:
# Exercice 1:
# 2) 39 est le plus petit entier n tel que le temps de calcul naif
# de la suite de fibonacci dépasse 20 secondes
# 4) Complexité en temps: O(2^n)
#    Complexité en espace: O(2^n)
#
# Exercice 2:
# 3) La pile d'execution est maximale pour n=999 (sur mon ordi
# personnel), le temps de calcul ne dépasse jamais 3 secondes.
# Complexité en temps: O(n)
# Complexité en espace: O(n)
# On constate un très grand gain de performance avec cet algorithme !
#
# Exercice 3:
# 3) Le temps de calcul dépasse 3 secondes pour l'entier n=~144980.
# Complexité en temps: O(n)
# Complexité en espace: O(1)
# 4) La fonction iterative est plus performante que la fonction recursive
# car elle n'est constituée que d'une simple boucle tandis que la recursive
# fait croitre la pile d'appel selon la taille de n.
#
# Exercice 4:
# 5) Ces fonctions sont ont toutes les trois la même vitesse pour des valeurs
# de n n'excedant pas 1400. Au delà, une erreur 'OverflowError: cannot convert
# float infinity to integer' survient.
# 6)
# fibo_phi_lent:
# Complexité en temps: O(1)
# Complexité en espace: O(1)
# fibo_phi_rapide:
# Complexité en temps: O(1)
# Complexité en espace: O(1)
# fibo_phi_natif:
# Complexité en temps: O(1)
# Complexité en espace: O(1)
# 7) fibo_phi_lent(100)=354224848179262980096
#  fibo_phi_rapide(100)=354224848179262062592
#   fibo_phi_natif(100)=354224848179263111168
# On constate que les valeurs donnés par les trois fonctions pour un même n sont
# différentes. Ceci s'explique par l'arrondi qui est fait grâce aux fonctions 'floor'.
# La vraie valeur du 100ème terme de la suite de fibonacci étant '354224848179261915075',
# il semblerait que ce soit la fonction 'fibo_phi_rapide' qui s'en rapproche le plus.
# 8) Il m'est impossible de déterminer une telle valeur car lorsque la valeur de n
# dépasse 1400, les fonctions produisent une erreur 'OverflowError: cannot convert
# float infinity to integer
#
# Exercice 5:
# 4) La fonction 'fibo_mat' est aussi efficace que 'fibo_iter' car elle permet de 
# calculer un tres grand terme de la suite de fibonacci sans produire d'erreur.
# Cependant, la fonction 'fibo_iter' reste plus rapide que la fonction 'fibo_mat' 
# 5) La fonction 'fibo_mat' n'est jamais plus rapide que la fonction 'fibo_iter' et la
# fonction 'fibo_rec'.
# 6) Complexité théorique : O(n^2)
# 7) La fonction 'fibo_mat' a de mauvaises performances à cause du fait qu'elle
# rappelle une autre fonction contenant une boucle dans laquelle elle rappelle
# elle même une autre fonction qui contient trois boucles imbriquées. Il est
# donc normal qu'elle mette beaucoup plus de temps à calculer le meme terme que
# les autres fonctions.


def description_du_script():
    """
        Cet énoncé a pour but de vous faire réfléchir aux complexités
        de ces différents modes de calcul de fn, et de tenter de les
        observer expérimentalement. Il reprend plusieurs éléments du
        TP 3, il est donc fortement recommandé de repartir du travail
        existant et de ne pas tout reprogrammer.
    """
    pass


#### Importation des modules/fonctions/procedures ####
from time import clock
from math import sqrt
from math import floor

#### Définition des fonctions/procédures ####
def fibo_naif(n):
    """
        Retourne la valeur d nème terme de la suite de fibonacci calculé de
        manière naive ainsi que le nombre d'additions effectuées dans cet
        ordre : terme n, nombre d'additions.
    """
    if not n :
        return 0, 0
    if n == 1:
        return 1, 0
    u, v = fibo_naif(n-1), fibo_naif(n-2)
    return u[0]+v[0], u[1]+v[1]+1


def fibo_rec(n, compteur=0) :
    """
        Retourne la valeur du n-1 et du nème terme de la suite de fibonacci
        calculés de manière récursive ainsi que le nombre d'additions effectuées
        dans cet ordre : terme n-1, terme n, nombre d'additions.
    """
    if not n: # Cas où n = 0
        return None, 0, 0
    if n == 1: # Cas d'arrêt
        return 0, 1, 0
    temp = fibo_rec(n-1)
    terme_suivant, terme_actuel = temp[0], temp[1]
    compteur = temp[2]+1
    return terme_actuel, terme_suivant+terme_actuel, compteur


def fibo_iter(n):
    """
        Retourne la valeur d nème terme de la suite de fibonacci calculé de
        manière itérative ainsi que le nombre d'additions effectuées dans cet
        ordre : terme n, nombre d'additions.
    """
    if not n :
        return 0, 0
    compteur = 0
    terme_suivant, terme_actuel = 0, 1
    for i in range(n-1) :
        terme_actuel, terme_suivant = terme_actuel + terme_suivant, terme_actuel
        compteur += 1
    return terme_actuel, compteur


def puissance_lente(a, n):
    if not n:
        return 1
    total = 1
    for compteur in range(n):
        total *= a
    return total


def puissance_rapide(a, n):
    if not n:
        return 1
    total = 1
    if not n%2:
        for compteur in range(floor(n/2)):
            total *= a*a
        return total
    for compteur in range(floor(n/2)):
        total *= a*a
    return total*a


def fibo_phi_lent(n):
    return floor((1/sqrt(5))*puissance_lente((1+sqrt(5))/2, n))


def fibo_phi_rapide(n):
    return floor((1/sqrt(5))*puissance_rapide((1+sqrt(5))/2, n))
    
    
def fibo_phi_natif(n):
    """Calcul du nème terme de la suite de fibonacci à l'aide de la formule générale."""
    return floor((((1+sqrt(5))/2)**n)/sqrt(5))


def produit_matrice(m1, m2):
    matrice_finale = []
    if len(m1[0]) != len(m2):
        return False
    for compteur1 in range(len(m1)):
        nouvelle_ligne = []
        for compteur2 in range(len(m2[0])):
            composant = 0
            for compteur3 in range(len(m1[0])):
                composant = composant + m1[compteur1][compteur3] * m2[compteur3][compteur2]
            nouvelle_ligne.append(composant)
        matrice_finale.append(nouvelle_ligne)
    return matrice_finale


def puissance_2x2(mat, n):
    if not n:
        return [[1, 0],
                [0, 1]]
    if n == 1:
        return mat
    mat_finale = mat
    for compteur in range(n-1):
        mat_finale = produit_matrice(mat_finale, mat)
    return mat_finale


def fibo_mat(n):
    return puissance_2x2([[1, 1], [1, 0]], n-1)[0][0]