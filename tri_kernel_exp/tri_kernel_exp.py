import experiment
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Experiment data
n_array = [1000]
eps_array = [1, 1/3, 1/6, 1/9, 1/12, 1/15, 1/18, 1/21, 1/24, 1/27, 1/30]
k_array_n = [0.1, 0.5, 1, 1.5, 2]

df = pd.DataFrame(experiment.multi_experiment(n_array, eps_array, k_array_n, 100, save=True))
df.to_csv('./results_exp1.csv')


# Plot
data_file = "results_exp1.csv"
df = pd.read_csv('results_exp1.csv')

df[np.logical_and(df['k']==1000, df['eps']<1)].round(decimals=2).groupby('eps').mean().plot(y=['kernel_size', 'nc_diag_prekernel', 'theoretic_kernel_size'], figsize=(20, 10))
plt.xticks(range(len(eps_array)), eps_array)
plt.gca().invert_xaxis()
plt.savefig('eps.png')
