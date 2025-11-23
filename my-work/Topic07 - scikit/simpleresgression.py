# import the library
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
data = sns.load_dataset('tips')

# the first five entries of the dataset
print(data.head())
sns.set_style('whitegrid')
sns.scatterplot(x='total_bill', y='tip', data=data)
plt.show()
