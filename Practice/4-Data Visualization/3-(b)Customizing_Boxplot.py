#Data Visualization



#importing Libraries and data set

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean
import time
boat = sns.load_dataset('titanic')

print("Everything will take 3-secs to pop")
time.sleep(1)


#Adding Markor to the plot
sns.boxplot(x = "survived",
	y = "age",
	data = boat,
	showmeans = True)
plt.show()


#Customizing markor of the plot
sns.boxplot(x = "survived",
	y = "age",
	data = boat, showmeans = True,
	meanprops = {"marker":"*",
			"markersize":"14",
			"markeredgecolor":"red"
			})
plt.show()