"""
Created on Thu Oct  5 09:09:43 2023
@author: pierre.vaulot
"""
#Main programme


from jeu import pendu
from jeu import meilleurScore



f=open("mots.txt","r")
dico=f.readlines()
best=0

pendu()
meilleurScore(best)
