import numpy as np 
radii = np.array([1.3,2.0])
print(np.pi * radii**2)

array_1 = np.array([[1], [2], [3], [4]])
print(array_1.shape)

number_arr = np.array([1,2,3,69,89,76,19,56,57,67])
teenagers = number_arr[number_arr < 18]
adults = number_arr[(number_arr >= 18) | (number_arr < 65)]
print(adults)
print(teenagers)
adultss = np.where(number_arr >= 18, number_arr, np.nan)# used where function first input is for condition, second is the selected array for the argument, and third is to replace the values
#which helps maintain the same size/shape of the array 
print(adultss)

rng = np.random.default_rng()
print(rng.integers(1,7))

np.random.seed(seed = 1)#.seed method helps in keeping the same value after random number generations 

print(np.random.uniform(low = -1, high = 10, size = (3,2)))#.uniform deals with the generation of random numbers in the form of decimals 

fruits = ['🥥', '🍍', '🥭', '🍎', '🍌']
fruits = rng.choice(fruits, size=3)
print(fruits)

