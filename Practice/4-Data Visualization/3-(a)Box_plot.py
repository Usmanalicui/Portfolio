#Data Visualization



#importing Libraries and data set

import seaborn as sns
import matplotlib.pyplot as plt
from numpy import mean
import time
boat = sns.load_dataset('titanic')

print("Everything will take 3-secs to pop")
time.sleep(1)


#Making a horizontal barplot
print("Making a horizontal barplot")
sns.barplot(x = "fare", y = "class", hue = "sex", data = boat, estimator = mean, errorbar = None, saturation = 1 )
plt.show()
