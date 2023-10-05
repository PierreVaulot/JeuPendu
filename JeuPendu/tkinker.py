'''

Tkinter
Utilise l'affichage

'''


from PIL import Image, ImageTk 
from tkinter import *
from affichage import affichageMot
from affichage import choixMot
from jeu import pendu

f=open("mots.txt","r")
dico=f.readlines()
Mot=choixMot(dico) 
LettresTrouvees=[]
root = Tk() 

Mafenetre=Tk()
Mafenetre.title('Jeu du Pendu')

#Création du canvas
Largeur=480
Hauteur=320
Canevas=Canvas(Mafenetre,width=Largeur, height=Hauteur,bg='white')
#photo=PhotoImage(file='Bonhomme',vie,'.gif')
#item=Canevas.create_image(80,80,image=photo)


image = PhotoImage(file="Mr_Incredible_Phase_1.jpg") 
photo = ImageTk.PhotoImage(image) 
 
canvas = Tk.Canvas(root, width = Largeur, height = Hauteur, bg='white') 
canvas.create_image(0,0, anchor = Tk.NW, image=photo)
canvas.pack() 
root.mainloop()







#Création entry
Lettre=StringVar()
BoutonEntry=Entry(Mafenetre,textvariable=Lettre)

#Création du bouton proposer
BoutonProposer=Button(Mafenetre,text='Proposer',command = pendu)

#Création bouton fermer
BoutonQuitter=Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)

#Création label du mot recherché
x = affichageMot(Mot,LettresTrouvees)
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

