import numpy as np
"""
    lin_ker, pol_ker and RBF_ker returns “scalar product-like”
    similarity measure of two vectors which is needed to minimize
    the lagrange.
"""
def lin_ker(i,j):
    lin_ker = np.dot(i,j) #Linear kernel
    return lin_ker
def pol_ker(i,j):
    p = 2
    pol_ker = pow((np.dot(i,j)+1),p)  #Polynomial kernel
    return pol_ker

def RBF_ker(i,j):
    sigma = 2
    RBF_don = 2*pow(sigma,2)
    RBF_ker = pow(np.e,-pow(np.linalg.norm(i-j),2)/RBF_don) #Radial Basis Function kernel
    return RBF_ker
