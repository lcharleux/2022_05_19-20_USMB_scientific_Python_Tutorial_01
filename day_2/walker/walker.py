import os
import pandas as pd

datadir = "./data/"

data = {"file":[], "aaa":[]}
for root, dirs, files in os.walk(datadir):
    print(f"{root}; {dirs}; {files}")
    for file in files:
        if file.endswith(".txt"):
            lines = open(root + "/" +file).readlines()
            for line in lines:
                words = [w.strip() for w in line.split(":")]
                if words[0] == "aaa":
                    data["file"].append(file)
                    data["aaa"].append(float(words[1]))

data = pd.DataFrame(data)                    