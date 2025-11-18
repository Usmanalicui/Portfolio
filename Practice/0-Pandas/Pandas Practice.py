#Pandas Practice

#Importing Libraries

import pandas as pd
import numpy as np

#Create Object series
a = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ])
a

#Create Object of dates of 6 days
b = pd.date_range("20250821", periods = 6)
b

#Assignment
print("Why its not exclusive tell that")
print("Its not exclusive cause it takes the first argument as default value and then counts the next given values(5 in this case). So, its not exclusive")

#Create a data frame with random
df = pd.DataFrame(np.random.randn(86431, 10), index = pd.date_range("20250821", periods = 86431), columns = list("USMANAASIA"))
df

#Make an error and find it, explain it why it happened to
#error = pd.DataFrame(np.random.randn(86431, 10), index = pd.date_range("20250821", periods = 100000), columns = list("USMANAASIA"))
#error
print("the error above is the number of index are not as the same as number of columns and python can only make dates up to 86431 Days above it throws error. ")

#Make an DataFrame with columns having ABCDEF, 1.0, timestamps, again 1.0 but with index range, 3, (test, train, test, train), through dic
df2 = pd.DataFrame(
{
	"A":1.0,
	"B":pd.Timestamp("20231231"),
	"C":pd.Series(1, index = list(range(4)), dtype = "float64"),
	"D":pd.array([3]*4, dtype = "int32"),
	"E":pd.Categorical(["Test", "Train", "Test", "Train"]),
	"F":"Foo"
})
df2

#find data type
df2.dtypes

#Assignment
print("what is int32 and int64")
print("The Difference is size and memory, int32 uses less memory and can store lesser digits then int64 who can store in quantillions")

#find head and tail of the data
df2.head(2)
df2.tail(2)

#find index of the data frame
df2.index

#convert data into numpy
df2.to_numpy

#describe the data set
df2.describe

#Take Transpose of the data set
df2.T

#Sort the data by indexs
df2.sort_index(axis = 1, ascending = False)
df2.sort_index(axis = 0, ascending = True)

#sort with specific column, both wise
df.sort_values(by = ["U"], ascending = True)
df.sort_values(by = df.columns[0], ascending = False)

#Row Wise selection
df[0:13]

#Row wise and column wise with loc
df.loc["2030-06-12", ['U']]

#index based location
df.iloc[3:4, 5:]

#index based location
df.iloc[:, 5:]

#have rows greater than 1
df.iloc[:, 5:] [df.iloc[:, 5:]>1].dropna(how = "all")

#add new column to the data set and add values to it
df["H"] = np.random.randn(86431)

#Assignment
#Add +1 in and get its average and make a new column of it
df.insert(5, "-", (df["U"]+1).mean())
df
df["-"] = df["-"].astype(int)
