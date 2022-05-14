import experiment
import pandas as pd

n_array = [10, 50, 100, 500, 1000]
eps_array = [1, 1/3, 9/30, 8/30, 7/30, 6/30, 5/30, 4/30, 3/30, 2/30, 1/30]
D_array_n = [0.1, 0.5, 1, 1.5, 2]

df = pd.DataFrame(experiment.multi_experiment(n_array, eps_array, D_array_n, 100, save='data'))
df.to_csv('./data/data.csv')
