#Ce programme propose deux jeux : 
#Le jeu 1 "Deviner le nombre mystere" genere un nombre aleatoirement entre 1 et 1000 et
#Demande a l utilisateur de le deviner. A chacuns de ses essais, il sera indique si le
#nombre a deviner est plus grand ou plus petit que son essai.
#Le jeu 2 "Faites deviner le nombre mystere a l'ordinateur !" demande a l utilisateur un nombre
#puis il doit, a l aide d indicateurs tels que plus, mois ou gagne, aider l ordinateur
#A deviner ce nombre

#Importation du module random
from random import randint

#Choix du jeu
print("Entrez '1' pour jouer a 'Deviner le nombre mystere !' ")
choixjeu = int(input("Entrez '2' pour jouer a 'Faites deviner le nombre mystere a l'ordinateur ! "))

#Message d erreur de mauvais choix du jeu
while choixjeu != 1 and choixjeu != 2:
    print("Vous n\'avez le choix qu\'entre deux jeux !")
    choixjeu = int(input("Entrez '1' pour jouer a 'Deviner le nombre mystere !',entrez '2' pour jouer a 'Faites deviner le nombre mystere a l'ordinateur ! "))
    
    print("Il n\'y a que deux possibilites de reponses.")
    choixjeu = int(input("Entrez '2' pour jouer a 'Faites deviner le nombre mystere a l'ordinateur ! "))

#Debut du jeu 1
if choixjeu == 1:
    print("Trouvez le nombre mystere en 10 essais maximum !")
    
    #Initialisation des variables
    x = randint(1,1000)
    y = int(input("Faites un essai, le nombre est compris entre 1 et 1000  : "))
    i = 0
    
    #Message d erreur de mauvais choix de nombre mystere
    while y < 1:
        print("Le nombre mystere est compris entre 1 et 1000 !")
        y = int(input("Refaites un essai : "))
        
    #Lancement de la boucle du jeu
    while x != y and i != 9:
        if y > x:
            y = int(input("Entrez un nombre plus petit que celui ci "))
            i = i + 1
        if y < x:
            y = int(input("Entrez un nombre plus grand que celui ci "))
            i = i + 1
        if y < 1:
            print("Le nombre mystere est compris entre 1 et 1000 !")
            y = int(input("Refaites un essai : "))
            
    #Phrase de victoire
    if y == x:
        print("C\'est la victoire victorieuse !!!")
        if i == 1:
            print("Vous avez gagne en 1 essai ! :O ")
        else:
            print("Vous avez gagne en",i,"essais")
            
    #Phrase de defaite
    if i == 9:
        print("Vous avez perdu :(")
        
#Debut du jeu 2
if choixjeu == 2:
    
    #Choix du mode de difficulte. En mode normal les nombres generes par l ordinateur sont aleatoires. Bien que
    #l intervalle de l aleatoire retrecisse a chaque essai, la probabilite que l ordinateur touve le nombre est
    #bien plus faible que dans le mode difficile. En mode difficile, chaque nombre genere par l ordinateur
    #resulte de la division par 2 de la difference du minimum et du maximum. Cette methode est la maniere
    #la plus optimisee pour trouver le nombre mystere.
    choixmode = input("Voulez-vous jouer en 'normal' ou en 'difficile' ? ")
    
    #Message d erreur de mauvais choix de jeu
    while choixmode != "normal" and choixmode != "difficile":
        print("Vous n\'avez le choix qu\'entre deux modes de jeux !")
        choixmode = input("Voulez-vous jouer en 'normal' ou en 'difficile' ? ")
    
    #Debut du mode normal
    if choixmode == "normal":
        #Initialisation des variables
        i = 1
        min = 1
        max = 1000
        y = randint(min,max)
    
        #Choix du nombre mystere
        x = int(input("Entrez le nombre mystere : "))
        
        #Message d erreur pour nombre mystere negatif
        while x <= 0:
            print("Le nombre mystere doit etre au moins egal a 1")
            x = int(input("Entrez a nouveau le nombre mystere : "))
        
        #Initialisation du jeu
        print("L\'ordinateur essaye le nombre",y)
        reponse = input("Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal (ne trichez pas !) : ")
        
        #Lancement de la boucle du jeu
        while reponse != "gagne":
            if reponse == "moins":
                max = y - 1
                y = randint(min,max)
                i = i + 1
                print("L\'ordinateur essaye le nombre",y)
                reponse = input("Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal (ne trichez pas !) : ")
            if reponse == "plus":
                min = y + 1
                y = randint(min,max)
                i = i + 1
                print("L\'ordinateur essaye le nombre",y)
                reponse = input("Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal (ne trichez pas !) : ")
            if reponse != "moins" and reponse != "plus" and reponse != "gagne":
                print("La chaine de caractere entree est incorrecte. Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal.")
                reponse = input("L\'ordinateur essaye le nombre "+str(y)+" ")
        
        #Message de victoire
        if reponse == "gagne":
            if i == 1:
                print("L\'ordinateur a gagne en un essai ! :O ")
            else:
                print("L\'ordinateur a gagne en",i,"essais !")
                
    #Debut du mode difficile
    if choixmode == "difficile":
        #Initialisation des variables
        i = 1
        min = 1
        max = 1000
        y = 500
        
        #Choix du nombre mystere
        x = int(input("Entrez le nombre mystere : "))
        
        #Message d erreur pour nombre mystere negatif
        while x <= 0:
            print("Le nombre mystere doit etre au moins egal a 1")
            x = int(input("Entrez a nouveau le nombre mystere : "))
            
        #Initialisation du jeu
        print("L\'ordinateur essaye le nombre",y)
        reponse = input("Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal (ne trichez pas !) : ")
        
        #Lancement de la boucle du jeu
        while reponse != "gagne":
            if reponse == "moins":
                max = y
                y = int(y - (max-min)/2)
                i = i + 1
                print("L\'ordinateur essaye le nombre",y)
                reponse = input("Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal (ne trichez pas !) : ")
            if reponse == "plus":
                min = y
                y = int(y + (max-min)/2)
                i = i + 1
                print("L\'ordinateur essaye le nombre",y)
                reponse = input("Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal (ne trichez pas !) : ")
            if reponse != "moins" and reponse != "plus" and reponse != "gagne":
                print("La chaine de caractere entree est incorrecte. Entrez 'moins' si le nombre mystere est plus petit que le nombre propose, 'plus' si il est plus grand ou 'gagne' si il est egal.")
                reponse = input("L\'ordinateur essaye le nombre "+str(y)+" ")
        
        #Message de victoire
        if reponse == "gagne":
            if i == 1:
                print("L\'ordinateur a gagne en un essai ! :O ")
            else:
                print("L\'ordinateur a gagne en",i,"essais !")