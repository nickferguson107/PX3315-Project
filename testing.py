import RandomGraph

nodes = 12
mean_degree = 2

graph = RandomGraph.RandomGraph(nodes)

p = graph.poisson_distribution(mean_degree)

matrix = graph.adjacency_matrix(nodes, p)