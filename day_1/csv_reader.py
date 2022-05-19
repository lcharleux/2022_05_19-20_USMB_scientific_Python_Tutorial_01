# CSV READER
# Reads csv files and plots them
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

datadir = "data/"
files = os.listdir(datadir)
data = []
for file in files:
    if file.endswith(".csv"):
        d = pd.read_csv(datadir + file,
        header =0, index_col=0)
        file_num = int(file.split(".")[0].split("_")[1])
        d["file"] = file_num
        data.append(d)

data = pd.concat(data, ignore_index = True)

from scipy import optimize
# CURVE FITTING
def func(x, a, b):
    return b * np.cos(a * x) * x**2 
opt, cov = optimize.curve_fit(func, 
    data.x, 
    data.y, 
    p0 = [3.2,4])
aopt, bopt = opt # OPTIMAL VALUES OF a AND b
x = data[data.file == 0].x

plt.figure()
plt.scatter(data.x, data.y, s = 1)
plt.plot(x, func(x, aopt, bopt), "r-")
plt.show()    



