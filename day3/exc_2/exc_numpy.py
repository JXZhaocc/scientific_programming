import numpy as np

# Create a null vector of size 10 but the fifth value which is 1
x = np.zeros(10)
x[5] = 1
print(x)

# Create a vector with values ranging from 10 to 49
v = np.arange(10,50)
print(v)

# Reverse a vector (first element becomes last)
s = v[::-1]
print(s)

# Create a 3x3 matrix with values ranging from 0 to 8
a = np.arange(0,9).reshape(3,3)
print(a)

# Find indices of non-zero elements from [1,2,0,0,4,0]
b = np.array([1,2,0,0,4,0])
c = b > 0
print(b[c])

#Create a random vector of size 30 and find the mean value
d = np.random.random(30).mean()
print(d)

# Create a 2d array with 1 on the border and 0 inside
e = np.ones((5,5))
e[1:-1,1:-1] = 0
print(e)

# Create a 8x8 matrix and fill it with a checkerboard pattern
f = np.zeros((8,8),dtype=int)
f[1::2,::2] = 1
f[::2,1::2] = 1
print(f)

#Create a checkerboard 8x8 matrix using the tile function
g = np.tile(np.array([[0,1],[1,0]]),(4,4))
print(g)

h = np.array([[1, 2], [3, 4]])
hh = np.tile(h, (2, 2))
print(hh)

#Given a 1D array, negate all elements which are between 3 and 8, in place
aa = np.arange(11)
aa[(3 < aa) & (aa <= 8)] *= -1
print(aa[aa>0])
print(aa)

# Create a random vector of size 10 and sort it
bb = np.random.random(10)
bb.sort()
print(bb)

#Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A, B)
print(equal)