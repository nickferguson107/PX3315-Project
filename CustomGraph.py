import general
import matplotlib.pyplot as plt

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
    
    def add_node(self, name):
        index = self.size
        self.vertices.append(Node(index+1, name))

    def add_edge(self, node1, node2):
        self.vertices[node1].neighbours.append(self.vertices[node2])
        self.vertices[node2].neighbours.append(self.vertices[node1])