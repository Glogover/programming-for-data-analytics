# This program loads the Seaborn tips data and prints out the top 5 rows (ie the head)
# Author: Marcin Kaminski

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

print(dataset.head())

