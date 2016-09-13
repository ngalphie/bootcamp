import numpy as np
import scipy.special as ss
import matplotlib.pyplot as plt
import seaborn as sns

#generate a array of x values
x = np.linspace(-15, 15, 400)

#Compute the normalized intensity
norm_I = 4 * (ss.j1(x) / x)**2

#Plot our computation
plt.close()
plt.plot(x, norm_I, marker='.', linestyle='none')
plt.margins(0.02)
plt.xlabel('$x$')
plt.ylabel('$I(x) / I_0$')

#Processing the spike data.
data = np.loadtxt('data/retina_spikes.csv', skiprows=2, delimiter=',')
t = data[:,0]
V = data[:,1]

#Close all other plots just incase
plt.close()
plt.plot(t, V)
plt.xlabel('t (ms)')
plt.ylabel('V (uV)')
plt.xlim(1395, 1400)
