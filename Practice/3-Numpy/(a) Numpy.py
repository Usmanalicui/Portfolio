#Importing Numpy 
import numpy as np
import time as t

#Creating 1D Array
print("Creating 1D array")
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a)  # printing array
t.sleep(1)

#Type of array 
print("Type of array:", type(a))  # printing type
t.sleep(1)

#indexing (specific index, Range of indexing) 
#Specific
print("Specific index a[5]:", a[5])
t.sleep(1)

#Range of Indexing
print("Range of indexing a[4:9]:", a[4:9])
t.sleep(1)

#Create arrays that consists of zero 
print("Array with zeros:", np.zeros([6]))
t.sleep(1)

#Create Arrays with one 
print("Array with ones:", np.ones([6]))
t.sleep(1)

#Create Arrays with empty 
print("Array with empty:", np.empty([6]))
t.sleep(1)

print("Assignment")
print("Differnce between empty and one's Array")
t.sleep(1)

print("Empty contains random garbage values and can be one, Ones contain only one")

#Make through Range 
print("Range with 200 elements:", np.arange(200))
t.sleep(1)

#Specify range
print("Range 0 to 50:", np.arange(0, 50))
t.sleep(1)

#Specific range with specific interval aka gap 
print("Countdown 150 to 0:", np.arange(150, 0, -1))
t.sleep(1)

print("Assignment No. 2")
print("Make a table through interval")
print(np.arange(6, 61, 6))
t.sleep(1)

#Use line space and tell whats use is it for 
print("Linspace Example:", np.linspace(2, 3))
print("Use to find numbers within a list having equal distance from the next selected number")
t.sleep(1)

#Specify data types and make an array of specific data types 
x = np.array([2, 3, 4, 5])
print("Original dtype:", x.dtype)
t.sleep(1)
x = np.array([2, 3, 4, 5], dtype=float)
print("New array with float dtype:", x)
t.sleep(1)
print("New dtype:", x.dtype)
t.sleep(1)

#Make whole array of int into decimal just putting one val in it
b = np.arange(2,10)
b = np.append(b, [10])
b = np.insert(b, 0, 1)
print("Modified array b:", b)
t.sleep(1)

#Sorting asc and des both order
b.sort()
print("Sorted ascending:", b)
t.sleep(1)
print("Sorted descending:", np.sort(b)[::-1])
t.sleep(1)

#Concatenate two arrays 
c = np.array([[1,2],[3,4]])
d = np.array([[5, 6],[7,8]])
e = np.concatenate((c, d), axis = 1)
print("Concatenated array:", e)
t.sleep(1)
print("While concatenating I enountered these errors, first i had to make a 2D array of lists, i was creating tuple, 2nd is Order of 2D arrays should be exact same as eachother, Third and final is the axis one that i got, I was doing it in One day array and it doesnt work on that i had to create it 1D in next practices i will show that")
t.sleep(1)

#Change axis of the concatenate make vertical then horizontal i mean in merging 
e = e.reshape(1, -1)
print("Reshaped e:", e)
t.sleep(1)

#Find number of dimensions in an array 
print("Dimensions of e:", e.ndim)
t.sleep(1)

#Find Number of elements in an array 
print("Number of elements in e:", e.size)
t.sleep(1)

#Find its shape 
print("Shape of e:", e.shape)
t.sleep(1)

#reshape the Array 
f = np.arange(1, 11)
f = f.reshape(2, -1)
print("Reshaped f (2 rows):", f)
t.sleep(1)

#Use order with reshape 
f = f.reshape(2, -1)
print("Column Wise")
g = np.sort(f)[::-1,:]
print("Sorted column-wise:", g)
t.sleep(1)
print("Row wise")
h = np.sort(f)[:, ::-1]
print("Sorted row-wise:", h)
t.sleep(1)

#convert 1d into 2d array 
i = np.arange(10)
i = i.reshape(-1, 2)  
print("1D to 2D (reshape with -1,2):")
print(i)
t.sleep(1)

#row wise and column wise making 2D arrays 
i = np.arange(10)
print("Column wise")
i = i.reshape(-1, 1)
print(i)
t.sleep(1)
print("Row Wise")
j = i.reshape(1, -1)
print(j)
t.sleep(1)

#slicing arrays 
k = np.arange(11)
print("Slice k[5:11]:", k[5:11])
t.sleep(1)

#Multiply Whole array with 6 and add whole array with 6 also get sum of whole array
l = np.arange(12)
print("Multiplying whole array with 6")
l = l * 6
print(l)
t.sleep(1)
print("Getting Sum of the whole array:", l.sum())
t.sleep(1)
print("The end")
t.sleep(3)
