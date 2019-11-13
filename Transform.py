import numpy as np
import csv
import matplotlib.pyplot as plt
import networkx as nx
import __future__


Mat5 = np.empty([5,5], dtype=int)

with open("data3.csv") as data:
    temp = csv.reader(data)
    mat_no = 0
    rowIndex = 0
    for index,line in enumerate(temp):
        if(line[0] == ''):
            mat_no += 1
            rowIndex = 0
        else:
            Mat5[rowIndex] =  line
            rowIndex += 1




##### key #########
# r -> 0 - 4            c + r -> 25 - 29
# ra -> 5- 9            c + ra -> 30 - 34
# rb -> 10 - 14         c + rb -> 35 - 39
# rc -> 15-19           c + rc -> 40 - 44
# rd -> 20 - 24         c + rd -> 45 - 49
##################

# #### transforming the matrix into 50x50 matrix

Lres = np.zeros([50 ,50], dtype = int)    
r = 0
ra = 5
rb = 10
rc = 15
rd = 20
for row in Mat5:
        c = 25
        for val in row:
            if val == 1:
                Lres[r][c] = 1
                Lres[c][r] = 1
                Lres[r + ra][c + ra] = 1
                Lres[c + ra][r + ra] = 1
                Lres[r + rb][c + rb] = 1
                Lres[c + rb][r + rb] = 1
                Lres[r + rc][c + rc] = 1
                Lres[c + rc][r + rc] = 1
                Lres[r + rd][c + rd] = 1
                Lres[c + rd][r + rd] = 1

            elif val == 2:
                Lres[r][c + ra] = 1
                Lres[c + ra][r] = 1
                Lres[r + ra][c + rb] = 1
                Lres[c + rb][r + ra] = 1
                Lres[r + rb][c + rc] = 1
                Lres[c + rc][r + rb] = 1
                Lres[r + rc][c + rd] = 1
                Lres[c + rd][r + rc] = 1
                Lres[r + rd][c] = 1
                Lres[c][r + rd] = 1
            elif val == 3:
                Lres[r][c + rb] = 1
                Lres[c + rb][r] = 1
                Lres[r + ra][c + rc] = 1
                Lres[c + rc][r + ra] = 1
                Lres[r + rb][c + rd] = 1
                Lres[c + rd][r + rb] = 1
                Lres[r + rc][c] = 1
                Lres[c][r + rc] = 1
                Lres[r + rd][c + ra] = 1
                Lres[c + ra][r + rd] = 1
            elif val == 4:
                Lres[r][c + rc] = 1
                Lres[c + rc][r] = 1
                Lres[r + ra][c + rd] = 1
                Lres[c + rd][r + ra] = 1
                Lres[r + rb][c] = 1
                Lres[c][r + rb] = 1
                Lres[r + rc][c + ra] = 1
                Lres[c + ra][r + rc] = 1
                Lres[r + rd][c + rb] = 1
                Lres[c + rb][r + rd] = 1
            elif val == 5:
                Lres[r][c + rd] = 1
                Lres[c + rd][r] = 1
                Lres[r + ra][c] = 1
                Lres[c][r + ra] = 1
                Lres[r + rb][c + ra] = 1
                Lres[c + ra][r + rb] = 1
                Lres[r + rc][c + rb] = 1
                Lres[c + rb][r + rc] = 1
                Lres[r + rd][c + rc] = 1
                Lres[c + rc][r + rd] = 1
            c += 1
        r += 1


Gtst = nx.from_numpy_matrix(Lres)

nx.draw(Gtst, pos=nx.circular_layout(Gtst), with_labels = True, node_size = 100, font_size=10)
# nx.draw(Gtst, pos=nx.spectral_layout(Gtst), with_labels = True, node_size = 100, font_size=10)


plt.show(Gtst)

# #### Save the created matrix to a file

# f = open("adjency.txt", "w")
# cn = 1
# for Mat in Mat5:
    # f.write("Graph" + str(cn) + "\n" + str(Mat) + "\n")
    # cn += 1
