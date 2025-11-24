""" 
This program loads the Seaborn tips data and produces a regression plot 
for the tips against the size of the party (using discrete values on x axis).
Instead of dots, an estimator has been used to estimate the mean tip for each size
"""
# Author: Marcin Kaminski

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

#print(dataset.head())

sns.set_style("whitegrid")
sns.lmplot(x='size', y='tip', data=dataset, x_estimator=np.mean)


plt.show()

