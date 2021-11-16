import sklearn
from sklearn import datasets, model_selection
X, y = datasets.load_boston(return_X_y=True)
print(X.shape)
print(y.shape)

print(X[:5])

