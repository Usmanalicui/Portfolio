#Data Visualization



#importing Libraries and data set

import seaborn as sns
import matplotlib.pyplot as plt
import time
flower = sns.load_dataset('iris')

print("Everything will take 3-secs to pop")
time.sleep(1)



#making a simple barplot

print("Barplot")
print("Relationship between sepal_width and Species")
time.sleep(3)
sns.barplot(x='species',y='sepal_width', data =flower)
plt.show()


#Again with petal_length as y

print("Between petal_length and Species")
time.sleep(3)
sns.barplot(x= "species", y= "petal_length", data = flower)
plt.show()


