'''

Jeu
Fonctions responsabes du jeu
'''




from affichage import choixMot
from affichage import affichageMot
from affichage import appelLettre

f=open("mots.txt","r")
dico=f.readlines()

def pendu():

    vie=8
    Mot=choixMot(dico) 
    LettresTrouvees=[Mot[0]]
    LettresFausses=[]
    affichageMot(Mot,LettresTrouvees)
    
    while vie>0:
        Lettre=appelLettre() #demande à l'utilisateur de la lettre qu'il veut tester
       
        if Lettre in LettresTrouvees or Lettre in LettresFausses: #si la lettre a déja été donnée
            print ("Vous avez déjà donné cette lettre")
        elif Lettre in Mot: 
            LettresTrouvees.append(Lettre)
            affichageMot(Mot,LettresTrouvees)#afficher le mot avec la nouvelle lettre trouvee
        else :
            vie-=1 
            LettresFausses.append(Lettre) #ajout de la lettre dans la liste de lettres fausses
            print ("Cette lettre n'est pas dans le mot. Il vous reste ",vie," chances")
        
        if gagne(Mot,LettresTrouvees): #si l'utilisateur a donné toutes les bonnes lettres
            print ("Vous avez gagné")
            Score=vie
            vie=0
        else : #si il manque des bonnes lettres mais qu'il reste des chances
            print ("Essayez encore")

    if vie == 0 and not gagne(Mot,LettresTrouvees) : #si il manque des bonnes lettres et que le nombre de chance est épuisé
        print ("Vous avez perdu")

    if vie==0 :
        rejouer = int(input("Voulez-vous rejouer, tapez 1 pour oui, 2 pour non :"))
        
        if rejouer==1:
            return Score, pendu() #relancer le jeu
        else :
            print ("Votre score est de",Score,"Au revoir") # arrêter le jeu
            return Score
        
def gagne(Mot,LettresTrouvees):
    gagner=False
    i=0
    for l in Mot:
        if l in LettresTrouvees: #ajouter 1 au compteur si la lettre du mot est dans la liste de lettres trouvees
            i+=1
    if i==len(Mot): #si le nombre de lettres trouvees est égal à la longueur du mot retourne gagne
        gagner=True
    return gagner 
    

def meilleurScore(Best):
    score = pendu()
    if score>best:
        best=score
        print ("Vous avez le meilleur score")

