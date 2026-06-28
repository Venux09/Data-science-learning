from sklearn.linear_model import Perceptron # perceptron a neuron 
from sklearn.datasets import make_classification # fake data just for the classiffication linear  model 
from sklearn.model_selection import train_test_split # Splliting the dataset 




x , y = make_classification(n_samples=10000000,n_features=100,n_classes=2,random_state=42)#data for the model 
x_train,x_test,y_train, y_test = train_test_split(x,y,random_state=42)#splliting the data 




clf = Perceptron(
    max_iter=10 , #training the data over and over for the 1000 times 
    random_state=42,
    eta0=0.1,#learing rate of the data 
    shuffle=True
)


clf.fit(x_train,y_train)#fitting the data on th clf model 



accuracy = clf.score(x_test,y_test) # accuracy of the data 


print(f'Accuracy:{accuracy*100}'
)



