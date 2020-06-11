import numpy as np
from numpy import random

arr = random.randint(1,10,(5,5))
print("Matrica\n",arr ,"\n")
arr = np.delete(arr,-1,axis=1)
print("Matrica\n",arr ,"\n")


