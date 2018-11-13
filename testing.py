import numpy as np
import matplotlib.pyplot as plt
import random

class RandomGraph():

    def __init__(self, nodes):
        self.node_number = nodes
    
    def poisson_distribution(self, mean_degree):
        p = np.random.poisson(mean_degree, size=self.node_number)
        return p+1
    
    def adjacency_matrix(self, nodes, p):
        am = np.zeros((nodes, nodes))
        node_list = [i for i in list(range(nodes))]
        for i in range(nodes):
            nodes_to_connect = random.sample(node_list, p[i])
            print(nodes_to_connect)
            for j in nodes_to_connect:
                am[i,j], am[j,i] = int(1)
        np.savetxt("am.csv", am, fmt='%i', delimiter='\t')
        return am

    def connected_nodes(self, am):
        node_dict = {i : [] for i in range(len(am[0:,0]))}
        for i in range(nodes):
            for j in range(nodes):
                if am[i,j] == 1:
                    node_dict[i].append(j)
        return node_dict

nodes = 10
mean_deg = 1
a = RandomGraph(nodes)
b = a.poisson_distribution(mean_deg)
c = a.adjacency_matrix(nodes, b)
d = a.connected_nodes(c)
print(b)
print(c)
print(d)
mean_test = [len(i) for i in d.values()]
print(np.mean(mean_test))