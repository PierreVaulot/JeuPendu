'''
Affichage
Fonctions responsable de la sélection et de l'affichage d'un mot 
'''

import random

def choixMot(Dico):
    Mot=random.choice(Dico).strip() #choix d'un mot aléatoire dans la liste
    return Mot
 

def affichageMot(Mot, LettresTrouvees):
    for i, l in enumerate(Mot): 
        if i == 0 or l in LettresTrouvees: #afficher la première lettre ainsi que les autres lettres trouvées
            print(l)
        else: #afficher _ pour les lettres non trouvees
            print("_")

def appelLettre():
    lettre = input("Donnez une lettre ") #demande à l'utilisateur d'entrer une lettre
    return lettre





