# CSV GENERATOR
# Generates CSV data with noise
import numpy as np
import pandas as pd
import os

datadir = "data"
if not os.path.exists(datadir):
    os.mkdir(datadir)

a = 3
b = 5

def func(x, a, b):
    return b * np.cos(a * x) * x**2 

x = np.linspace(0., 10., 1000)
y = func(x, a, b)

Num_file = 20
for n in range(Num_file):
    print("GENERATING FILE #{0}".format(n))
    noise = np.random.normal(scale = 20, size=y.size)
    yn = y + noise
    data = pd.DataFrame()
    data["x"] = x
    data["y"] = yn
    data.to_csv("data/data_{0}.csv".format(n))
    
