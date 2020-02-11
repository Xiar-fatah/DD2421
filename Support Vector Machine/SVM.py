import numpy as np
from scipy.optimize import minimize 
import matplotlib.pyplot as plt
import data
import Kernels
# Import the random values from data, see explanation in data.py
inputs = data.inputs
targets = data.targets
N = data.N
# From the file Kernel import wanted kernel:
# in_ker, pol_ker or RBF_ker,
# see explanation in Kernel.py
kernel = Kernels.lin_ker

"""
    Define a function which implements equation (4).
    objective is the Lagrange function that will be
    minimized.
"""
def objective(alpha):
    L =   1/2 * np.dot(alpha, np.dot(alpha, P)) - np.sum(alpha)
    return L

"""
    This function should implement the equality constraint of (10)
    in the section Adding Slack Variables that allows a few datapoints
    to be miss-classified. The contraint is 
    0 <= alpha_i <= C for all i and the sum alpha_i * t_i = 0 <- given by
    the derivation of the Lagrange.
    
    zerofun is used in XC and called in minimize
    where zerofun is a function you have defined
    which calculates the value which should be
    constrained to zero. Like objective, zerofun
    takes a vector as argument and returns a scalar value.
"""
def zerofun(alpha):
    return np.dot(alpha,targets)

"""
    Calculate the b value using equation (7).
    Note that you must use a point on the margin. This corresponds to a
    point with an α-value larger than zero, but less than C (if slack is used).
"""
def b_cal():
    b = 0
    for value in nonzero:
        b += value[0] * value[2] * kernel(value[1], nonzero[0][1])
    return b - nonzero[0][2]

"""
    This is the indicator according to equation (6)
"""
def ind(x,y,b):
    summ = 0
    for value in nonzero:
        summ += value[0] * value[2] * kernel([x, y], value[1])
    return summ - b


"""
    P = t_i * t_j * Kernel(i,j) is a matrix, that
    is a part of the Lagrange function. It is 
    precomputed globally because it is called many times
    t_i and t_j are the targets and varies between -1 and 1
    depending if the data is from classA or classB.
"""

P = np.zeros((N,N))
for i in range(0,len(P)):
    for j in range(0,len(P)):
        P[i][j] = targets[i] * targets[j]* kernel(inputs[i],inputs[j])
        
"""
    ret = minimize( objective , start , bounds=B, constraints=XC )
    alpha = ret['x'], Will find the vector alpha which minimizes
    the function objective within the bounds B and the constraints XC.
    The explanation of objective can be found in the beginning of this
    document and start is a vector with the initial guess of the alpha vector
    
    B is a list of pairs of the same length as the alpha -vector, stating the lower
    and upper bounds for the corresponding element in alpha. To constrain the alpha
    values to be in the range 0 ≤ alpha ≤ C, we can set bounds=[(0, C) for b in range(N)].
"""
C = 100
B = [(0, C) for b in range(N)]
XC = {'type':'eq', 'fun':zerofun}
start = np.zeros(N) 
bounds=[(0, C) for b in range(N)] 
ret = minimize(objective, start, bounds = B, constraints = XC )
"""
    Make the call to minimize as indicated in the code sample above. 
    Note that minimize returns a dictionary data structure; this is why we must
    must use the string 'x' as an index to pick out the actual alpha values.
    There are other useful indices that you can use; in particular,
    the index 'success' holds a boolean value which is True if the optimizer
    actually found a solution.
"""
if (not ret['success']): 
    raise ValueError('Cannot find optimizing solution')
alpha = ret['x']

"""
    If the data is well separated, only a few of the alpha values will be non-zero.
    Since we are dealing with floating point values, however, those that are
    supposed to be zero will in reality only be approximately zero. Therefore,
    use a low threshold (10−5 should work fine) to determine 
    which are to be regarded as non-zero
"""
nonzero = [(alpha[i], inputs[i], targets[i]) for i in range(N) if abs(alpha[i]) > 10e-5]
        
        
        
        
b = b_cal()        
        

############# Plot the results #############
xgrid = np.linspace(-5, 5) 
ygrid= np.linspace(-4, 4)
grid = np.array([[ind(x, y,b) for x in xgrid ] for y in ygrid])
plt.contour (xgrid , ygrid , grid , (-1.0, 0.0, 1.0),
colors=('red', 'black', 'blue'), linewidths=(1, 3, 1))
        
        
            
            
            
            