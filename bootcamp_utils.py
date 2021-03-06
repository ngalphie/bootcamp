#bootcamp_utils: A collection of statistical function proved
#useful to 55 students
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def ecdf(data):
    """
    Compute x, y values for an empirical distribution
    function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) /len(x)
    return x, y


def bootstrap(data, func, size=1):
    """Function that draws bootstrap replicates
    Takes array of data, a function, size (default 1)
    Outputs the bs_replicates
    """
    #make empty array of replicates of the correct size
    bs_rep = np.empty(size)
    for i in range(size):
        bs_sample = np.random.choice(data, replace=True, size = len(data))
        bs_rep[i] = func(bs_sample)
    return bs_rep

def ci95(rep):
    """Function that takes in replicates and outputs the 95% confidence interval
    """
    return np.percentile(rep, [2.5, 97.5])

def cv(X):
    try:
        return np.std(X) / np.mean(X)
    except ZeroDivisionError:
        raise StatsError('mean is zero')
