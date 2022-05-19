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
        data.append(d)

plt.figure()
for d in data:
    plt.scatter(d.x, d.y, s = 2)
plt.show()    


