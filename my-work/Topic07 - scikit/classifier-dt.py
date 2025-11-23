import pandas as pd

dataurl = "https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl) # load dataset into a pandas dataframe
print(irisdf.head(3)) # print first 3 rows of the dataframe

colnames = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"] # feature column names
x = irisdf[colnames] # input features, independent variables 
y = irisdf["target"] # output label, target variable, dependent variable

# decision tree classifier
#from sklearn import tree # import decision tree classifier
#clf = tree.DecisionTreeClassifier() # create decision tree classifier object

# kn classifier
from sklearn.neighbors import KNeighborsClassifier # import k-nearest neighbors classifier
clf = KNeighborsClassifier(n_neighbors=5) # create k-nearest neighbors classifier object with k=5


clf = clf.fit(x.values, y) # fit the model with input features and target variable
print(clf.predict([[1,3,4,5]])) # Predict the class label for a new sample with features [1,3,4,5]
print(clf.score(x.values, y))  # Print the accuracy of the model on the training data








