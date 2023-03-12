import random
import numpy as np

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

a = np.array([1,2,3,4,5,6,7,8,9])
N = a.shape[0]
c = np.sum(a[N*rank//size:N*(rank+1)//size])
c = np.array([c]) # after np.sum c is just a number but not an array, so we need to turn c into an array
#print(c)
total = np.zeros(1,dtype =c.dtype) # notice that the type should be the same, otherwise there will be mistakes
comm.Reduce(c, total, op=MPI.SUM, root=0)
print(rank, total)

# notice that the type of the numbers matter
# got stuck at 