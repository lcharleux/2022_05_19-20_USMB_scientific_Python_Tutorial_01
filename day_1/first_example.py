# FIRST EXAMPLE: PLOT A FUNCTION
import matplotlib.pyplot as plt
import numpy as np
# 1: DEFINE A GRID
#x = np.array([0., 1., 2.])
x = np.linspace(0., 10., 1001) # Evenly spaced points

def func(x):
    return np.sin(x)*x 

y = func(x)   
plt.figure()
plt.xlabel("Time $x$")
plt.ylabel("Amplitude, $y$")
plt.grid()
plt.title("A nice figure")
plt.plot(x,y)
plt.savefig("figure.png")
#plt.show()