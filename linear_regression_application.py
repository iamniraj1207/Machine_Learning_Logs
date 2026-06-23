import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

x_train = np.array([1.0,2.0])
y_train = np.array([300.0,500.0])

print(f"{x_train} are the square feet values")
print(f"{y_train} is the price of the house ")

m = x_train.shape[0]
M = y_train.shape[0]

print(f"The number of training set for the example is {m}")

i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"x^i = {x_i} and y^i = {y_i}")

plt.scatter(x_train,y_train,marker = 'x', c = 'r')
plt.title('Housing Prices')
plt.ylabel('Prices in Thousand of Dollars')
plt.xlabel('Sizes in 1000sqft')

plt.show()



w = 200                         
b = 100    
x_i = 1.2
cost_1200sqft = w * x_i + b    

print(f"${cost_1200sqft:.0f} thousand dollars")
