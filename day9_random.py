import numpy as np

#Random numbers in numpy
from numpy import random

#Generate Random Number
x = random.randint(50)
print(x)

#Generate Random Float
x = random.rand()
print(x)

#Generate Random Array
x=random.randint(50,size=(4))
print(x)

x = random.randint(50,size=(2,2))
print(x)

#Generate a 1-D array
x = random.rand(5)
print(x)

#Generate a 2-D array
x = random.rand(3,3)
print(x)

#Generate Random Number From Array
x = random.choice([1,2,3,4])
print(x)

x = random.choice([1,2,3,4], size=(3,3))
print(x)

#Random Distribution
x = random.choice([4,5,6,7], p=[0.1, 0.3, 0.6, 0.0], size=(20))
print(x)

x = random.choice([4,5,6,7], p=[0.1, 0.3, 0.6, 0.0], size=(3,3))
print(x)

#Generating Permutation of Arrays
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

#Normal Distribution
x = random.normal(size=(2, 3))
print(x)

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

#Binomial Distribution
x = random.binomial(n=10, p=0.5, size=10)
print(x)

#Poisson Distribution
x = random.poisson(lam=2, size=10)
print(x)

#Uniform Distribution
x = random.uniform(size=(2, 3))
print(x)

#Logistic Distribution
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)

#Multinomial Distribution
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)

#Exponential Distribution
x = random.exponential(scale=2, size=(2, 3))
print(x)

#Chi Square Distribution
x = random.chisquare(df=2, size=(2, 3))
print(x)

#Rayleigh Distribution
x = random.rayleigh(scale=2, size=(2, 3))
print(x)

#Pareto Distribution
x = random.pareto(a=2, size=(2, 3))
print(x)

#Zipf Distribution
x = random.zipf(a=2, size=(2, 3))
print(x)

