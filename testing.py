import RandomGraph
import general

nodes = int(input("Give number of nodes in graph: "))
threshold = float(input("Set connection threshold: "))
iterations = int(input("Set number of iterations: "))

graph = RandomGraph.RandomGraph(nodes)
<<<<<<< HEAD

#matrix = graph.randomgraph(nodes, threshold)
averaged_degrees = graph.many_graphs(iterations, nodes, threshold)
hist, x = general.plot_distribution(averaged_degrees)
input("Press Enter to exit.")
=======
p = graph.poisson_distribution(mean_degree)
matrix = graph.adjacency_matrix(nodes, p, print_status=False)
sym = graph.check_symmetry(nodes, matrix)
print(sym)
input()
>>>>>>> dd5610d6a077212a0a776402669e321cfebebb56
