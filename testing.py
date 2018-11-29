import RandomGraph

nodes = int(input("Give number of nodes in graph: "))
mean_degree = int(input("Give mean degree of nodes: "))

graph = RandomGraph.RandomGraph(nodes)
p = graph.poisson_distribution(mean_degree)
matrix = graph.adjacency_matrix(nodes, p, print_status=False)
sym = graph.check_symmetry(nodes, matrix)
print(sym)
input()