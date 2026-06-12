from sklearn.linear_model import Perceptron
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
 

x , y = make_classification(n_samples=10000,n_features=10000,random_state=42)
x_train, x_test, y_train , y_test = train_test_split(x,y,random_state=42   )

clf = Perceptron(
    max_iter=10000,
    eta0= 0.1,
    random_state=42,
    tol=1e-3,
    shuffle=True
)
 

clf.fit(x_train,y_train)


#evaluating the model 

accuracy = clf.score(x_test,y_test)
print(f"Accuracy {accuracy}")

