# -*- coding: utf-8 -*-
# BIZZOZZERO Nicolas

from random import randint, shuffle
from time import time

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


def tri_selection(lst):
    """
        1. On recherche la plus petite valeur dans la partie non triée de la liste ;
        2. On l’insère à la suite de la partie déjà triée du tableau ;
        3. On répète ces deux opérations autant de fois que nécessaire.
    """

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


def tri_fusion(lst, debut=0, fin=None):
    """
        1. Si la liste contient moins de deux éléments, on la trie directement
        2. Sinon :
        (a) On divise la liste en deux
        (b) On relance l’algorithme pour chaque partie de la liste
        (c) On fusionne les deux parties triées de la liste
    """

    def fusionner(lst, g, d, debut):
        """
            Fonction complementaire à la fonction 'tri_fusion'.
            Concatène en triant les morceaux de la liste 'lst'.
        """
        # On vide les listes g et d jusqu'à ce que l'une d'elles soit vide
        while (len(g)) and (len(d)):
            if g[0] < d[0]:
                lst[debut] = g.pop(0)
            else:
                lst[debut] = d.pop(0)
            debut += 1
        # On trie la liste non-vide qu'il reste dans lst
        while len(g):
            lst[debut] = g.pop(0)
            debut += 1
        while len(d) :
            lst[debut] = d.pop(0)
            debut += 1
        return lst

    # Attribution de la valeur 'fin', si le paramètre n'est pas specifié
    if fin is None:
        fin = len(lst)-1
    # Condition d'arret de la récursion
    if fin - debut + 1 < 2:
        return lst
    # Partie (a)
    moitie_de_liste = (debut + fin) // 2
    # Partie (b)
    tri_fusion(lst, debut, moitie_de_liste)
    tri_fusion(lst, moitie_de_liste+1, fin)
    # Partie (c)
    g = lst[debut:moitie_de_liste+1]
    d = lst[moitie_de_liste+1:fin+1]
    lst = fusionner(lst, g, d, debut)
    return lst


def tri_rapide(lst, debut=0, fin=None):
    """
        1. Si la liste a au plus 1 élément, elle est déjà triée
        2. Sinon :
        (a) On choisit arbitrairement un pivot
        (b) On met toutes les valeurs plus petites que le pivot à sa gauche
        (c) Et à sa droite toutes les valeurs plus grandes
        (d) On divise la liste en deux parties au niveau du pivot
        (e) On relance l’algorithme sur chacunes des parties
    """

    def partition(lst, debut, fin, pos_pivot):
        """Fonction complementaire à la fonction 'tri_rapide'."""
        lst[debut], lst[pos_pivot] = lst[pos_pivot], lst[debut]
        curseur1, curseur2 = debut + 1, fin
        while curseur1 <= curseur2:
            while curseur1 <= curseur2 and lst[curseur1] <= lst[debut]:
                curseur1 += 1
            while lst[curseur2] > lst[debut]:
                curseur2 -= 1
            if curseur1 < curseur2: # si nécessaire, procéder à l'échange
                lst[curseur1], lst[curseur2] = lst[curseur2], lst[curseur1]
                curseur1 += 1
                curseur2 -= 1
        lst[debut], lst[curseur2] = lst[curseur2], lst[debut]
        return curseur2 # la position finale du pivot servira plus tard

    if fin is None:
        fin = len(lst)-1
    if debut < fin:
        # choix d'un pivot aléatoire
        pos_pivot = randint(debut, fin)
        # partition par rapport au pivot
        pos_finale_pivot = partition(lst, debut, fin, pos_pivot)
        # tri de la zone à gauche du pivot
        tri_rapide(lst, debut, pos_finale_pivot - 1)
        # tri de la zone à droite du pivot
        tri_rapide(lst, pos_finale_pivot + 1, fin)
    return lst


def bogosort(lst):
    """ 
        Tant que 'lst' n'est pas triée, on mélange tous ses elements.
        ~5 secondes pour une liste de 10 elements
        ~2 minutes pour une liste de 11 elements
        ~50 minutes pour une liste de 12 elements
    """
    while not isSorted(lst):
        shuffle(lst)
    return lst


def bogobogosort(lst):
    """ 
        Tant que les 2 premiers elements de 'lst' ne sont pas triés, on les melange.
        Puis, tant que les 3 premiers elements de 'lst' ne sont pas triés, ont les melange.
        Puis on continue ainsi de suite jusqu'à ce que les n elements de 'lst' soient triés.
    """
    if len(lst) < 2:
        return lst
    cursor_position = 2
    while not isSorted(lst):
        bogosort(lst[:cursor_position])
        cursor_position += 1
        if not isSorted(lst[:cursor_position]):
            shuffle(lst)
            cursor_position = 2
    return lst


def sleep_sort(array: int) -> None:
    """ Sort the array in-place using the sleep sort algorithm.
        The sleep sort algorithm create a thread for each element of the array,
        and make them sleep for an amount of time corresponding to the element
        value. After this time, the thread append themself to the list.
    """
    from threading import Timer

    # Construct all threads
    threads = []
    for value in array:
        threads.append(Timer(value, lambda array,
                             value: array.append(value), (array, value)))

    # Clean the array
    del array[:]

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all of them to finish
    for thread in threads:
        thread.join()


# source:
#    http://stackoverflow.com/questions/4836710/
#    does-python-have-a-built-in-function-for-string-natural-sort/4836734#4836734
def natural_sort(l):
    """Returns sorted strings using natural sort
    """
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)



def isSorted(lst):
    prev = None
    for x in lst:
        if (prev) and (prev > x):
            return False
        prev = x
    return True

if __name__ == "__main__":
    liste = [4, 8, 15, 16, 23, 42]
    shuffle(liste)

    print("Liste originale     :", liste)
    print("Tri bulle           :", tri_bulle(liste))
    print("Tri par insertion   :", tri_insertion(liste))
    print("Tri par selection   :", tri_selection(liste))
    print("Tri bulle-caillou   :", tri_bulle_caillou(liste))
    print("Tri bulle-caillou 2 :", tri_bulle_caillou_2(liste))
    print("Tri fusion          :", tri_fusion(liste))
    print("Tri rapide          :", tri_rapide(liste))
    print("Tri stupide         :", bogosort(liste))
    print("BogoBogoSort        :", bogobogosort(liste))
