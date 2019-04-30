import RandomGraph
import general
import numpy as np
import matplotlib.pyplot as plt

def fit_and_average_dd(n, p, i, method, filename="auto"):

    if filename == "auto":
        filename = "dd_fitted n={}, p={}, i={}".format(n, p, i)
    x, hist = RandomGraph.multiple_networks(n, p, i)
    if method == "binomial":
        fit = general.binomial_fit(x, p, n)
    elif method == "poisson":
        fit = general.poisson_fit(x, n*p)
    else: 
        raise TypeError("Invalid fitting method. Choose 'binomial' or 'poisson'.")
    np.savetxt("Results/{}.txt".format(filename), np.transpose(np.vstack((x, hist/n, fit))), delimiter='\t')

def average_dd(n, p, i, filename="auto"):

    if filename == "auto":
        filename = "dd n={}, p={}, i={}".format(n, p, i)
    x, hist = RandomGraph.multiple_networks(n, p, i)
    print(sum(hist))
    np.savetxt("Results/{}.txt".format(filename), np.transpose(np.vstack((x, hist/n))), delimiter='\t')

average_dd(1000, 0.05, 100)
average_dd(1000, 0.1, 100)
average_dd(1000, 0.175, 100)
average_dd(1000, 0.25, 100)
average_dd(1000, 0.375, 100)
average_dd(1000, 0.5, 100)