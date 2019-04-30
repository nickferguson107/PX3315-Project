import general
import numpy as np

class Node:
    """
    Creates node object with list of neighbouring nodes
    """
    def __init__(self, index, name):
        self.index = index
        self.neighbours = []
        self.name = name

    def __repr__(self):
        return repr(self.name)

class CustomGraph:

    def __init__(self, nodes):
        self.vertices = [Node(i, str(i)) for i in range(nodes)]
        self.size = len(self.vertices)
    
    def __repr__(self):
        return repr(self.vertices)
    
    def matrix(self):
        self.am = np.empty((self.size, self.size), dtype = dict)
        return self.am

    def add_node(self, name):
        index = self.size
        self.vertices.append(Node(index+1, name))

    def add_edge(self, node1, node2, name, length):
        if len(self.am) == 0:
            a = 1
        np.column_stack((self.am, np.empty(self.size, dtype=dict)))
        np.row_stack((self.am, np.empty(self.size, dtype=dict)))
        self.vertices[node1].neighbours.append(self.vertices[node2])
        self.vertices[node2].neighbours.append(self.vertices[node1])
        self.am[node1, node2] = dict(ident = name, length = length)
        self.am[node2, node1] = dict(ident = name, length = length)