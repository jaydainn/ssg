import math
import numpy as np
import random


nbpicks = 1 
nbpolice = 1 
nbcivil = 3


class Character:
  def __init__(self, x, y, type):
    self.x = x
    self.y = y
    self.type = type


class GridBox:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.items = []

  def check_score(self, score):
    print("ok")



  
       
            




class Grid:
  def __init__(self):
    self.items = []
    self.score = np.zeros(2)
    for i in range (5):
        for j in range(5):
          self.items.append(GridBox(i , j ))
    for i in range(nbcivil):
        r = int(random.randint(0 , 24))
        self.items[r].items.append(Character(self.items[r].x , self.items[r].y , 1))

    for i in range(nbpolice):
        r = int(random.randint(0 , 24))
        self.items[r].items.append(Character(self.items[r].x , self.items[r].y , 2))
    
    for i in range(nbpicks):
        r = int(random.randint(0 , 24))
        self.items[r].items.append(Character(self.items[r].x , self.items[r].y , 3))

  def display(self):
    displaygrid = np.zeros( (5 , 5) )
    for i in range(24):
        x = self.items[i].x
        y = self.items[i].y
        tp = 0 
        if len(self.items[i].items) > 0 : 
            tp = self.items[i].items[0].type
        displaygrid[x][y] = tp
    print(displaygrid)
        




    

 
    

grid = Grid()

grid.display()



