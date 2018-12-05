import RandomGraph
import general

nodes = 100
threshold = 0.05

graph = RandomGraph.RandomGraph(nodes)

matrix, time = graph.randomgraph(nodes, threshold, save=True)
degrees = general.get_distribution(matrix)
mean_degree = graph.mean_degree(nodes, threshold)
print(mean_degree)
hist, x = general.plot_distribution(degrees)