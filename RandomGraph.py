import numpy as np
import random

class RandomGraph():

    def __init__(self, nodes):
        self.node_number = nodes
    
    def poisson_distribution(self, k):
        while(1):
            p = np.random.poisson(k, size=self.node_number)
            if np.sum(p+1)%2 == 0:
                break
        return p+1
    
    def adjacency_matrix(self, nodes, p, print_status=False):
        for i in p:
            if i < nodes:
                break
            return ValueError('Degree higher than number of nodes.')     
        am = np.zeros((nodes, nodes))    # Create blank matrix
        nodes = list(range(nodes))    # List of node numbers (0, 1, ..., max)
        node_pairs = []    # Will become list of node pairs
        while(np.sum(p)>0):
            for i in range(len(p)):
                #print('Current degree distribution: {}'.format(p))
                if p[i] == 0: continue
                if print_status: print('Starting node: {}.'.format(i))
                origin_node = nodes[i]
                while(1):
                    connection_node = random.choice(nodes)
                    if print_status: print('Attempting to connect node {} to node {}...'.format(origin_node, connection_node))
                    if p[connection_node] == 0:
                        if print_status: print('Connection node invalid: node already full.')
                        continue
                    if connection_node != origin_node:
                        break
                    if print_status: print('Connection node invalid: can\'t connect node to itself.')
                node_pairs.append([origin_node, connection_node])    # Connect nodes, add to list of node pairs
                am[origin_node, connection_node] += int(1)    # Add connection to adjaceny matrix
                am[connection_node, origin_node] += int(1)
                if print_status: print('Connection {} to {} made successfully.'.format(origin_node, connection_node))
                #print(am)
                p[i] = p[i]-1
                p[connection_node] = p[connection_node]-1
                #print('Updated degree distribution: {}'.format(p))
                if np.sum(p) == 0:
                    if print_status: print('All nodes filled.')
                    break
        np.savetxt("am.csv", am, fmt='%i', delimiter='\t')
        return am

    def check_symmetry(self, nodes, am):
        if type(am) == ValueError:
            result = 'Invalid adjacency matrix.'
            return result
        else:
            for i in range(nodes):
                for j in range(nodes):
                        if am[i,j] == am[j,i]:
                            result = 'Adjacency matrix is symmetrical.'
                        else:
                            result = 'Adjacency matrix is not symmetrical.'
            return result

if __name__ == '__main__':
    print(1+1)