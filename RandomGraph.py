import numpy as np
import time, random, os, errno
import general
import matplotlib.pyplot as plt

class Node:
    """
    Creates node object with list of neighbouring nodes
    """
    def __init__(self, index):
        self.index = index
        self.neighbours = []

def random_network(n, p):
    """
    Creates random network

    Parameters
    ----------
    n : int
        The number of nodes in the network
    p : float
        The probability of connecting any two nodes

    Returns
    -------
    vertices : list
        A list of node objects in the network
    elapsed : float
        Time taken to create node in seconds
    """    
    start = time.perf_counter()
    vertices = [Node(i) for i in range(n)]
    edges = [(i,j) for i in range(n) for j in range(i) if random.random() < p]
    for (i,j) in edges:
        vertices[i].neighbours.append(vertices[j])
        vertices[j].neighbours.append(vertices[i])
    end = time.perf_counter()
    elapsed = end - start
    return vertices, elapsed

def time_creation(n_min, n_max, num, p, iternum):
    """
    Graph network creation time versus node number

    Parameters
    ----------
    n_min : int
        Start of node range
    n_max : int
        End of node range
    num : 
        Number of steps between n_min and n_max
    p : float
        Probability of connecting two nodes
    iternum: int
        Number of iterations for each graph

    Returns
    -------
    nodes : list
        List of node numbers being tested
    times : list
        Average creation time of networks
    """   

    nodes = np.linspace(n_min, n_max, num, dtype=int)
    _, ax = plt.subplots(1, 1)
    times = []
    for n in nodes:
        _, _, elapsed = multiple_networks(n, p, iternum)
        times.append(elapsed)
    ax.plot(nodes, times, linestyle='-', label="Time")
    ax.legend(loc='best')
    ax.set_xlabel(r"Node number")
    ax.set_ylabel(r"Creation time ($s$)")
    ax.grid()
    ax.ticklabel_format(axis='y', style='sci')
    plt.tight_layout()
    plt.savefig("{}-{}n_creationtime.png".format(n_min, n_max))

    return nodes, times

def degree_distribution(vertices, hist=True):
    """
    Return histogram of degree distribution for a supplied network

    Parameters
    ----------
    vertices : list
        List of the node objects in the network

    Returns
    -------
    plotx : ndarray, optional
        Array of x values to plot the histogram against
    hist : ndarray, optional
        Histogram of degrees in the network
    dist : ndarray, optional
        Array containing the degree for every node in the network
    """    
    dist = [len(vertices[i].neighbours) for i in range(len(vertices))]
    if hist:
        bins = np.linspace(0, len(vertices), len(vertices)+1)
        hist, _ = np.histogram(dist, bins=bins)
        plotx = np.linspace(0, len(vertices)-1, len(vertices))
        return plotx, hist
    else:
        return dist

def all_edges(vertices):
    """
    Finds all edges in the network denoted by (a,b) where a and b are   
    the two nodes the edge is connected to.

    Parameters
    ----------
    vertices : list
        List of the node objects in the network

    Returns
    -------
    alledges : list
        List of tuples of edges
    """
    alledges = []
    allneighbours = [i.neighbours for i in vertices]
    for j in range(len(allneighbours)):
        for k in allneighbours[j]:
            alledges.append((j, k))
    return alledges

def multiple_networks(n, p, i):
    """
    Calls random_network i times and averages degree distribution.

    Parameters
    ----------
    n : int
        The number of nodes in the network
    p : float
        The probability of connecting any two nodes
    i : int
        The number of networks to create

    Returns
    -------
    plotx : ndarray
        Array of x values to plot the histogram against
    average_hist : ndarray
        Degree distribution averaged over i networks
    average_time : float
        Average time taken for the creation of each network
    """    
    all_hists = np.zeros((i, n))
    all_times = np.zeros(i)
    for j in range(i):
        vertices, all_times[j] = random_network(n, p)
        all_hists[j], plotx = degree_distribution(vertices, hist=True)
    average_hist = np.mean(all_hists, axis=0)
    average_time = np.mean(all_times)
    return plotx, average_hist, average_time

def find_component(node, visited):
    """
    Performs depth-first search to find the component of node.

    Parameters
    ----------
    node : Node object
        A node in the network
    visited : set
        The set of all visited nodes

    """    
    for v in node.neighbours:
        if v not in visited:
            visited.add(v)
            find_component(v, visited)        

def get_all_components(vertices):
    """
    Finds all the components in the network.

    Parameters
    ----------
    vertices : list
        List of the node objects in the network

    Returns
    -------
    components : list
        List of all components in the network
    """    
    components = []
    all_visited = set()

    for v in vertices:
        if v not in all_visited:
            this_component = set([v])
            find_component(v, this_component)
            components.append(this_component)
            all_visited |= this_component

    # Check all nodes have been visited
    assert sum(len(c) for c in components) == len(vertices)
    return components


def largest_component_size(vertices):
    """
    Finds the size of the largest component in the network.

    Parameters
    ----------
    vertices : list
        List of the node objects in the network

    Returns
    -------
    s : int
        Size of the largest component in the network
    """    

    s = max(len(c) for c in get_all_components(vertices))
    return s


def graph_largest_component_size(n, ps):
    """
    Finds largest component for a range of networks

    Parameters
    ----------
    n : int
        The number of nodes in the network
    ps : list
        List of probabilities 

    Returns
    -------
    l : list
        List of largest components of the networks generated from ps
    """    

    l = [largest_component_size(random_network(n, p)) for p in ps]
    return l


def moving_average(a, n=3):
    """
    Creates moving average for graph

    Parameters
    ----------
    a : list
        List of numbers to average
    n : float

    Returns
    -------
    avg : ndarray
        Array of averages
    """    
    window = np.ones(n) / float(n)
    avg = np.convolve(a, window, 'same')
    return avg


def plot(nodes, filename, k_min=0.01, k_max=0.5, num=1000, avg_width=5):
    """
    Plots largest component size with a moving average for a range of k.

    Parameters
    ----------
    n : int
        The number of nodes in the network
    filename : str
        Filename of saved image
    k_min : float
        Start point of x range
    k_max : float
        End point of x range
    num : int
        Number of points to evaluate
    avg_width : int
        Width of moving average    

    Returns
    -------
    k : ndarray
        Array of k used in the graph
    y : ndarray
        Array of largest component sizes for k
    """    

    k = np.linspace(k_min, k_max, num=num)
    sizes = graph_largest_component_size(nodes, k/nodes)

    y = [s/nodes for s in sizes]
    avg = moving_average(y, avg_width)
    newk = np.linspace(k_min, k_max, num=len(avg))
    _, ax = plt.subplots()

    ax.plot(k, y, label="Component size")
    ax.plot(newk, avg, label="Average", lw=2)
    ax.set(xlabel = r"$k$",
           ylabel = r"$\frac{N_{G}}{N}$",
           xlim = [k[0], k[-1]],
           ylim = [0, 1]
    )  
    ax.grid()
    ax.legend(loc='best')
    plt.savefig("Graphs/{}.png".format(filename))
    return k, y

if __name__ == '__main__':
    if not os.path.exists('Graphs'):
        os.makedirs('Graphs')