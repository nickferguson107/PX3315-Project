import numpy as np
import random

class RandomGraph():

    def __init__(self, nodes):
        self.node_number = nodes
    
    def poisson_distribution(self, k):
        p = np.random.poisson(k, size=self.node_number)
        return p+1
    
    def adjacency_matrix(self, nodes, p):
        am = np.zeros((nodes, nodes))    # Create blank matrix
        nodes = list(range(nodes))    # List of node numbers (0, 1, ..., max)
        node_pairs = []    # Will become list of node pairs
        for i in range(len(p)):    # For each value of Poisson sample...
            for j in range(p[i]):    # Take that value, and for that many times...
                origin_node = nodes[i]    # Get a random node
                while(1):
                    chosen_node = random.choice(nodes)    # Choose another node at random
                    if chosen_node != origin_node:    # Check they're not the same
                        break               
                node_pairs.append([j, chosen_node])    # Connect nodes, add to list of node pairs
                am[origin_node, chosen_node] = int(1)    # Add connection to adjaceny matrix
                am[chosen_node, origin_node] = int(1)
        np.savetxt("am.csv", am, fmt='%i', delimiter='\t')
        return am

    def check_symmetry(self, nodes, am):
        for i in range(nodes):
            for j in range(nodes):
                if am[i,j] != am[j,i]:
                    return(print("Not symmetric"))
                else:
                    return(print("Symmetric"))

if __name__ == '__main__':
    print(1+1)