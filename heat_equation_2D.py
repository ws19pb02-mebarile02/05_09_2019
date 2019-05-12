"""
heat_equation_2D.py



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

def rightRotate(lists, num):
    "Cut the deck."
    n = len(lists) - num
    return lists[n:] + lists[:n]

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

xvec = [round(deltax*i, 2) for i in range(L)] # x-coordinates
yvec = [round(deltay*i, 2) for i in range(M)] # y-coordinates

#grid of points in plane
grid = [[xvec[i],yvec[j]] for i in range(len(xvec)) for j in range(len(yvec))]

"""
note 1-2*(lamb1 + lamb2) evaluates to zero in this case,
but keep code anyway
"""

linCombRow = L*M*[0]
linCombRow[1] = lamb1
linCombRow[2*M + 1] = lamb1
linCombRow[M] = lamb2
linCombRow[M+2] = lamb2
linCombRow[M+1] = 1-2*(lamb1 + lamb2)

       
A = []   # calculating A matrix

for i in range(L*M):
    if i > M - 1 and i <= L*M - M-1 and (i + 1) % M >= 2:
        irow = rightRotate(linCombRow, i - (M+1))
    else:
        irow = [0] * (L * M)
        irow[i] = 1

    A.append(irow)
    

# initial state vector
uvec = L*M*[0]
for i in range(0,L*M,M):
    uvec[i] = 20
    
 
A = np.array(A)
uvec = np.array(uvec)

nt = 2000
for i in range(nt):   # change this argument to adjust time steps
    uvec = A.dot(uvec)

xgrid = np.array([grid[i][0] for i in range(len(grid))])
ygrid = np.array([grid[i][1] for i in range(len(grid))])

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




