# This program loads the Seaborn tips data and produces a regression plot for the tips against the total bill .
# Author: Marcin Kaminski

import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

#print(dataset.head())

sns.set_style("whitegrid")
#sns.lmplot(x='total_bill', y='tip', order = 1, data=dataset)
#sns.lmplot(x='total_bill', y='tip', order = 2, data=dataset)
#sns.lmplot(x='total_bill', y='tip', order = 3, data=dataset)
#sns.lmplot(x='total_bill', y='tip', order = 4, data=dataset)
#sns.lmplot(x='total_bill', y='tip', order = 5, data=dataset)
#sns.lmplot(x='total_bill', y='tip', order = 10, data=dataset)
sns.lmplot(x='total_bill', y='tip', order = 20, data=dataset)



plt.show()

