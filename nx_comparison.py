from networkx import erdos_renyi_graph, connected_component_subgraphs
import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt

def nx_giant_component(nodes, p):

    G = erdos_renyi_graph(nodes, p)
    c = len(max(connected_component_subgraphs(G), key=len))

    return c

def nx_giant_component_range(nodes, p_range):

    sizes = [nx_giant_component(nodes, p) for p in p_range]

    return sizes

def plot_nx_components(nodes, filename="auto", k_min=0, k_max=7.5, k_iters=1500, save=False):

    k = np.linspace(k_min, k_max, num=k_iters)

    if filename == "auto":
        filename = "n={}, k=({},{})".format(nodes, k_min, k_max)

    sizes = nx_giant_component_range(nodes, k/nodes)

    y = [s/nodes for s in sizes]
    _, ax = plt.subplots()

    ax.plot(k, y, label="Component size")
    ax.set(xlabel = r"$k$",
           ylabel = r"$\frac{N_{G}}{N}$",
           xlim = [k[0], k[-1]],
           ylim = [0, 1]
    )  
    ax.grid()
    ax.legend(loc='best')
    if save:
        plt.savefig("Graphs/nx_{}.png".format(filename))
        np.savetxt("Results/nx_{}.txt".format(filename),
                    np.transpose(np.vstack((k, y))),
                    delimiter='\t')
    return k, y

def multiplot(num, nodes, k_min, k_max):

    all_arrays = np.empty((nodes, num))
    filename = "n={}, k=({},{}), {} averaged".format(nodes, k_min, k_max, num)

    for i in range(num):
        print("Beginning iteration {}...".format(i))
        _, all_arrays[:,i] = plot_nx_components(nodes, k_min = k_min, k_max = k_max, k_iters=nodes)
        print("Finished iteration {}.".format(i))


    averaged = np.mean(all_arrays, axis=1)

    np.savetxt("Results/nx_{}.txt".format(filename), averaged, delimiter='\t')

    return averaged




a, b = plot_nx_components(1000, 'test')
