import numpy as np
# This is how we import the module of Matplotlib we'll be using
import matplotlib.pyplot as plt

# Some pretty Seaborn settings
import seaborn as sns
rc={'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

alpha = 1
beta = 0.2
delta = 0.3
gamma = 0.8
delta_t = 0.001
t = np.arange(0, 60, delta_t)

# Make an array to store the number of r and foxes
r = np.empty_like(t)
f = np.empty_like(t)

#initial conditions

r[0] = 10
f[0] = 1


# Write a for loop to keep updating n as time goes on
for i in range(1, len(t)):
    r[i] = r[i-1] + delta_t * (alpha*r[i-1] - beta*r[i-1]*f[i-1])
    f[i] = f[i-1] + delta_t * (delta*f[i-1]*r[i-1] - gamma*f[i-1])

plt.close()
plt.plot(t, r)
plt.plot(t, f)
plt.legend(('Rabbit', 'Fox'), loc="lower right")
plt.margins(0.02)
plt.xlabel('time')
plt.ylabel('number')
