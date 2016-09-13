import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Setmatplotlib rc params.
rc = {'lines.linewidth': 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}

sns.set(rc=rc)

# Load the food data.
xa_high = np.loadtxt('data/xa_high_food.csv', comments="#")
xa_low = np.loadtxt('data/xa_low_food.csv', comments="#")

#Make bin boundaries
low_min = np.min(xa_low)
low_max = np.max(xa_low)

high_min = np.min(xa_high)
high_max = np.min(xa_high)
global_min = np.min([low_min, high_min])
global_max = np.max([low_max, high_max])

bins = np.arange(global_min-50, global_max+50, 50)

#Plot data as a histogram
##_ = plt.hist((xa_low, xa_high), bins=bins)
##plt.xlabel('Cross-sectional area (um$^2$)')
##plt.ylabel('count')
##plt.show()


## Reset bins, since xa_low has smaller values
##bins = np.arange(1600, 2501, 50)

# Generate the histogram for the low-density fed mother
_ = plt.hist(xa_low, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)
_ = plt.hist(xa_high, normed=True, bins=bins, histtype='stepfilled', alpha=0.5)

# Add axis labels
plt.xlabel('Cross-sectional area (µm$^2$)')
plt.ylabel('count')

# Add a legend
plt.legend(('low', 'high'), loc='upper right')
