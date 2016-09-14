import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#Specify parameters

#Number of generations
n_gen = 16

# Chance of having beneficial mutation
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen - 1)

#Adaptive immunity: binomial distribution
ai_samples = np.random.binomial(n_cells, r, size=100000)

#Report mean and std
print ('AI mean:', np.mean(ai_samples))
print ('AI stdv:', np.std(ai_samples))
print ('AI Fano:', np.var(ai_samples) / np.mean(ai_samples))


#Function to draw out of random mutation hypothesis
def draw_random_mutation(n_gen, r):
    """Draw sample under random mutation hypothesis."""
    # Initialize number of mutations
    n_mut = 0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size=1):
    #Initialize samples
    samples = np.empty(size)

    #draw the samples
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples

def ecdf(data):
    """
    Compute x, y values for an empirical distribution
    function
    """
    x = np.sort(data)
    y = np.arange(1, 1+len(x)) /len(x)
    return x, y

x_ai, y_ai = ecdf(ai_samples)

rm_samples = sample_random_mutation(n_gen, r, size=100000)

x_rm, y_rm = ecdf(rm_samples)

plt.close()
plt.semilogx(x_ai, y_ai, linestyle='none', marker='.', color='red')
plt.semilogx(x_rm, y_rm, linestyle='none', marker='.', color='blue')
plt.legend(('adaptive', 'random'), loc = "lower right")
plt.margins(0.02)
plt.ylabel('ECDF')
plt.xlabel('Number of survivors')


#Report mean and std
print ('RM mean:', np.mean(rm_samples))
print ('RM stdv:', np.std(rm_samples))
print ('RM Fano:', np.var(rm_samples) / np.mean(rm_samples))
