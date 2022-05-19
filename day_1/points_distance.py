# DISTANCE BETWEEN POINTS
from types import DynamicClassAttribute
import numpy as np
import matplotlib.pyplot as plt

Npoints = 3
points = np.random.rand(Npoints, 2)

if False:
    plt.figure()
    #x, y = points.T # ANOTHER OPTION
    x = points[:,0]
    y = points[:,1]
    plt.scatter(x,y)
    plt.show()

def calc_distance(points):
    Npoints = len(points)
    D = np.zeros((Npoints, Npoints))
    for i in range(Npoints):
        for j in range(Npoints):
            P = points[i]
            Q = points[j]
            xp, yp = P
            xq, yq = Q
            d = np.sqrt((xp-xq)**2 + (yp-yq)**2 )
            D[i, j] = d
    return D        

def calc_distance_numpy(points):
    x, y = points.T
    N = len(points)
    Dx = x.reshape(1,N) - x.reshape(N,1)
    Dy = y.reshape(1,N) - y.reshape(N,1) 
    D = np.sqrt(Dx**2 + Dy**2)
    return D

import math, numba
@numba.njit
def calc_distance_numba(points, D):
    Npoints = len(points)
    for i in range(Npoints):
        for j in range(Npoints):
            D[i,j] = math.sqrt((points[i,0]-points[j,0])**2 + (points[i,1]-points[j,1])**2 )
            
    return D        

big_points = np.random.rand(200, 2)
Npoints2 = len(big_points)
big_D = np.zeros((Npoints2, Npoints2))
D0 = calc_distance(big_points)    
D1 = calc_distance_numpy(big_points)
D2 = calc_distance_numba(big_points, big_D)


