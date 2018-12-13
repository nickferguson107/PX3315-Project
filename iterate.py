import RandomGraph
import matplotlib.pyplot as plt
import general
import numpy as np
import time

np.seterr(over='ignore', divide='ignore')

def iterate_prob(nodes, iternum, prange=[0.001, 0.01], pnum=20):
    x = np.linspace(0, nodes-1, nodes)
    probs = np.linspace(prange[0], prange[1], pnum)
    p_resids = np.zeros(pnum)
    b_resids = np.zeros(pnum)
    print("Starting {} iterations...".format(iternum*pnum))
    start_time = time.perf_counter()
    for p in range(len(probs)):
        print("Starting probability p = {:.3f} iterations...".format(probs[p]))
        dist = RandomGraph.multiple_graphs(nodes, probs[p], iternum)
        p_fit = general.fit(general.poisson_fit, x, dist, guess=[probs[p]*nodes])
        b_fit = general.fit(general.binomial_fit, x, dist, guess=[probs[p], nodes])
    
        p_resids[p] = np.absolute(np.sum(np.nan_to_num(dist-(p_fit*nodes))))
        b_resids[p] = np.absolute(np.sum(np.nan_to_num(dist-(b_fit*nodes))))
        print("Finished probability p = {:.3f} iterations.".format(probs[p]))
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    print("Finished {} iterations. Time taken {}s.".format(iternum*pnum, elapsed))

    return x, probs, p_resids, b_resids

def iterate_n(meandeg, iternum, nodenums=[100, 1000]):
    p = [meandeg/i for i in nodenums]
    dists = np.zeros((len(nodenums), nodenums[-1]))
    for n in range(len(nodenums)):
        dists = RandomGraph.multiple_graphs(n, p, iternum)
    return dists

nodes = 1000
iternum = 100
threshold = 0.0025
p_lims = [0.002, 0.02]
p_num = 10

x, probs, p_resids, b_resids = iterate_prob(nodes, iternum, prange=p_lims, pnum=p_num)

fig, ax = plt.subplots(1, 1)
ax.plot(probs, p_resids, label="Poisson residuals")
ax.plot(probs, b_resids, label="Binomial residuals")
ax.set_xlabel("Degree")
ax.set_ylabel("Residual sum")
ax.set_title("Residuals versus p for different fits")
ax.grid()
ax.legend()
plt.savefig("fit_comparison.png")
