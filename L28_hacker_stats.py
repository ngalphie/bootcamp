import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

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

def ecdf(data):
    return np.sort(data), np.arange(1,len(data)+1) / len(data)

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')


plt.close()
for i in range(1000):
    bs_sample = np.random.choice(bd_1975, replace=True, size = len(bd_1975))
    x, y = ecdf(bs_sample)
    plt.plot(x, y, marker='.', linestyle='none', color='blue', alpha=0.01)
    # plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
    plt.xlabel('beak dpeth (mm)')
    plt.ylabel('ECDF')
    # plt.legend(('1975', '1975 bs'), loc="lower right")
    plt.margins(0.02)
