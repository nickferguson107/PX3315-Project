import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
from scipy.optimize import curve_fit

nodes = 1000
threshold = 0.003

graph = RandomGraph.RandomGraph(nodes)

matrix, time = graph.randomgraph(nodes, threshold, save=True)
dist = general.get_distribution(matrix)

x = np.linspace(0, nodes-1, nodes)
plot_x = np.linspace(0, nodes-1, 100*nodes)

p_guess1 = [threshold*nodes]
popt1, pcov1 = curve_fit(general.poisson_fit, x, dist, p0=p_guess1)
p_guess2 = [threshold, nodes]
popt2, pcov2 = curve_fit(general.binomial_fit, x, dist)


_, ax1 = plt.subplots(1, 1)
ax1.grid()
bins = np.linspace(0, len(dist), len(dist)+1)
hist = np.histogram(dist, bins=bins)
ax1.hist(dist,
        bins=bins,
        histtype='step',
        rwidth=1,
        label='Degree',
        linewidth=2,
        zorder=10,
        align='mid')
ax1.plot(plot_x, general.poisson_fit(plot_x, *popt1)*nodes)
ax1.plot(plot_x, general.binomial_fit(plot_x, *popt2)*nodes)
ax1.set_xlim(left=min(dist),
            right=max(dist))
ax1.set_xlabel("Degree")
ax1.set_ylabel("Frequency")
ax1.set_title("Degree distribution")
ax1.legend(loc='best')
plt.show()
