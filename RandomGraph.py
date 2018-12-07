import numpy as np
import random
import time
import general

class RandomGraph():

    def __init__(self, nodes):
        self.node_number = nodes
    
    def poisson_distribution(self, k):
        while(1):
            p = np.random.poisson(k, size=self.node_number)
            if np.sum(p+1)%2 == 0:
                break
        return p+1

    def mean_degree(self, nodes, threshold):
        z = threshold*(nodes-1)
        return z
    
    def randomgraph(self, nodes, threshold, save=False):
        dist = np.random.uniform(size=nodes**2)
        p = np.reshape(dist, (nodes, nodes))
        am = np.zeros((nodes, nodes))
        start_time = time.perf_counter()
        for i in range(nodes):
            for j in range(nodes):
                if p[i,j] < threshold/2 and i!=j:
                    am[i,j] = int(1)
                    am[j,i] = int(1)
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        print("Finished creating network. Time taken: {:.3g}s".format(time_elapsed))
        if save:
            np.savetxt("am.csv", am, fmt='%i', delimiter='\t')
        return am, time_elapsed
    
    def many_graphs(self, number_of_iterations, nodes, threshold):
        all_distributions = np.zeros((number_of_iterations, nodes))
        average_degrees = np.zeros(nodes)
        times = []
        start_time = time.perf_counter()
        for i in range(number_of_iterations):
            print("Creating graph {}...".format(i+1))
            am, singlegraphtime = self.randomgraph(nodes, threshold)
            times.append(singlegraphtime)
            degrees = general.get_distribution(am)
            all_distributions[i] = degrees
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time
        avg_time = np.mean(times)
        print("Finished iterations. Time taken: {:.3g}s, average time {:.3g}s".format(time_elapsed, avg_time))
        average_degrees = np.sum(all_distributions, axis=0)
        return average_degrees

    def predetermined(self, nodes, p, print_status=False):
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