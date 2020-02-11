import numpy as np
import random
from scipy.optimize import minimize 
import matplotlib.pyplot as plt

"""
    The data will have the form of a N × 2 array, inputs, 
    where each row contains the (x, y)- coordinates of a 
    datapoint. There is also a corresponding N × 1 array,
    targets, which contains the classes, i.e. the ti values,
    encoded as (−1 or 1).
    
    For classA, np.random.randn(10, 2) 
    creates a 10 x 2 numpy array with positive random
    values from univariate Gaussian distribution with
    mean 0 and variance 1. Furthertime, addition with
    [1.5, 0.5]-[-1.5, 0.5] just gives us a range between
    the random values. np.concatenate "Join a sequence of
    arrays along an existing axis.", in essence puts 
    them together. classB is now trivial to understand.
    inputs become a N x 2 array that puts classA 
    and classB together. targets is an array with
    values between -1 and 1 that describe if the
    values come from classA or classB.
    
    permute = list(range(N)) creates a list with
    1,2,3,4,5...., N-1, N. Shuffle permute and
    now inputs and targets are matches for random
    values from classA and classb.
    
"""
np.random.seed(100) #same values each iteration
cluster = 0.2
classA = np.concatenate ( 
        (np.random.randn(10, 2) * 3 + [1.5, 0.5],
         np.random.randn(10, 2) * 3+ [-1.5, 0.5])) 

classB = np.random.randn(20, 2) * cluster + [0.0 , -0.5]

inputs = np.concatenate ((classA , classB)) 
targets = np.concatenate (
    (np.ones(classA.shape[0]), 
     -np.ones(classB.shape[0])))

N = inputs.shape[0] # Number of rows (samples)
permute = list(range(N)) 
random.shuffle(permute) 
inputs = inputs[permute, :]
targets = targets[permute]
