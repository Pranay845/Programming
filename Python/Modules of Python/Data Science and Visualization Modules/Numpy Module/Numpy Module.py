"""
Numpy Module for Big Calculations
and also for Arrays and Data Manipulation.
"""

import numpy as np

# Topic: Types of Arrays,It's Making and It's Methods
a = np.array([1, 2, 3])
b = np.array([1, 2, 3], np.int32)
c = np.array([[1, 2, 3]])
d = np.array([[1, 2, 3], [4, 5, 6]], np.int64)

# Topic: To get Information
print(d[0, 1])
print(d.shape)
print(d.dtype)

# Topic: Changing the Numpy Array
d[0, 1] = 9

e = np.zeros((20, 20), dtype=int)  # makes a array of all zeros
print(e)

f = np.ones((20, 20, 6), dtype=int)  # makes a array of all ones
print(f)

g = np.arange(1, 10, 2)  # makes evenly spaced array with start,stop,step
print(g)

h = np.arange(1.8, 10.9, 2.7)
print(h)

i = np.linspace(1, 4, 6)  # makes evenly spaced array with equal interval
print(i)

j = np.empty((3, 6))  # makes array at faster passe
print(j)

k = np.empty_like(j)
print(k)

l = np.identity(20)  # makes array with diagonal ones
print(l)

e = d.reshape(3, 2)  # reshapes the array
print(e)

e = e.ravel()  # makes array into 1D
print(e)

# Topic: Average
s = np.array([[1, 2, 3], [4, 5, 6]])

t = s.argmax()
print(t)

u = s.argmin()
print(u)

# Topic: Sorting
v = s.argsort()
print(v)

w = s.argsort(axis=0)
print(w)

x = s.argsort(axis=1)
print(x)

y = np.array([[1, 2], [3, 4]])
z = np.array([[1, 2], [3, 4]])

# Topic: Math operations
ab = np.add(y, z)
print(ab)

bc = np.subtract(y, z)
print(bc)

cd = np.multiply(y, z)
print(cd)

de = np.divide(y, z)
print(de)

ef = np.sqrt(y)
print(ef)

fg = np.dot(y, z)
print(fg)

gh = np.sum(y)
print(gh)

hi = np.max(y)
print(hi)

ij = np.min(y)
print(ij)

# Topic: Information
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m = np.array(m)

p = m.ndim  # lists the dimensions of array
print(p)

q = m.size  # lists the size of array
print(q)

r = m.nbytes  # lists the bytes of array
print(r)

jk = np.where(y > 5)
print(jk)

kl = np.count_nonzero(y)
print(kl)

lm = np.nonzero(y)
print(lm)

mn = y.tolist()
print(mn)

# Topic: Manipulation
n = m.T  # change rows to columns and viceversa
print(n)

m.flat  # flats the array
print(m)

m = np.sum(m, axis=1)  # add all columns in array
print(m)

m = np.sum(m, axis=0)  # add all rows in array
print(m)

no = np.array([[1, 3, 4], [5, 6, 8]])
print(a.data)

op = np.append(no[1], 45)
print(op)

pq = np.delete(no, 0)
print(pq)

# Topic: More types of Numpy Array Making
qr = np.full((2, 2), 8)
print(qr)

rs = np.eye(1)
print(rs)

st = np.random.random((2, 3))
print(st)

# Documentation: https://numpy.org/doc/
