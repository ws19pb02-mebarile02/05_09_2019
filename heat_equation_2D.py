"""
heat_equation_2D.py

This is the first version of a file that solves the 2D heat equation.
It was copied almost exactly from my Mathematica program and is inefficient.
The next step is to make the code more efficient using list comprehensions and
consolidating some of the loops to eliminate unnecessary computations.

The rectangle in the plane has vertices at (0,0), (100,0), (100,200) and
(0,200). The initial condition has 20 degrees along the x-axis from 0 to 100
and 0 everywhere else in the rectangle.  The boundary conditions fix
20 degrees along the x-axis from 0 to 100, and 0 degrees along the remaining
three boundaries.  The output produces a 3D scatter plot after twenty seconds.
It takes a while to run.  To produce a scatter plot for a shorter time
interval, see the for loop below next to the comment: # change this argument to
adjust time steps.  
"""


import sys
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


"""
I copied the rightRotate code from the following location:
https://www.geeksforgeeks.org/python-program-right-rotate-list-n/
"""

def rightRotate(lists, num): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(lists) - num, len(lists)): 
        output_list.append(lists[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(lists) - num):  
        output_list.append(lists[item]) 
          
    return output_list

L = 101 # number of x-coordinates
M = 101 # number of y-coordinates

a = 0.  # x interval
b = 100.

c = 0.  # y interval
d = 200.

deltax = (b-a)/(L-1)  # size of x steps
deltay = (d-c)/(M-1)  # size of y steps
alpha = 40   
deltat = 1./100  # size of time steps
lamb1 = alpha*deltat/(deltax*deltax)
lamb2 = alpha*deltat/(deltay*deltay)

xvec = []   #x-coordinates
for i in range(1, L+1):
    xvec.append((i-1)*deltax)

yvec = []    #y-coordinates
for i in range(1, M+1):
    yvec.append((i-1)*deltay)

grid = []   #grid of points in plane
for i in range(len(xvec)):
    for j in range(len(yvec)):
        grid.append([xvec[i],yvec[j]])


linCombRow = []

for i in range(1, L*M+1):
    if i == 2 or i == 2*M + 2:
        linCombRow.append(lamb1)
    elif i == M + 1 or i == M + 3:
        linCombRow.append(lamb2)
    elif i == M + 2:
        linCombRow.append(1-2*(lamb1 + lamb2))
    else:
        linCombRow.append(0)

       
A = []   # calculating A matrix
irow = []
for i in range(1, L*M + 1):
    if i <= M+1 or i > L*M - (M-1):
        for j in range(1, L*M + 1):
            if j == i:
                irow.append(1)
            else:
                irow.append(0)
    else:
        if i%M == 0 or i%M == 1:
            for h in range(1, L*M + 1):
                if h == i:
                    irow.append(1)
                else:
                    irow.append(0)
    
        else:
            irow = rightRotate(linCombRow, i-(M+2))
    A.append(irow)
    irow = []


uvec = []  # initial state vector

for i in range(1, L*M + 1):
    if i % M == 1:
        uvec.append(20.)
    else:
        uvec.append(0)



A = np.array(A)
uvec = np.array(uvec)
grid = np.array(grid)

for i in range(2000):   # change this argument to adjust time steps
    unew = A.dot(uvec)
    uvec = unew

xgrid = []
ygrid = []
for i in range(len(grid)):
    xgrid.append(grid[i][0])
    ygrid.append(grid[i][1])

xgrid = np.array(xgrid)
ygrid = np.array(ygrid)


"""
I got info on 3D scatter plot from:
https://www.youtube.com/watch?v=6ljHxJQ47Uk
"""

fig = plt.figure()   
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(xgrid, ygrid, uvec, s=.5, c = 'r', marker = 'o')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('temperature at t = 20 s')

plt.show()

sys.exit(0)




