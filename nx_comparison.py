import networkx as nx
import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt

def nx_giant_component(nodes, p):

    G = nx.erdos_renyi_graph(nodes, p)
    c = len(max(nx.connected_component_subgraphs(G), key=len))

    return c

def nx_giant_component_range(nodes, p_range):

    sizes = [nx_giant_component(nodes, p) for p in p_range]

    return sizes

def plot_nx_components(nodes, filename="auto", k_min=0.1, k_max=5, num=1000, avg_width=5):

    k = np.linspace(k_min, k_max, num=num)

    if filename == "auto":
        filename = "n={}, k=({},{})".format(nodes, k_min, k_max)

    sizes = nx_giant_component_range(nodes, k/nodes)

    y = [s/nodes for s in sizes]
    avg = RandomGraph.moving_average(y, avg_width)
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
    plt.savefig("Graphs/nx_{}.png".format(filename))
    np.savetxt("Results/nx_{}.txt".format(filename),
                np.transpose(np.vstack((k, y, avg))),
                delimiter='\t')
    return k, y


a, b = plot_nx_components(1000, 'test')
