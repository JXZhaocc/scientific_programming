# Program to multiply two matrices using nested loops
import random
import numpy as np

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

N = 250

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
'''def results(N):
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result'''

# iterate through rows of X
def cal(X,Y,):
    result = np.dot(X,Y)
    return result

#result = results(N)
result_final = cal(X,Y)

print(rank, result_final)

'''for r in result_final:
    print(r)'''

# You can use conda install to install mpi4py, pip install
# cannot becasue of the complex dependencies

#I also think we will get different results as we are using random.randint