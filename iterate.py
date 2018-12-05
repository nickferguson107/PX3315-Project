import RandomGraph
import general

nodes = int(input("Give number of nodes in graph: "))
threshold = float(input("Set connection threshold: "))
iterations = int(input("Set number of iterations: "))

graph = RandomGraph.RandomGraph(nodes)

averaged_degrees = graph.many_graphs(iterations, nodes, threshold)
hist, x = general.plot_distribution(averaged_degrees)
input("Press Enter to exit.")