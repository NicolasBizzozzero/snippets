from upemtk import *

coordonnes_clic = (0, 0)

cree_fenetre(1000, 600)

# Menu d'accueil
rectangle(0, 0, 1000, 600, couleur = 'black', remplissage = 'black')
texte(500, 150, "TRADES GAME", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 30)
rectangle(350, 330, 650, 445, couleur = '#708090', remplissage = '#868686')
texte(500, 387, "Let's play !", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
rectangle(350, 460, 650, 575, couleur = '#708090', remplissage = '#868686')
texte(500, 517, "Exit", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
#image(x, y, "img/logo-labyrinthe.gif", ancrage='center'), à implementer plus tard

coordonnees_du_clic = attente_clic()

while (coordonnees_du_clic[0] < 350) or (coordonnees_du_clic[0] > 650) or (coordonnees_du_clic[1] < 330) or (coordonnees_du_clic[1] > 445 and coordonnees_du_clic[1] < 460) or (coordonnees_du_clic[1] > 575):
	coordonnees_du_clic = attente_clic()
if coordonnees_du_clic[0] >= 350 and coordonnees_du_clic[0] <= 650 and coordonnees_du_clic[1] >= 330 and coordonnees_du_clic[1] <= 445:
	efface_tout()
	rectangle(0, 0, 1000, 600, couleur = 'black', remplissage = 'black')
	coordonnees_du_clic = attente_clic()
	


elif coordonnees_du_clic[0] >= 350 and coordonnees_du_clic[0] <= 650 and coordonnees_du_clic[1] >= 460 and coordonnees_du_clic[1] <= 575:
	ferme_fenetre()