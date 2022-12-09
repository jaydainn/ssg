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
        self.x = x
        self.y = y
        self.n = n

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
        if(self.x % 2 == 0 and self.y< 4 and self.y>0):
            self.est()
        elif(self.x % 2 == 1 and self.y< 4 and self.y>0):
            self.ouest()
        elif(self.y == 0 or self.y == 4):
            self.sud()

    def strategy2(self):
        if(self.x % 2 == 0 and self.y< 4 and self.y>0):
            self.ouest()
        elif(self.x % 2 == 1 and self.y< 4 and self.y>0):
            self.est()
        elif(self.y == 0 or self.y == 4):
            self.sud()

    def strategy3(self):
        if(self.x % 2 == 0 and self.y< 4 and self.y>0):
            self.ouest()
        elif(self.x % 2 == 1 and self.y< 4 and self.y>0):
            self.est()
        elif(self.y == 0 or self.y == 4):
            self.nord()

    # Se déplacer vers le haut
    def nord(self):
        if self.y - 1 >= 0:
            self.y -= 1

    # Se déplacer vers le bas
    def sud(self):
        if self.y + 1 < n:
            self.y += 1

    # Se déplacer vers la gauche    
    def ouest(self):
        if self.x - 1 >= 0:
            self.x -= 1

    # Se déplacer vers la droite
    def est(self):
        if self.x + 1 < n:
            self.x += 1



   

def afficher_grille(n, personnages):
    for x in range(n):
        ligne = ""
        for y in range(n):
            ligne += "| "
            for personne in personnages:
                if personne.x == x and personne.y == y:
                    ligne += personne.poste[0] + ","

        print(ligne + "|")

n = 5
personnages : List[Person] = []
positions_civils = []

num_civil = 3
for i in range(num_civil):
    x =  random.randint(0, n - 1)
    y =  random.randint(0, n - 1)
    positions_civils.append([x , y])
    civil = Person("Civil", x, y, n)
    personnages.append(civil)

num_police = 1
police1 = Person("Police", 0, 0, n)
personnages.append(police1)


positions_civils = np.array(positions_civils)

num_pick = 1
x_pick =  math.floor(positions_civils[: , 0].mean())
y_pick =  math.floor(positions_civils[: , 1].mean())
pick1 = Person("Pick", x_pick, y_pick, n)
personnages.append(pick1)

history = []

Q = np.zeros(2)

nb_tour = 15
for i in range(nb_tour):
    afficher_grille(n, personnages)

    for personne in personnages:
        personne.random_deplacement()

    print()