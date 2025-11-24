""" 
This program loads the Seaborn tips data and produces a regression plot 
for the tips against the size of the party (using discrete values on x axis).
"""
# Author: Marcin Kaminski

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

#print(dataset.head())

sns.set_style("whitegrid")
sns.lmplot(x='size', y='tip', data=dataset)

plt.show()

