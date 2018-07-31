import numpy as np
import random
import time 

n= int(input())
np.random.seed(0)  #seeding
arr1 = np.random.randint(0, 10, size=(n,n))
arr2 = np.random.randint(0, 10, size=(n,n))
res = np.zeros((n,n))

start = time.time() #start time

for i in range(n):
 
    # iterating by coloum by B 
    for j in range(n):
 
        # iterating by rows of B
        for k in range(n):
            res[i][j] = res[i][j] + arr1[i][k] * arr2[k][j]
 
for r in res:
 print(r)

print("--- %s seconds ---" % (time.time() - start))  #end time

