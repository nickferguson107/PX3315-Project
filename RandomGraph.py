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

def random_network(n, p):
    start = time.perf_counter()
    vertices = [Node(i) for i in range(n)]
    edges = [(i,j) for i in range(n) for j in range(i) if random.random() < p]
    for (i,j) in edges:
      vertices[i].neighbours.append(vertices[j])
      vertices[j].neighbours.append(vertices[i])
    end = time.perf_counter()
    elapsed = end - start
    return vertices, elapsed

def degree_distribution(vertices, hist=True):
    dist = [len(vertices[i].neighbours) for i in range(len(vertices))]
    if hist:
        bins = np.linspace(0, len(vertices), len(vertices)+1)
        hist, _ = np.histogram(dist, bins=bins)
        plotx = np.linspace(0, len(vertices)-1, len(vertices))
        return plotx, hist
    else:
        return dist

def multiple_networks(n, p, iterations):
    all_hists = np.zeros((iterations, n))
    all_times = np.zeros(iterations)
    for i in range(iterations):
        vertices, all_times[i] = random_network(n, p)
        all_hists[i], plotx = degree_distribution(vertices, hist=True)
    average_hist = np.mean(all_hists, axis=0)
    average_time = np.mean(all_times)
    return plotx, average_hist, average_time

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
   return [(p, sizeOfLargestComponent(random_network(n, p))) for p in theRange]


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