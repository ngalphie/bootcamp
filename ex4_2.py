'''
Exercise 4.2: Hacker stats on bee sperm data
Neonicotinoid pesticides are thought to have inadvertent effects on service-providing insects such as bees. A recent study of this was recently featured in the New York Times. The original paper is Straub, et al., Proc. Royal Soc. B 283(1835): 20160506. Straub and coworkers put their data in the Dryad repository, which means we can work with it!
(Do you see a trend here? If you want people to think deeply about your results, explore them, learn from them, in general further science with them, make your data publicly available. Strongly encourage the members of your lab to do the same.)
We will look at the weight of drones (male bees) using the data set stored in ~/git/bootcamp/data/bee_weight.csv and the sperm quality of drone bees using the data set stored in ~/git/bootcamp/data/bee_sperm.csv.
a) Load the drone weight data in as a Pandas DataFrame.
b) Plot ECDFs of the drone weight for control and also for those exposed to pesticide. Do you think there is a clear difference?
c) Compute the mean drone weight for control and those exposed to pesticide. Compute 95% bootstrap confidence intervals on the mean.
d) Repeat parts (a)-(c) for drone sperm. Use the 'Quality' column as your measure. This is defined as the percent of sperm that are alive in a 500 µL sample.
e) As you have seen in your analysis in part (d), both the control and pesticide treatments have some outliers with very low sperm quality. This can tug heavily on the mean. So, get 95% bootstrap confidence intervals for the median sperm quality of the two treatments.
'''

import pandas as pd
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
    """Function that takes in data and outputs the 95% confidence interval
    """
    return np.percentile(rep, [2.5, 97.5])

def cv(X):
    try:
        return np.std(X) / np.mean(X)
    except ZeroDivisionError:
        raise StatsError('mean is zero')

b_sperm = pd.read_csv('data/bee_sperm.csv', delimiter=',', comment='#').dropna()

b_weight = pd.read_csv('data/bee_weight.csv', delimiter=',', comment='#').dropna()

plt.close()
plt.clf()
x1_con,y1_con = ecdf(b_weight.loc[b_weight['Treatment']=='Control', 'Weight'])
x1_pes,y1_pes = ecdf(b_weight.loc[b_weight['Treatment']=='Pesticide', 'Weight'])


# bs_sample = np.random.choice(bd_1975, replace=True, size = len(bd_1975))
# x, y = ecdf(bs_sample)
plt.plot(x1_con, y1_con, marker='.', linestyle='none', alpha=0.5)
plt.plot(x1_pes, y1_pes, marker='.', linestyle='none', alpha=0.5)
# # plt.plot(x_1975_bs, y_1975_bs, marker='.', linestyle='none')
plt.xlabel('Weight')
plt.ylabel('ECDF')
plt.legend(('Control', 'Pesticide'), loc="lower right")
plt.margins(0.02)
plt.savefig('Control_vs_Pesticide_Sperm_Bee_Weight.pdf')

mean_weight_control = np.mean(b_weight.loc[b_weight['Treatment']=='Control', 'Weight'])
mean_weight_pesticide = np.mean(b_weight.loc[b_weight['Treatment']=='Pesticide', 'Weight'])

print('Mean weight of control equals: ', mean_weight_control)
print('Mean weight of pesticide equals: ', mean_weight_pesticide)

ci95_weight_control = ci95(n(b_weight.loc[b_weight['Treatment']=='Control', 'Weight']))
ci95_weight_pesticide = ci95(np.mean(b_weight.loc[b_weight['Treatment']=='Pesticide', 'Weight']))

print('Mean weight of control confidence intervals equals: ', ci95_weight_control)
print('Mean weight of pesticide confidence intervals equals: ', ci95_weight_pesticide)
