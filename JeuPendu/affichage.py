#Affichage
#Fonctions responsable de la sélection et de l'affichage d'un mot 

import random

f=open("mot.txt","r")
dico=f.readlines()


def ChoixMot(Dico):
    Mot=random.choice(Dico) #choix random d'un mot dans la liste
    return Mot


def AffichageMot(Mot, LettresTrouvees):
    for i, l in enumerate(Mot): 
        if i==0 or l in LettresTrouvees: #afficher la première lettre ainsi que les autres lettres trouvées
            print(l)
        else: #afficher _ pour les lettres non trouvees
            print("_")

def AppelLettre():
    lettre=input("Donnez une lettre ") #demande à l'utilisateur d'entrer une lettre
    return lettre

def Gagne(Mot,LettresTrouvees):
    i=0
    for l in Mot:
        if l in LettresTrouvees: #ajouter 1 au compteur si la lettre du mot est dans la liste de lettres trouvees
            i+=1
    if i==len(Mot): #si le nombre de lettres trouvees est égal à la longueur du mot retourner True
        return True

def MeilleurScore(Best):
    score=Pendu()
    if score>best:
        Best=score
        print ("Vous avez le meilleur score")


best=0

def Pendu():
    i=8
    Mot=ChoixMot(dico) #Choix random du mot
    LettresTrouvees=[Mot[0]]#initialistation de la liste de lettres trouvees
    LettresFausses=[] #initialisation de la liste de lettres données mais fausses
    AffichageMot(Mot,LettresTrouvees) #Affichage du mot avec les lettres trouvées
    while i>0:#tant que le joueur n'a pas épuisé ses chances
        Lettre=AppelLettre() #demande à l'utilisateur de la lettre qu'il veut tester
        if Lettre in LettresTrouvees or Lettre in LettresFausses: #si la lettre a déja été donnée
            print ("Vous avez déjà donné cette lettre")
        elif Lettre in Mot: #si la lettre est dans le mot
            LettresTrouvees.append(Lettre)#on ajoute la lettre à la liste de lettres trouvees
            AffichageMot(Mot,LettresTrouvees)#afficher le mot avec la nouvelle lettre trouvee
            print ("Cette lettre est dans le mot. Il vous reste ",i," chances")
        else :
            i-=1 #enlever une chance à l'utilisateur
            LettresFausses.append(Lettre) #ajout de la lettre dans la liste de lettres fausses
            print ("Cette lettre n'est pas dans le mot. Il vous reste ",i," chances")
        if Gagne(Mot,LettresTrouvees)==True: #si l'utilisateur a donné toutes les bonnes lettres
            print ("Vous avez gagné")
            Score=i
            i=0
        else : #si il manque des bonnes lettres mais qu'il reste des chances
            print ("Essayez encore")
    if i==0 and Gagne(Mot,LettresTrouvees)!=True : #si il manque des bonnes lettres et que le nombre de chance est épuisé
        print ("Vous avez perdu")
    if i==0 :
        rejouer=input("Voulez-vous rejouer, tapez 1 pour oui, 2 pour non")
        if rejouer==1:
            return Score, Pendu() #relancer le jeu
        else :
            print ("Votre score est de",Score,"Au revoir") # arrêter le jeu
            return Score

Pendu()
MeilleurScore(best)




