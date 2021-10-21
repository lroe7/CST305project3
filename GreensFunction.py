# Lauren Roe
# CST-305
# This is my work

# This program finds the solution to two second order ODEs using odeint and greens function
# It plots the solutions to the two equations on the same graph to compare methods of finding the solutions

import math                             # import math to do e^x and cos for the equations
import numpy as np                      # import the numpy library to use np.log and np.linespace
import matplotlib.pyplot as plt         # imported to be able to plot the results of both odeint and python
from scipy.integrate import odeint      # imported to find the true y values


def eq1(U, x):                                  # defines the first equation
    return [U[1], (-2 * U[1]) + (2 * x) - 2]    # returns the second order DE


def eq2(U, x):                  # defines the second equation
    return [U[1], 4 - U[0]]     # returns the second order DE


# returns the green's function equation found by hand
def greens1(x):                                                             # defines the green's function
    return 0.5 * (x * x) - (1.5 * x) + 0.75 - (0.75 * math.exp(-2 * x))     # returns the first equation


# returns the green's function equation found by hand
def greens2(x):                         # defines the green's function
    return 4 - (4 * math.cos(x))        # returns the second equation


# finding the solution to the  first ODE
U0 =[0, 0]                              # initial values of U
xs = np.linspace(0, 10, 101)            # creates values for x in increments of 0.1
Ux = odeint(eq1, U0, xs)                # stores the solution for the DE
ys = Ux[:,0]                            # stores the solution found above into y values to plot

# finding the solution to the second ODE
Ux2 = odeint(eq2, U0, xs)               # solution for the ODE
ys2 = Ux2[:,0]                          # stores the solution found above into y values to plot

# plotting the solution to the green's function first equation

gy1 = []            # stores the greens function y values for the first equation
gy2 = []            # stores the greens function y values for the second equation

for i in range (0, 101):
    x = xs[i]                   # changes x by the values in xs
    gy1.append(greens1(x))      # calculates and adds the y value using the greens function equation
    gy2.append(greens2(x))      # calculates and adds the y value using the greens function equation


# plotting the first equation
plt.plot(xs, gy1, 'g--', linewidth=2, label='greens function')  # plots the greens function
plt.plot(xs, ys, 'b:', linewidth=2, label='odeint solution')    # plots the odeint solution
plt.legend()                                                    # plots the legend on the graph
plt.xlabel('x')                                                 # labels x axis
plt.ylabel('y')                                                 # labels y axis
plt.title('d2y/dx2 + dy/dx +2 = 2x')                            # titles the graph the equation being solved
plt.show()                                                      # displays graph

plt.plot(xs, gy2, 'g--', linewidth=2, label='greens funtion')   #plots the greens function
plt.plot(xs, ys2, 'b:', linewidth=2, label='odeint solution')   # plots the odeint solution
plt.legend()                                                    # plots the legend on the graph
plt.xlabel('x')                                                 # labels x axis
plt.ylabel('y')                                                 # labels y axis
plt.title('d2y/dx2 + y = 4')                                    # titles the graph the equation being solved
plt.show()                                                      # displays graph

