# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas
# TDA TP1
#
# Réponse à la question 6 :
# Afin d'éviter les décompositions supplémentaires d'un même entier, une solution serait de placer dans 
# un dictionnaire ces entiers. Les clefs correspondraient aux entiers et leur valeur associée serait une chaine de caractères
# correspondant à leur décomposition. Il suffira alors d'un simple appel dans ce dictionnaire et de vérifier si la clef demandée
# est dedans pour gagner en efficacité !
#
# Ajouts :
# - Une fonction récursive permettant de supprimer les caractères superflus après la décomposition a été ajoutée.
# - Une simple boucle a été ajoutée pour que l'utilisateur puisse décomposer plusieurs entiers sans relancer le programme.

def description_du_script():
    """
        TP2 - exercice 3 : Décomposition en facteurs premiers
        On cherche à calculer une chaîne de caractères représentant
        la décomposition en facteurs premiers d'un entier donné. Par
        exemple, si l'entier à décomposer est 600, on doit obtenir
        la chaîne '2**3 * 3**1 * 5**2' puisque 600 = 2^3.3.5^2
        On demande à ce que toutes les fonctions écrites soient
        récursives (usage des boucles interdit).
    """
    pass

#### Définition des fonctions ####
def est_premier(n, div = 3):
    """
        Renvoie 'True' si n est premier, 'False' sinon.
        Cette fonction récursive effectue une boucle en incrémentant
        le diviseur 'div' (qui a 3 pour valeur par défaut) de 2 en 2
        et s'arrête dès qu'il dépasse 'n' ou qu'une des conditions soit remplie.
    """
    if n == 2: # On ajoute cette condition dans le cas où n = 2,
        return True # car 2 est premier.
    elif n < 2 or n % 2 == 0: # Si 'n' est négatif, nul, égal à 1 ou pair, 
        return False # alors 'n' n'est pas premier.
    elif div * div > n: # Si 'div^2' est supérieur à 'n',
        return True # alors 'n' est premier.
    elif n % div == 0: # Si 'n' est divisible par 'div',
        return False # alors 'n' n'est pas premier.
    else: # Si aucune des conditions n'est remplie
        return est_premier(n, div + 2) # Relancement de la fonction (comme une boucle) en incrémentant le diviseur 'div' de 2.

def premier_suivant(p):
    """ Renvoie le plus petit nombre premier strictement supérieur à p. """
    if est_premier(p + 1):
        return p + 1
    return premier_suivant(p + 1)

def exposant(n, p):
    """
        Renvoie l'exposant de p dans la décomposition en facteurs premiers de
        n et le nombre restant à décomposer.
    """
    if n % p:
        return (0, n)
    return (exposant(n / p, p)[0] + 1, exposant(n // p, p)[1])
    

def decomposition(n, p = 2):
    """
        Renvoie une chaîne décrivant la décomposition en facteurs premiers de n.
        Si l'argument p est donné, la recherche de facteur commence à
        cette valeur.
    """
    if n != 1:
        (x, y) = exposant(n, p)
        if x != 0:
            return ' ' + str(p) + '^' + str(x) + ' ' + '*' + decomposition(y, premier_suivant(p))[:-1]
        return decomposition(y, premier_suivant(p))
    return ' '

def decomposition_nettoyee(string):
    """
        Supprime les caractères superflus lors de l'utilisation de la
        fonction 'decomposition'.
    """
    if string[-1:] == '*':
        return string[:-1]
    else:
        return string
    return decomposition_nettoyee(string)

#### Début du programme ####
if __name__ == '__main__':
    print(description_du_script.__doc__)
    nombre = input("Entrez le nombre à décomposer (['Quitter/quitter'] pour quitter):\n> ")
    while (nombre != 'Quitter') and (nombre != 'quitter'):
        print(decomposition_nettoyee(decomposition(int(nombre))))
        nombre = input("Entrez le nombre à décomposer (['Quitter/quitter'] pour quitter):\n> ")