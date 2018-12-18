import numpy as np
from scipy import optimize, stats, special

def get_distribution(am):
    degrees = [np.sum(row) for row in am]
    return degrees

def poisson_fit(k, lam):
    np.seterr(over='ignore', divide='ignore')
    p = (lam**k/special.factorial(k))*np.exp(-lam)
    return p

def binomial_fit(k, p, n):
    np.seterr(over='ignore', divide='ignore')
    p = stats.binom.pmf(k, n, p)
    return p

def fit(f, x, y, guess=[]):
    popt, _ = optimize.curve_fit(f, x, y, p0=guess)
    fit = f(x, *popt)
    return fit