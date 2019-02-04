import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

network, _ = RandomGraph.random_network(100, 0.02)
edges = RandomGraph.all_edges(network)

G = nx.Graph()
G.add_edges_from(edges)
nx.draw(G, node_size=50)
plt.show()