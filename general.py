import numpy as np
import matplotlib.pyplot as plt

def get_distribution(am):
    degrees = [np.sum(row) for row in am]
    return degrees

def plot_distribution(degrees):
    fig, ax = plt.subplots(1, 1)
    bins = np.linspace(0, len(degrees), len(degrees)+1)
    x = np.linspace(1, len(degrees), len(degrees)+1)
    hist = np.histogram(degrees, bins=bins)
    ax.hist(degrees,
            bins=bins,
            histtype='step',
            rwidth=1,
            label='Degree')
    ax.set_xlim(left=min(degrees)-10,
                right=max(degrees)+10)
    ax.set_xlabel("Degrees")
    ax.set_ylabel("Frequency")
    ax.set_title("Degree distribution")
    ax.legend(loc='best')
    ax.grid()
    plt.savefig("Degree distribution.png")
    return hist, x