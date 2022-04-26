import experiment
import pandas as pd

n_array = [1000]
eps_array = [1/3, 1/6, 1/9, 1/12, 1/15, 1/18, 1/21, 1/24, 1/27, 1/30]
k_array_n = [0.1, 0.5, 1, 1.5, 2]

df = pd.DataFrame(experiment.multi_experiment(n_array, eps_array, k_array_n, 100, save=True))
df.to_csv('./results_exp.csv')
