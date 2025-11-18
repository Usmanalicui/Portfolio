#Data Visualization



#importing Libraries and data set

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean
import time
boat = sns.load_dataset('titanic')

print("Everything will take 3-secs to pop")
time.sleep(1)


#making a barplot with grouping(Hue)
print("Barplot with grouping and different colours")
time.sleep(3)
sns.barplot(x="who", y = "alone", hue = "sex", data = boat)
plt.show()


#changing order of the male and female
print("Changing order")
print("Putting Female to first")
time.sleep(3)
sns.barplot(x="who", y = "alone", hue = "sex", data = boat, order = ["woman", "man", "child"])
plt.show()


#Adding colors to the plot
print("changning color to the red")
sns.barplot(x="who", y = "alone", hue="sex", data = boat, color = "red")
plt.show()


#removing error bars
print("removing error bars aka weird stick type lines on the top of the bars")
sns.barplot(x = "who", y = "alone", hue = "sex", data = boat, color = "red", ci = None)
plt.show()


#changing pallet of the plot
print("changing color pallet")
sns.barplot(x= "who", y = "alone", hue= "sex", data = boat, color = "red", ci = None, palette = "pastel")
plt.show()


#Adding Estimators to the plot
print("Adding estimators")
sns.barplot(x= "who", y = "alone", hue= "sex", data = boat, color = "red", errorbar = None, palette = "pastel", estimator = mean)
plt.show()



#Making a horizontal barplot
print("Making a horizontal barplot")
sns.barplot(x = "fare", y = "class", hue = "sex", data = boat, estimator = mean, errorbar = None, saturation = 1 )
plt.show()


#Adding linewidth, facecolor, errorcolor and edge color to the plot
sns.barplot(x="fare", y = "class", hue = "sex", data = boat, edgecolor = "0", facecolor = (0,1,1,1), linewidth = 1, errcolor = ".5")
plt.show()
print("This is the End")
