import numpy as np
from scipy import optimize, stats, special

def get_distribution(am):
    degrees = [np.sum(row) for row in am]
    return degrees

def poisson_fit(k, lam):
    np.seterr(over='ignore', divide='ignore')
    p = stats.poisson.pmf(k, lam)
    return p

def binomial_fit(k, p, n):
    np.seterr(over='ignore', divide='ignore')
    p = stats.binom.pmf(k, n, p)
    return p

def fit(f, x, y, guess=[]):
    popt, _ = optimize.curve_fit(f, x, y, p0=guess)
    fit = f(x, *popt)
    return fit

def find_primary(filename):
    """
    Extract primary roads from file.

    Parameters
    ----------
    filename : path
        Source file

    Returns
    -------
    labels : list
        Column names
    """
    with open(filename, 'r') as f:
        data = f.readlines()
        labels = data[0].split('\t')
        new_filename = filename[0:-4] + '_primary.txt'
        with open(new_filename, 'w') as p:
            for i in data:
                attrs = i.split('\t')
                if attrs[10] == 'true':
                    p.write(i)
    return labels, new_filename

    
