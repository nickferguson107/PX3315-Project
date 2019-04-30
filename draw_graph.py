import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
G.add_edges_from([(0,1), (1,3), (2,4), (3,4), (0,5), (0,3), (2,5)])
nx.draw(G, node_size=500, width=10)
plt.savefig("Graphs/demo.png")