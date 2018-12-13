import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.close("all")
n = 1000
kmin = 0.5
kmax = 5

pmin = kmin/n
pmax = kmax/n

#RandomGraph.plot(n, kmin, kmax, 1000, 'test1000', windowSize=20)

n = 100
k = 0.2
p = k/n

graph = RandomGraph.randomGraph(100, p)
neighbs, edges = RandomGraph.all_edges(graph)

G = nx.Graph()
G.add_edges_from(edges)
nx.draw(G, node_size=50)
plt.savefig("n100k02.png")