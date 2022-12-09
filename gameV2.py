# ******************************************************
# @author: Jeremy Dain, Ethan Postic et Lemuel Falret
# ******************************************************

import random
from typing import List
import numpy as np 
import json
from IPython.display import clear_output
from collections import deque
#import progressbar
import math

# from tensorflow.keras import Model, Sequential
# from tensorflow.keras.layers import Dense, Embedding, Reshape
# from tensorflow.keras.optimizers import Adam

class Person:
    def __init__(self, poste, x, y, n):
        self.poste = poste
        self.x = x #ligne
        self.y = y #colonne
        self.n = n
        self.etat = True
        self.score = 0

    def random_deplacement(self):
        direction = random.choice(["nord", "sud", "ouest", "est"])

        if direction == "nord":
            self.nord()
        elif direction == "sud":
            self.sud()
        elif direction == "ouest":
            self.ouest()
        elif direction == "est":
            self.est()

    def strategy1(self):       
        if(self.x % 2 == 0 and self.y < n-1):
            self.est()
        elif(self.x % 2 == 1 and self.y > 0):
            self.ouest()
        elif(self.x % 2 == 0 and self.y == n-1 or self.x % 2 == 1 and self.y == 0):
            self.sud()

    def strategy2(self):
        if(self.x % 2 == 0 and self.y > 0):
            self.ouest()
        elif(self.x % 2 == 1 and self.y < n-1):
            self.est()
        elif(self.x % 2 == 0 and self.y == 0 or self.x % 2 == 1 and self.y == n-1):
            self.sud()

    def strategy3(self):
        if(self.x % 2 == 0 and self.y < n-1):
            self.est()
        elif(self.x % 2 == 1 and self.y > 0):
            self.ouest()
        elif(self.x % 2 == 0 and self.y == n-1 or self.x % 2 == 1 and self.y == 0):
            self.nord()

    # Se déplacer vers le haut
    def nord(self):
        if self.etat == True and self.x - 1 >= 0:
            self.x -= 1

    # Se déplacer vers le bas
    def sud(self):
        if self.etat == True and self.x + 1 < n:
            self.x += 1

    # Se déplacer vers la gauche
    def ouest(self):
        if self.etat == True and self.y - 1 >= 0:
            self.y -= 1   

    # Se déplacer vers la droite
    def est(self):
        if self.etat == True and self.y + 1 < n:
            self.y += 1


def afficher_grille(n, personnages):
    for x in range(n):
        lignes = []
        for y in range(n):
            ligne = []
            for personne in personnages:
                if personne.etat == True and personne.x == x and personne.y == y:
                    ligne.append(personne.poste[:2])
            lignes.append(ligne)

        print(lignes)

def same_position(perso1, perso2):
    return perso1.x == perso2.x and perso1.y == perso2.y

def is_policier(perso):
    return perso.poste == POLICIER

def is_pick(perso):
    return perso.poste == PICK

CIVIL = "Civil"
POLICIER = "Policier"
PICK = "Pick"
n = 5
personnages : List[Person] = []

#Initialisation des policiers
num_police = 1
strategie = random.choice([1, 2, 3])
for i in range(num_police):
    print(strategie)
    x = 0
    y = 0
    if (strategie == 2):
        x = 0
        y = n-1
    elif (strategie == 3):
        x = n-1
        y = 0
    
    police = Person(POLICIER, x, y, n)
    personnages.append(police)

#Initialisation des civils
positions_civils = []
num_civil = 3
for i in range(num_civil):
    x =  random.randint(0, n - 1)
    y =  random.randint(0, n - 1)
    positions_civils.append([x , y])
    civil = Person(CIVIL, x, y, n)
    personnages.append(civil)
positions_civils = np.array(positions_civils)

#Initialisation des pickpockets
num_pick = 1
for i in range(num_pick):
    x =  math.floor(positions_civils[: , 0].mean())
    y =  math.floor(positions_civils[: , 1].mean())
    pick = Person(PICK, x, y, n)
    personnages.append(pick)

Q = np.zeros(2)
history = []
nb_tour = 25
for i in range(nb_tour):
    afficher_grille(n, personnages)

    str_list = []
    for personne in personnages:
        str_perso = personne.poste, personne.x, personne.y, personne.etat
        str_list.append(str_perso)
    history.append(str_list)

    for perso1 in personnages:
        for perso2 in personnages:
            #Le cas où les trois postes sont sur la même case, le pickpocket se fera attrapé avant qu'il ai le temps de voler 
            if perso1.etat == True and perso2.etat == True and perso1 != perso2 and same_position(perso1, perso2):
                #POLICIER / PICK
                if perso1.poste == POLICIER and perso2.poste == PICK:
                    perso1.score += 1
                    perso2.etat = False
                #PICK / POLICIER
                if perso1.poste == PICK and perso2.poste == POLICIER:
                    perso2.score += 1
                    perso1.etat = False

                #CIVIL / PICK
                if perso1.poste == CIVIL and perso2.poste == PICK:
                    perso2.score += 1
                    perso1.etat = False
                #PICK / CIVIL
                if perso1.poste == PICK and perso2.poste == CIVIL:
                    perso1.score += 1
                    perso2.etat = False

    for personne in personnages:
        if not is_policier(personne):
            personne.random_deplacement()
        elif strategie == 1:
            personne.strategy1()
        elif strategie == 2:
            personne.strategy2()
        elif strategie == 3:
            personne.strategy3()

    print()

score_policier = 0
score_pick = 0
for personne in personnages:
    if is_policier(personne) or is_pick(personne):
        print(personne.poste, personne.score)

    if is_policier(personne):
        score_policier += personne.score
    if is_pick(personne):
        score_pick += personne.score

print("Score des Policiers :", score_policier)
print("Score des Pick :", score_pick)
print()
print(history)