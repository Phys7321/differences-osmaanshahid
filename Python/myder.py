# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:50:22 2018

@author: Tom K
edited by: Osmaan S
"""

# Define the function f(x)
def f(x):
    return x**2

# Define forward difference method for derivative, f'(x)
# over the interval [a,b] for N points
# N is
# h is

def forwardiff(f,a,b,N):
    h = (b-a)/N
    y_prime=[]
    for k in range(1,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h
        y_prime.append(slop)
    return y_prime
    
def backwardiff(f,a,b,N):
    h = (b-a)/N
    y_prime=[]
    for k in range(0,N-1):
        slop = (f(a+(k+1)*h)-f(a+k*h))/h
        y_prime.append(slop)
    return y_prime

def centraldiff(f,a,b,N):
    h = (b-a)/N
    g=[]
    for k in range(0,N):
        slop = (f(a+(k+1/2)*h)-f(a+(k-1/2)*h))/h
        g.append(slop)
    return array(g)