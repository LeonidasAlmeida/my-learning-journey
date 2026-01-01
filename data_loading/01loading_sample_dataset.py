#problem: you want to load a preexisting sample dataset from the scikit-learn libray
#solution scikit-learn comes with a number of popular dataset for you to use
#Load scikit-learn's datasets
from sklearn import datasets
#load digits dataset
digits = datasets.load_digits()
#create features matrix
features = digits.data
#create target vector
target = digits.target
#view first observation
print(features[0])