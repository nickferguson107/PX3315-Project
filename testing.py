import numpy as np
import matplotlib.pyplot as plt

class RandomGraph():

    def __init__(self, nodes):
        self.node_number = nodes
        self.node_dict = {i: '' for i in range(nodes)}
    
    def poisson_distribution(self):
        p = np.random.poisson(1, size=self.node_number)
        return p

nodes = 100
a = RandomGraph(nodes)
b = a.poisson_distribution()
print(b)