import numpy as np
b = 100
W = np.array([50,70,90])###list or vectors of weights, considering multiple linear regression or features present in the algorithm 
X = np.array([300,400,700]) ###size in 1000 sq ft. It is also a vector, as these are in a list and then finding the function value or fit line by vectorization or summing up of all the weights and X vector with Biases 
m = X.shape[0]
# finding the predicted value 
f = 0
for i in range(0,m):
    f += W[i] * X[i]
f = f + b

print(f)

# Now doing this with vectorization 
# Means it will also help the GPU or hardware to perform fewer mathematical operations as we performed in the for loop 

F = np.dot(W,X) + b
print(F)
# Getting a more efficient program with vectorization, or the so-called dot product of vectors to get a numerical value
#THE DOT PRODUCT FUNCTION OF NUMPY PERFORMS THESE FOR LOOPS EQUATION IN A SINGLE STEP WITH USE OF GPU 

###GRADIENT DESCENT WITH VECTORIZATION 

#considering for a Gradient Descent 
#formula is w = w - alpha * d/dw(J)
W = np.array([80,90,100])
dj = np.array([0.3,0.4,0.5])
alpha = 0.1

for j in range(0,3):# without vectorization
    W = W - alpha * dj

print(W)
#with vectorization 
# remove the non vectorised code to get correct Gradient descent Minima for the Weights 
W = W - alpha * dj
print(W)
#This type of vectorization helps when there are thousands of features j
