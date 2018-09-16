# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:50:22 2018

@author: Tom K
edited by: Osmaan S
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return x**2

# Define forward difference method for derivative, f'(x)
# over the interval [a,b] for N points
# h is spacing between each point

def forwardiff(f,a,b,N):
    h = (b-a)/N
    forward_prime=[]                       # Empty list, will become f'(x)
    xaxis = np.linspace(a,b,num=(N-1))     # x-axis
    for k in range(1,N):
        slop = (f(a+k*h)-f(a+(k-1)*h))/h   # Calculate derivative at each point
        forward_prime.append(slop)         # At each point, add f'(x) to list
    # print(forward_prime)
    # print(xaxis.tolist())
    plt.plot(xaxis.tolist(),forward_prime) # Plot on xy-axes
    plt.show()
    
def backwardiff(f,a,b,N):
    h = (b-a)/N
    backward_prime=[]                       # Empty list, will become f'(x)
    xaxis = np.linspace(a,b,num=(N-1))      # x-axis
    for k in range(0,N-1):
        slop = (f(a+(k+1)*h)-f(a+k*h))/h    # Calculate derivative at each point
        backward_prime.append(slop)         # At each point, add f'(x) to list
    # print(backward_prime)
    # print(xaxis.tolist())
    plt.plot(xaxis.tolist(),backward_prime) # Plot on xy-axes
    plt.show()

def centraldiff(f,a,b,N):
    h = (b-a)/N
    central_prime=[]                              # Empty list, will become f'(x)
    xaxis = np.linspace(a,b,num=N)                # x-axis
    for k in range(0,N):
        slop = (f(a+(k+1/2)*h)-f(a+(k-1/2)*h))/h  # Calculate derivative at each point
        central_prime.append(slop)                # At each point, add f'(x) to list
    # print(central_prime)
    # print(xaxis.tolist())
    plt.plot(xaxis.tolist(),central_prime)        # Plot on xy-axes
    plt.show()

def secondiff(f,a,b,N):
    h = (b-a)/N
    second_prime=[]                               # Empty list, will become f''(x)
    xaxis = np.linspace(a,b,num=N)                # x-axis 
    for k in range(0,N):
        slop = (f(a+(k+1)*h) + f(a+(k-1)*h) - 2*f(a+k*h) )/(h**2)   # Calculate derivative at each point
        second_prime.append(slop)                 # At each point, add f''(x) to list
    print(second_prime)
    # print(xaxis.tolist()
    plt.plot(xaxis.tolist(),second_prime)         # Plot on xy-axes
    plt.show()