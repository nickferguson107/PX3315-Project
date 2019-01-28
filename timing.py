import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

plt.close("all")

min_node = 50
max_node = 100
node_step = 50
iternum = 1
p = 0.05

nodes = np.arange(min_node, max_node, node_step, dtype=int)

fig, ax = plt.subplots(1, 1)

times = []

for n in nodes:
    _, _, elapsed = RandomGraph.multiple_networks(n, p, iternum)
    times.append(elapsed)

'''
ax.plot(nodes, times, linestyle='-', marker='x', label="Time".format(n))
ax.legend(loc='best')
ax.set_xlabel(r"Node number")
ax.set_ylabel(r"Creation time ($s$)")
ax.grid()
plt.savefig("timecomparison.png")
'''
#fig, ax = plt.subplots(1, 1)
ax.plot(nodes, times/nodes,
        linestyle='-',
        marker='x',
        label="Time")
ax.ticklabel_format(style='sci')
ax.legend(loc='best')
ax.set_xlabel(r"Node number")
ax.set_ylabel(r"Creation time ($s$)")
ax.grid()
plt.tight_layout()
plt.savefig("timecomparisonovern.png")
