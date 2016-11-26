# -*- coding:utf-8 -*-
def description_du_script():
	"""
		Piti jeu
	"""
	pass

#### Modules ####
from upemtk import *
from time import *

#### Fonctions/procédures ####

#### Variables ####
intelligence = 0
connaissances = {
	"Sciences":{
		"Maths":{
			"Géométrie":0,
			"Probabilités":0,
			"Analyse":0,
			"Algèbre":0
		},
		"Physique":{
			"Astrophysique":0,
			"Mécanique":0,
			"Physique quantique":0,
			"Physique ondulatoire":0,
			"Physique des particules":0,
			"Physique statistique":0,
			"Physique de la matière condensée":0
		}
	},
	"Langues":{
		"Français":{
			"Conjugaison":0,
			"Grammaire":0,
			"Vocabulaire":0,
			"Prononciation":0
		},
		"Anglais":{
			"Conjugaison":0,
			"Grammaire":0,
			"Vocabulaire":0,
			"Prononciation":0
		},
		"Espagnol":{
			"Conjugaison":0,
			"Grammaire":0,
			"Vocabulaire":0,
			"Prononciation":0
		},
		"Chinois":{
			"Conjugaison":0,
			"Grammaire":0,
			"Vocabulaire":0,
			"Prononciation":0
		},
		"Japonais":{
			"Conjugaison":0,
			"Grammaire":0,
			"Vocabulaire":0,
			"Prononciation":0
		},
		"Arabe":{
			"Conjugaison":0,
			"Grammaire":0,
			"Vocabulaire":0,
			"Prononciation":0
		}
	}
} #sciences, langues, maitrises (peche, chasse etc.)
corps = {} #force, vision, endurance
inventaire = {}
francais = 0
anglais = 0
espagnol = 0
sortie = False

#### Début du programme ####
print(description_du_script.__doc__)
cree_fenetre(1000, 600)
attente_clic()
ferme_fenetre()
input()