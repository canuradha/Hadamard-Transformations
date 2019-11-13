import numpy as np
import csv
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
import __future__


Mat5 = np.empty([5,16,16], dtype=int)

# ##### Reading from the data.csv file (contains 5 matrices)
with open("data.csv") as data:
    temp = csv.reader(data)
    mat_no = 0
    rowIndex = 0
    for index,line in enumerate(temp):
        if(line[0] == ''):
            mat_no += 1
            rowIndex = 0
        else:
            Mat5[mat_no][rowIndex] =  line
            rowIndex += 1

# ####### Converting the values from (-1,1) to (1,0)
Mat15 = np.empty([5,15,15], dtype=int)
mcount = 0
for mat in Mat5:
    Mat15[mcount] = mat[1:, 1:]
    mcount += 1


Mat15[Mat15 == 1] = 0
Mat15[Mat15 == -1] = 1



mcount = 1
for m in Mat15:
    G1 = nx.from_numpy_matrix(m)
    Gtst = nx.from_numpy_matrix(Mat15[1])
    plt.subplot(3,2,mcount)
    nx.draw(Gtst, pos=nx.circular_layout(Gtst), with_labels = True, node_size = 100, font_size=10)
    name = 'L15_'+ str(mcount)
    print('Graph ', name)
    print('No of Vertices: ', len(G1))
    print('No of Edges', G1.number_of_edges())
    print('Degree List: ', G1.degree())  
    mcount += 1

plt.show(Gtst)

