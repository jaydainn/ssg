# ******************************************************
# @author: Jeremy Dain, Ethan Postic et Lemuel Falret
# ******************************************************
#
# police: 2 
# civil: 1
# pickpocket: 3

import random
import numpy as np 
import json
from IPython.display import clear_output
from collections import deque
import progressbar
import math



from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Dense, Embedding, Reshape
from tensorflow.keras.optimizers import Adam






n = 6
grid = np.zeros((n , n))
num_civ = 3
num_police = 1
num_pick = 1


history = []

Q = np.zeros(2)


positions_civils = []


for i in range(num_civ ):
     x =  random.randint(0, n -1)
     y =  random.randint(0, n -1)
     positions_civils.append([x , y])
     grid[x][y] = 1


positions_civils = np.array(positions_civils)
for i in range(num_pick ):
     x =  math.floor(positions_civils[: , 0].mean())
     print(x)
     y =  math.floor(positions_civils[:  , 1].mean())
     print(y)
     grid[x][y] = 3

for i in range(num_police ):
     x =  random.randint(0, n -1)
     y =  random.randint(0, n -1 )
     grid[x][y] = 2


for i in  range(15):
     for j in range(n):
          for k in range(n):
               if(grid[j][k] != 0 ):
                    if(j < (n-1) and k < (n-1)):
                         direction = random.randint(1 , 4)
                         if(direction == 1 ):
                              if(grid [j + 1][k] == 0 ):
                                   grid[j + 1 ][k] = grid[j][k]
                                   grid[j][k] = 0 
                              else:
                                   if((grid[j+1][k] == 3 and grid[j][k] == 2)  or (grid[j+1][k] == 2 and grid[j][k] == 3)):
                                        Q[0] += 1 
                                        grid[j+1][k] = 2
                                        grid[j][k] = 0 
                                   elif( (grid[j+1][k] == 3 and grid[j][k] == 1 ) or (grid[j+1][k] == 1 and grid[j][k] == 3) ):
                                        Q[1] += 1 
                                        grid[j+1][k] = 3
                                        grid[j][k] = 0
                         elif(direction == 2):
                              if(grid [j - 1][k] == 0 ):
                                   grid[j - 1 ][k] = grid[j][k]
                                   grid[j][k] = 0 
                              else:
                                   if((grid[j-1][k] == 3 and grid[j][k] == 2)  or (grid[j-1][k] == 2 and grid[j][k] == 3)):
                                        Q[0] += 1 
                                        grid[j-1][k] = 2
                                        grid[j][k] = 0 
                                   elif( (grid[j-1][k] == 3 and grid[j][k] == 1 ) or (grid[j-1][k] == 1 and grid[j][k] == 3) ):
                                        Q[1] += 1 
                                        grid[j-1][k] = 3
                                        grid[j][k] = 0
                         elif(direction == 3):
                              if(grid [j][k+1] == 0 ):
                                   grid[j][k+1] = grid[j][k]
                                   grid[j][k] = 0 
                              else:
                                   if((grid[j][k+1] == 3 and grid[j][k] == 2)  or (grid[j][k+1] == 2 and grid[j][k] == 3)):
                                        Q[0] += 1 
                                        grid[j][k+1] = 2
                                        grid[j][k] = 0 
                                   elif( (grid[j][k+1] == 3 and grid[j][k] == 1 ) or (grid[j][k+1] == 1 and grid[j][k] == 3) ):
                                        Q[1] += 1 
                                        grid[j][k+1] = 3
                                        grid[j][k] = 0
                         elif(direction == 4):
                              if(grid [j][k-1] == 0 ):
                                   grid[j][k-1] = grid[j][k]
                                   grid[j][k] = 0 
                              else:
                                   if((grid[j][k-1] == 3 and grid[j][k] == 2)  or (grid[j][k-1] == 2 and grid[j][k] == 3)):
                                        Q[0] += 1 
                                        grid[j][k-1] = 2
                                        grid[j][k] = 0 
                                   elif( (grid[j][k-1] == 3 and grid[j][k] == 1 ) or (grid[j][k-1] == 1 and grid[j][k] == 3) ):
                                        Q[1] += 1 
                                        grid[j][k-1] = 3
                                        grid[j][k] = 0
                    elif(j >= n -1 ):
                         grid[j - 1][k] = grid[j][k]
                         grid[j][k] = 0 
                    elif(j <= 0):
                         grid[j -1][k] = grid[j][k]
                         grid[j][k] = 0 
                    elif(k >= n -1):
                         grid[j][k -1] = grid[j][k]
                         grid[j][k] = 0 
                    elif(k <= 0 ):
                         grid[j][k + 1] = grid[j][k]
                         grid[j][k] = 0 



     print(grid)
     #history.append(grid.tolist())
     print(Q)



               

     

