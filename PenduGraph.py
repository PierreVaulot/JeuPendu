# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:38:05 2018

@author: noemie.rolland
"""
from Tkinter import *
import random

Dico = [] #initialistation de la liste de mots
Dico.append("pigeon")
Dico.append("pitch")
Dico.append("alpaga")
Dico.append("crocodile")
Dico.append("lunettes")

def ChoixMot(Dico):
    Mot=random.choice(Dico) #choix random d'un mot dans la liste
    return Mot
    
def AffichageMot(Mot,LettresTrouvees):
    x = ""
    for i, L in enumerate(Mot): 
        if i==0 or L in LettresTrouvees: #afficher la première lettre ainsi que les autres lettres trouvées
            x+=L
        else: #afficher _ pour les lettres non trouvees
            x+=" _"
    return x

def AppelLettre():
    lettre=raw_input("Donnez une lettre ") #demande à l'utilisateur d'entrer une lettre
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
    if score>Best:
        Best=score
        print "Vous avez le meilleur score"

Best=0

def Verif(LettresTrouvees,LettresFausses,Mot,l,vie):
    if l in LettresTrouvees or l in LettresFausses: #si la lettre a déja été donnée
        print ("Vous avez déjà donné cette lettre")
    elif l in Mot: #si la lettre est dans le mot
        LettresTrouvees.append(l)#on ajoute la lettre à la liste de lettres trouvees
        AffichageMot(Mot,LettresTrouvees)#afficher le mot avec la nouvelle lettre trouvee
        print ("Cette lettre est dans le mot. Il vous reste ",vie," chances")
    else :
        vie-=1 #enlever une chance à l'utilisateur
        LettresFausses.append(l) #ajout de la lettre dans la liste de lettres fausses
        print ("Cette lettre n'est pas dans le mot. Il vous reste ",vie," chances")
    return LettresTrouvees,LettresFausses,vie

def Pendu():
    global vie,Mot,LettresTrouvees,LettresFausses 
    AffichageMot(Mot,LettresTrouvees) #Affichage du mot avec les lettres trouvées
    while vie>0:#tant que le joueur n'a pas épuisé ses chances       
        l=Lettre.get() #demande à l'utilisateur de la lettre qu'il veut tester
        print l
        Verif(LettresTrouvees,LettresFausses,Mot,l,vie)
        if Gagne(Mot,LettresTrouvees)==True: #si l'utilisateur a donné toutes les bonnes lettres
            print "Vous avez gagné"
            Score=vie
            vie=0
        else : #si il manque des bonnes lettres mais qu'il reste des chances
            print "Essayez encore"
    if vie==0 and Gagne(Mot,LettresTrouvees)!=True : #si il manque des bonnes lettres et que le nombre de chance est épuisé
        print "Vous avez perdu"
    if vie==0 :
        rejouer=input("Voulez-vous rejouer, tapez 1 pour oui, 2 pour non")
        if rejouer==1:
            return Score, Pendu() #relancer le jeu
        else :
            print "Votre score est de",Score,"Au revoir" # arrêter le jeu
            return Score

#Variables pour que ça marche
vie=8
Mot=ChoixMot(Dico) #Choix random du mot
LettresTrouvees=[Mot[0]]#initialistation de la liste de lettres trouvees
LettresFausses=[]

#Création de la fenêtre principale
Mafenetre=Tk()
Mafenetre.title('jeu')

#Création du Canvas
Largeur=480
Hauteur=320
Canevas=Canvas(Mafenetre,width=Largeur, height=Hauteur,bg='white')
#photo=PhotoImage(file='Bonhomme',vie,'.gif')
#item=Canevas.create_image(80,80,image=photo)

#Création entry
Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)

#Création du bouton proposer
BoutonProposer=Button(Mafenetre,text='Proposer',command = Pendu)

#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Création label du mot recherché
x = AffichageMot(Mot,LettresTrouvees)
LabelMotRech=Label(Mafenetre,text=x,fg='black',bg='white')

#Création label nb de coups restants
vie=IntVar()
vie.set(str(vie))
LabelCoup=Label(Mafenetre,textvariable=vie,fg='black',bg='white')

#Mise en page
LabelCoup.grid(row=1,sticky=NE)
LabelMotRech.grid(row=2)
BoutonEntry.grid(row=3)
BoutonProposer.grid(row=4)
BoutonQuitter.grid(row=5)
Canevas.grid(row=1,column=2,rowspan=5)
 
Mafenetre.mainloop()