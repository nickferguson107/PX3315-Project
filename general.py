import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import scipy.stats
from scipy.optimize import curve_fit, OptimizeWarning
from inspect import signature

def get_distribution(am):
    degrees = [np.sum(row) for row in am]
    return degrees

def edge_number(am):
    m = np.sum(am)
    if m%2 != 0:
        return ValueError("Odd number of edges.")
    else:
        return int(m/2)

def poisson_fit(k, lam):
    np.seterr(over='ignore', divide='ignore')
    p = (lam**k/scipy.special.factorial(k))*np.exp(-lam)
    return p

def binomial_fit(k, p, n):
    np.seterr(over='ignore', divide='ignore')
    p = scipy.stats.binom.pmf(k, n, p)
    return p

def fit(f, x, y, guess=[]):
    popt, _ = curve_fit(f, x, y, p0=guess)
    fit = f(x, *popt)
    return fit

def plot_distribution(degrees):
    _, ax = plt.subplots(1, 1)
    ax.grid()
    bins = np.linspace(0, len(degrees), len(degrees)+1)
    x = np.linspace(1, len(degrees), len(degrees)+1)
    hist = np.histogram(degrees, bins=bins)
    ax.hist(degrees,
            bins=bins,
            histtype='step',
            rwidth=1,
            label='Degree',
            linewidth=2,
            zorder=10)
    ax.set_xlim(left=min(degrees),
                right=max(degrees))
    ax.set_xlabel("Degrees")
    ax.set_ylabel("Frequency")
    ax.set_title("Degree distribution")
    ax.legend(loc='best')
    plt.savefig("Degree distribution.png")
    return hist, x