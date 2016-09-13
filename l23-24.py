import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import seaborn as sns

rc = {'lines.linewidth': 2, 'axes.labelsize' : 18,
        'axes.titlesize' : 18}
sns.set(rc=rc)

data_txt = np.loadtxt('data/collins_switch.csv', skiprows=2, delimiter=',')

#Slice out iptg and gfp
iptg = data_txt[:, 0]
gfp = data_txt[:, 1]
sem = data_txt[:, 2]

# # Plot ipgt vs gfp
# plt.close()
# plt.semilogx(iptg, gfp, marker='.', markersize=20,
#              linestyle='none')
# plt.ylim(-0.02, 1.02)
# plt.xlim(8e-4, 15)
# plt.title('IPTG Titration - semilog X')
# plt.xlabel('IPTG (mM)')
# plt.ylabel('Normalized GFP')
# plt.show()

# Plot ipgt vs gfp
plt.close()
plt.errorbar(iptg, gfp, yerr=sem, marker='.',
             markersize=20, linestyle='none')
plt.ylim(-0.02, 1.1)
plt.xlim(8e-4, 15)
plt.title('IPTG Titration - semilog X')
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.xscale('log')
plt.show()
