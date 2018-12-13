import numpy as np
import random
import time
import general
import matplotlib.pyplot as plt

class Node:
   def __init__(self, index):
      self.index = index
      self.neighbours = []

   def __repr__(self):
      return repr(self.index)

def randomGraph(n,p):
   vertices = [Node(i) for i in range(n)]
   edges = [(i,j) for i in range(n) for j in range(i) if random.random() < p]

   for (i,j) in edges:
      vertices[i].neighbours.append(vertices[j])
      vertices[j].neighbours.append(vertices[i])

   return vertices

def degree_distribution(vertices, hist=True):
    dist = [len(vertices[i].neighbours) for i in range(len(vertices))]
    if hist:
        bins = np.np.linspace(0, len(vertices), len(vertices)+1)
        hist, _ = np.histogram(dist, bins=bins)
        return hist
    else:
        return dist

def multiple_graphs(n, p, iterations):
    all_hists = np.zeros((iterations, n))
    for i in range(iterations):
        if i%10 == 0:
            print("{:.3g} percent complete".format((i/iterations)*100))
        vertices = randomGraph(n, p)
        all_hists[i] = degree_distribution(vertices, hist=True)
    average_hist = np.mean(all_hists, axis=0)
    return average_hist

def dfsComponent(node, visited):
   for v in node.neighbours:
      if v not in visited:
         visited.add(v)
         dfsComponent(v, visited)


def connectedComponents(vertices):
   components = []
   cumulativeVisited = set()

   for v in vertices:
      if v not in cumulativeVisited:
        componentVisited = set([v])
        dfsComponent(v, componentVisited)

        components.append(componentVisited)
        cumulativeVisited |= componentVisited

   assert sum(len(c) for c in components) == len(vertices)
   return components


def sizeOfLargestComponent(vertices):
   return max(len(c) for c in connectedComponents(vertices))


def graphLargestComponentSize(n, theRange):
   return [(p, sizeOfLargestComponent(randomGraph(n, p))) for p in theRange]


def movingAverage(a, n=3):
    window = np.ones(n) / float(n)
    return np.convolve(a, window, 'same')


def plot(numVertices, xstart, xend, xpts, filename, windowSize=5):
   plt.clf() # clear figure

   xs = np.linspace(xstart, xend, num=xpts)
   data = graphLargestComponentSize(numVertices, xs/numVertices)

   ys = [p[1]/numVertices for p in data]
   movingavg = movingAverage(ys, windowSize)
   newxs = np.linspace(xstart, xend, num=len(movingavg))

   plt.plot(xs, ys, label="Component size")
   plt.plot(newxs, movingavg, label="Average", lw=2)
   plt.xlabel(r"$k$")
   plt.ylabel(r"$\frac{N_{G}}{N}$")
   plt.ylim((0, 1))
   plt.xlim((xs[0], xs[-1]))
   plt.grid()
   plt.legend()
   plt.savefig(filename)

def all_edges(vertices):
    alledges = []
    allneighbours = [i.neighbours for i in vertices]
    for j in range(len(allneighbours)):
        for k in allneighbours[j]:
            alledges.append((j, k))
    return allneighbours, alledges

def many_graphs(self, number_of_iterations, nodes, threshold):
    hists = np.zeros((number_of_iterations, nodes))
    times = []
    start_time = time.perf_counter()
    bins = np.np.linspace(0, nodes, nodes+1)
    for i in range(number_of_iterations):
        print("Creating network {}...".format(i+1))
        am, singlegraphtime = self.randomgraph(nodes, threshold)
        times.append(singlegraphtime)
        degrees = general.get_distribution(am)
        hists[i], _ = np.histogram(degrees, bins=bins)
    end_time = time.perf_counter()
    time_elapsed = end_time - start_time
    avg_time = np.mean(times)
    print("Finished iterations. Time taken: {:.3g}s, average time {:.3g}s".format(time_elapsed, avg_time))
    average_hist = np.mean(hists, axis=0)
    return average_hist