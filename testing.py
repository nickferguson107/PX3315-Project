import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.close("all")

G = nx.Graph()

G.add_edges_from([('A', 'B'),('G','D')], weight=1)
G.add_edges_from([('D','A'),('B','D'),('D','E')], weight=3)
G.add_edges_from([('B','C'),('A','F')], weight=5)
G.add_edges_from([('C','G')], weight=7)
edges = G.edges()
weights = [G[u][v]['weight'] for u,v in edges]
pos=nx.spring_layout(G)
nx.draw(G, pos=pos, width=weights)
plt.savefig("simpledemo.png")
