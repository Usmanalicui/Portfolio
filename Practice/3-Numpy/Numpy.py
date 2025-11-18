#Importing Libraries
import numpy as np

#Creating Arrays in Numpy
#Creating 1-D Arrays in Numpy
a = np.array([1, 2, 3, 4, 5, 6])
a

b = np.zeros([5])
b

c = np.ones([5])
c

d = np.empty([5])
d

e = np.arange(2)
e

f = np.arange(2, 20)
f

g = np.arange(2, 20, 2)
g

h = np.linspace(0,20,num = 5)
h

i = np.ones(5, dtype = np.int8)
i

j = np.ones (5, dtype = np.float64)
j

#Making 2-D Arrays
k = np.zeros((4, 4))
k

#making one 3d-array
l = np.zeros((24)).reshape(2, 3, 4)
l
