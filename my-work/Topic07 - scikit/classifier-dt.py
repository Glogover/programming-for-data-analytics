import pandas as pd

dataurl = "https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl)
irisdf.head(3)
print(irisdf.head(3))

colnames = ["sepal_length (cm)", "sepal_width (cm)", "petal_length (cm)", "petal_width (cm)"]
x = irisdf[colnames] # input features, independent variables
y = irisdf["target"] # output label, target variable, dependent variable

from sklearn import tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)




