#Data Visualization



#importing Libraries and data set

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean
import time
boat = sns.load_dataset('titanic')

print("Everything will take 3-secs to pop")
time.sleep(1)


#Making a simple BoxPlot
print("Making a simple Box Plot")
#Setting a style for BoxPlot
sns.set(style = "whitegrid")
sns.boxplot(x= "class", y= "fare",data = boat)
plt.show()



#Importing New Data set
print("Importing a New Data set")
tips = sns.load_dataset("tips")
tips


#Checking on which day we get highest tips
print("Checking on which day we get highest tips")
sns.set(style = "whitegrid")
sns.boxplot(x = "day", y= "tip", data = tips)
plt.show()


#Changing Saturation of BoxPlot
print("Changing Saturation of Box Plot")
sns.set(style="whitegrid")
sns.boxplot(x= "day", y = "tip", data = tips, saturation = .3)
plt.show()


#Making a graph with a single variable
print("Making a graph with a single variable")
#Choosing Y variable cause we dont want anything horizantal
sns.boxplot(y =tips["total_bills"])
plt.show()


#Making a graph with groups
print("Checking if Smoker gives more Tips than non smoker")
sns.boxplot(x = "day", y = "tip", data = tips, hue = "smoker")
plt.show()


#Use Dodge function with it
print("Using Dodge as true")
sns.boxplot(x = "day", y = "tip", data = tips, hue = "smoker", dodge = True)
plt.show()

print("Without Dodge Function")
sns.boxplot(x = "day", y = "tip", data = tips, hue = "smoker", dodge = False)
plt.title("Overlapping on eachother be like")
plt.show()