""" 
This program loads the Seaborn tips data and produces a regression plot 
for the tips against the size of the party (using discrete values on x axis)
with a jitter effect to better visualize overlapping points."""
# Author: Marcin Kaminski

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

#print(dataset.head())

sns.set_style("whitegrid")
sns.lmplot(x='size', y='tip', data=dataset, x_jitter=.05)

plt.show()

