# ******************************************************
# @author: Jeremy Dain, Ethan Postic et Lemuel Falret
# ******************************************************

import itertools
import random
from typing import List
import numpy as np 
import json
from IPython.display import clear_output
from collections import deque
import progressbar
import math
from collections import defaultdict
from tqdm import tqdm
from time import sleep

# from tensorflow.keras import Model, Sequential
# from tensorflow.keras.layers import Dense, Embedding, Reshape
# from tensorflow.keras.optimizers import Adam



# Definition des variables utilisé


Q = np.zeros((3 , 3))



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



def jeu(strat):
    #Initialisation des policiers
    personnages : List[Person] = []
    num_police = 1
    strategie = strat
    for i in range(num_police):
        #print(strategie)
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

    x =  0
    y =  2
    positions_civils.append([x , y])
    civil = Person(CIVIL, x, y, n)  
    personnages.append(civil)

    x =  1
    y =  3
    positions_civils.append([x , y])
    civil = Person(CIVIL, x, y, n)
    personnages.append(civil)

    x =  2
    y =  4
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


    history = []
    nb_tour = 25
    for i in range(nb_tour):
        #afficher_grille(n, personnages)

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

        #print()

    score_policier = 0
    score_pick = 0
    for personne in personnages:
        

        if is_policier(personne):
            score_policier += personne.score
        if is_pick(personne):
            score_pick += personne.score

    #print("Score des Policiers :", score_policier)
    #print("Score des Pick :", score_pick)
    #print()
    #print(history)

    
    return (score_policier , score_pick)





def qLearning(Q, num_episodes, discount_factor = 0.8,
							alpha = 0.6, epsilon = 0.4):
	
    
    prev_action = 1
    state = 1
    
    for ith_episode in tqdm(range(num_episodes)):
        
        score_pol , score_pick= jeu(prev_action)
        if ((score_pol/1) - (score_pick/2)) > 0:
            state = 0
        elif ((score_pol /1) - (score_pick/2)) < 0:
            state = 1
        else:
            state = 2

        for t in itertools.count():
            
           
            action = 0 


            
            #on utilise epsilon pour separer la phase d'exploration et d'exploitation
            if random.random() > epsilon: 
                action = np.argmax(Q[state])
            else:
                action = random.randint(0 , 2)
            
            action += 1

           
            score_pol , score_pick = jeu(action)
            done = True 
            next_state = 2
            if ((score_pol/ 1) - (score_pick / 2)) > 0:
                next_state = 0
            elif ((score_pol / 1) - (score_pick/2)) < 0:
                next_state = 1
            else:
                next_state = 2

            reward = (score_pol / 1) - (score_pick / 2)
            prev_action = action 
            
            
            best_next_action = np.argmax(Q[next_state])	
            td_target = reward + discount_factor * Q[next_state][best_next_action]
            td_delta = td_target - Q[state][action - 1]
            Q[state][action -1] += alpha * td_delta

            # done is True if episode terminated
            if done:
                break
                
        state = next_state
    return Q


Q = qLearning(Q , 100000)
print()
print(Q)