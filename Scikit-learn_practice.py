import numpy as np 

X = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])
y = np.array([0, 0, 0, 1, 1, 1])

from sklearn.linear_model import LogisticRegression 

lr_model = LogisticRegression()
lr_model.fit(X,y)# converts the function to sigmoid and then finds decision boundary and then also finds the best weights and biases or Gradient descent 

y_pred = lr_model.predict(X) # here we get the pred value for the training set data
print(y_pred)

acc_log = lr_model.score(X,y)# to see the accuracy with the training set data 
print(acc_log)
