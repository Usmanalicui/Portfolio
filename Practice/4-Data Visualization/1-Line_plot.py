#Data Visualization



#importing Libraries and data set

import seaborn as sns
import matplotlib.pyplot as plt
import time
flower = sns.load_dataset('iris')

print("Everything will take 3-secs to pop")
time.sleep(1)

#Printing first few rows of the data set
print("Printing first few rows of the data set")
time.sleep(3)
print(flower.head(5))
time.sleep(1)



#Plotting a Simple line graph
print("Plotting Simple Lineplot")
time.sleep(3)
sns.lineplot(x= "sepal_length", y = "sepal_width", data = flower)
plt.show()
time.sleep(1)


#Adding title to the plot

print("Adding Title to the Plot")
time.sleep(3)
sns.lineplot(x= "sepal_length", y = "sepal_width", data = flower)
plt.title("Relationship B/W Sepal's Length and width")
plt.show()
time.sleep(1)



#Adding limits to the plot

print("Adding limits to the Plot")
time.sleep(1)
print("Setting x & y, Both Equal to 2")
time.sleep(3)
sns.lineplot(x="sepal_length", y ="sepal_width", data = flower)
plt.xlim(2)
plt.ylim(2)
plt.title("Relationship B/W Sepal's Length and width")
plt.show()
time.sleep(1)



#Setting Styles to the Plot

print("Adding Styles")
time.sleep(3)
sns.set_style(style = None, rc = None)
sns.set_style("dark")
sns.lineplot(x="sepal_length", y="sepal_width", data = flower)
plt.title("Relationship B/W Sepal's Length and width")
plt.show()
time.sleep(1)



#Size of figure
print("Changing Figure Size")
time.sleep(3)
sns.lineplot(x='sepal_length', y= 'sepal_width', data = flower)
plt.title("Relationship B/W Sepal's Length and width")
plt.figure(figsize= (8,6))
plt.show()