import numpy as np
import matplotlib.pyplot as plt
import scipy.special

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
    p = (lam**k/scipy.special.factorial(k))*np.exp(-lam)
    return p

def binomial_fit(x, p, n, k):
    p = ((np.math.factorial(n))/(np.math.factorial(k))*np.math.factorial(n-k))*(p**k)*((1-p)**(n-k))
    return p

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