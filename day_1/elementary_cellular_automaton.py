# ELEMENTARY CELLULAR AUTOMATON

import numpy as np
import matplotlib.pyplot as plt

# IDEAS
# RANDOM INTEGERS
x = np.random.randint(2, size=10)
# EMPTY MATRIX CREATION
nr, nc = 20, 10
X = np.zeros((nr, nc))  # ZERO MATRIX WITH nr ROWS and NC cols
# INTEGER TO BINARY ARRAY
R = 230  # INTEGER (RULE)
Rb = np.array(list(bin(230)[2:]))  # BINARY ARRAY (RULE)

# CELLULAR AUTOMATON
Nc = 300  # NUMBER OF CELLS
Nt = 300  # NUMBER OF TIME STEPS
c0 = np.random.randint(2, size=Nc)  # START VALUES
C = np.zeros((Nt, Nc), dtype=np.int8)  # CELLS
C[0] = c0
R = 126  # INTEGER (RULE)
# BINARY RULE
Rb = np.array(list(bin(R)[2:].zfill(8))).astype(np.int32)  # BINARY ARRAY (RULE)
# BINARY RULE ALTERATIVE
# Rb = np.array([1,0,1,0,1,1,1,1], dtype=np.int32  )

def apply_rule(c=0, r=0, l=0):
    case = int(f"{l}{c}{r}", 2)
    return Rb[-(case+1)]

# CELL SCANNING
for row in range(Nt-1):
    for cell in range(Nc):
        if cell == 0:
            l = 0
        else:
            l = C[row, cell-1]
        c = C[row, cell]
        if cell == (Nc -1):
            r = 0
        else:
            r = C[row, cell+1]
        C[row+1, cell] = apply_rule(l,c,r)    

plt.figure()
plt.imshow(C, cmap = "binary")
plt.show()