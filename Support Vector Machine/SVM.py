import numpy as np
from scipy.optimize import minimize 
import matplotlib.pyplot as plt
import random
#Returns “scalar product-like” similarity measure of two vectors
def lin_ker(i,j):
    lin_ker = np.dot(i,j) #Linear kernel
    return lin_ker
def pol_ker(i,j):
    p = 1
    pol_ker = pow((np.dot(i,j)+1),p)  #Polynomial kernel
    return pol_ker

def RBF_ker(i,j):
    sigma = 1
    RBF_don = 2*pow(sigma,2)
    RBF_ker = pow(np.e,-pow(np.linalg(i-j),2)/RBF_don) #Radial Basis Function kernel
    return RBF_ker

def objective(alpha):
    L =   1/2 * np.dot(alpha, np.dot(alpha, P)) - np.sum(alpha)
    return L

def zerofun(alpha):
    return np.dot(alpha,targets)

def b_cal():
    b = 0
    for value in nonzero:
        b += value[0] * value[2] * lin_ker(value[1], nonzero[0][1])
    return b - nonzero[0][2]
def ind(x,y,b):
    summ = 0
    for value in nonzero:
        summ += value[0] * value[2] * lin_ker([x, y], value[1])
    return summ - b

np.random.seed(100) #same values each iteration

classA = np.concatenate ( 
        (np.random.randn(10, 2) * 0.2 + [1.5, 0.5],
         np.random.randn(10, 2) * 0.2 + [-1.5, 0.5])) 
classB = np.random.randn(20, 2) * 0.2 + [0.0 , -0.5]

inputs = np.concatenate ((classA , classB)) 
targets = np.concatenate (
    (np.ones(classA.shape[0]), 
     -np.ones(classB.shape[0])))

N = inputs.shape[0] # Number of rows (samples)
permute = list(range(N)) 
random.shuffle(permute) 
inputs = inputs[permute, :]
targets = targets[permute]

#Note that P is a NxN matrix
#P is t_i * t_j * Kernel(i,j) and precomputed globally
P = np.zeros((N,N))
for i in range(0,len(P)):
    for j in range(0,len(P)):
        P[i][j] = targets[i] * targets[j]* lin_ker(inputs[i],inputs[j])
C = 100

B = [(0, C) for b in range(N)]
XC = {'type':'eq', 'fun':zerofun}

start = np.zeros(N) #Initial guess 
bounds=[(0, C) for b in range(N)] #Constraints alpha to be 0 <= alpha <= C
ret = minimize(objective, start, bounds = B, constraints = XC )
if (not ret['success']): # The string 'success' instead holds a boolean representing if the optimizer has found a solution
    raise ValueError('Cannot find optimizing solution')
alpha = ret['x']
nonzero = [(alpha[i], inputs[i], targets[i]) for i in range(N) if abs(alpha[i]) > 10e-5]
        
        
        
        
b = b_cal()        
        
        
xgrid = np.linspace(-5, 5) 
ygrid= np.linspace(-4, 4)
grid = np.array([[ind(x, y,b) for x in xgrid ] for y in ygrid])
plt.contour (xgrid , ygrid , grid , (-1.0, 0.0, 1.0),
colors=('red', 'black', 'blue'), linewidths=(1, 3, 1))
        
        
            
            
            
            