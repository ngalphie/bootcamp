import numpy as np

# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

def fold_change(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Function that computes the theoretical fold change"""
    #Check if the inputs are the correct format--RK must be scalar and c can be array or scalar
    fc = 0
    fc = np.power(1 + (RK)*np.square(1+c/KdA)/(np.square(1+c/KdA)+Kswitch*np.square(1+c/KdI)),-1)
    return fc

def bohr_parameter(c, RK,  KdA=0.017, KdI=0.002, Kswitch=5.8):
    """Function that computes the Bohr parameter"""
    bp = 0
    bp = -np.log(RK)-np.log(np.square(1+c/KdA)/(np.square(1+c/KdA)+Kswitch*np.square(1+c/KdI)))
    return bp

def fold_change_bohr(bohr_parameter):
    """Compute the fold change of bohr parameter"""
    fc = 0
    fc = 1/(1+np.exp(-1*bohr_parameter))
    return fc


#Read data properly into arraynp.e
wt_lac = np.loadtxt('data/wt_lac.csv', skiprows=3, delimiter=',', comments="#")
q18m_lac = np.loadtxt('data/q18m_lac.csv', skiprows=3, delimiter=',', comments="#")
q18a_lac = np.loadtxt('data/q18a_lac.csv', skiprows=3, delimiter=',', comments="#")

#Slice data into iptg and fc
wt_lac_iptg = wt_lac[:,0]
wt_lac_fc = wt_lac[:,1]


q18m_lac_iptg = q18m_lac[:,0]
q18m_lac_fc = q18m_lac[:,1]

q18a_lac_iptg = q18a_lac[:,0]
q18a_lac_fc = q18a_lac[:,1]

# #Plot the data in semilog
plt.close()
# plt.semilogx(wt_lac_iptg, wt_lac_fc, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.semilogx(q18m_lac_iptg, q18m_lac_fc, marker='.', linestyle='none', markersize=20, alpha=0.5)
# plt.semilogx(q18a_lac_iptg, q18a_lac_fc, marker='.', linestyle='none',markersize=20, alpha=0.5)


# #Compute the theoretical fold change
# theoretical_iptg = np.logspace(-6,2,500)
# wt_lac_fct = fold_change(theoretical_iptg, 141.5)
# q18m_lac_fct = fold_change(theoretical_iptg, 1332)
# q18a_lac_fct = fold_change(theoretical_iptg, 16.56)
# plt.semilogx(theoretical_iptg, wt_lac_fct, alpha=0.5)
# plt.semilogx(theoretical_iptg, q18m_lac_fct, alpha=0.5)
# plt.semilogx(theoretical_iptg, q18a_lac_fct, alpha=0.5)

plt.plot(np.linspace(-6,6,50), fold_change_bohr(np.linspace(-6,6,50)), color = 'gray' )
plt.plot(bohr_parameter(wt_lac_iptg, 141.5), wt_lac_fc, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(bohr_parameter(q18m_lac_iptg, 1332), q18m_lac_fc, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.plot(bohr_parameter(q18a_lac_iptg, 16.56), q18a_lac_fc, marker='.', linestyle='none', markersize=20, alpha=0.5)

plt.margins(0.02)
plt.xlabel('Bohr Parameter')
plt.ylabel('fold change')
plt.legend(('theoretical', 'WT', 'Q18M', 'Q18A'), loc='center right')
# plt.ylim(0, 1.1)
# plt.xlim(5e-6, 50)




plt.savefig('IPTG.pdf', bbox_inches='tight')
