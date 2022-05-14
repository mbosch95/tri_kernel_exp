import pandas as pd
import triangulation as tri
import itertools
import copy


def experiment(sample_size, n, eps, D=None):
    """Given a sample size, the size of the triangulation n, the number of flips to generate one triangulation starting from other 
    (if set to None creates a new random triangulation) and epsilon returns:
    - kernel_size: The size of the instance after applying the kernel
    - kernel_size_n: The size of the instance after applying the kernel as a fraction of n
    - kernel_size_theoric: The theoretical upper bound on the size of the kernel.
    - nc_diag_prekernel: The number of non-common diagonals before applying the kernel
    - nc_diag_postkernel: The number of non-common diagonals after applying the kernel
    - removed_instances: Number of instances removed when applying the kernel (the kernel first step is to 
    divide the triangulation into several instances)
    - max_removed: Size of the instance of maximum size that was removed.
    """

    rv = {
        'kernel_size': [],
        'kernel_size_n': [],
        'kernel_size_theoric': [],
        'nc_diag_prekernel': [],
        'nc_diag_postkernel': [],
        'removed_instances': [],
        'max_removed': [],
    }
    for _ in range(sample_size):
        t1 = tri.Triangulation(n)

        if D == None:  
            t2 = tri.Triangulation(n)
        else:
            t2 = copy.deepcopy(t1)
            t2.random_flips(D)

        decomp = t1.multi_divide(list(t1.common_diagonals(t2)))
        instances = [t for t in decomp if t.n >= (1/eps + 3)]
        removed = [t.n for t in decomp if t.n < (1/eps + 3)]
        max_removed = max(removed) if removed != [] else 0

        n_kernel = sum([t.n for t in instances]) - 2*len(instances) + 2 if len(instances) > 0 else 0
        nc_diag_pre = n - len(decomp) - 2
        nc_diag_post = n_kernel - len(instances) - 2 if n_kernel > 0 else 0

        rv['kernel_size'].append(n_kernel)
        rv['kernel_size_n'].append(n_kernel/n)
        rv['kernel_size_theoric'].append(nc_diag_pre*(1 + eps) + 2)
        rv['nc_diag_prekernel'].append(nc_diag_pre)
        rv['nc_diag_postkernel'].append(nc_diag_post)
        rv['removed_instances'].append(len(decomp) - len(instances))
        rv['max_removed'].append(max_removed)

    return rv

def multi_experiment(n_array, eps_array, D_array_n, sample_size, save=None):
    """Given lists of sizes, epsilons and k's, and a sample size, it performs an
    experiment for each possible combination of the elements in the lists. If 
    save is set to true then it saves the result of every individual experiment."""

    datas = itertools.product(n_array, eps_array, D_array_n)
    rv = {
        'n': [],
        'eps': [],
        'D': [],
        'kernel_size': [],
        'kernel_size_n': [],
        'kernel_size_theoric': [],
        'nc_diag_prekernel': [],
        'nc_diag_postkernel': [],
        'removed_instances': [],
        'max_removed': [],
    }
    for data in datas:
        n, eps = data[0], data[1]
        D = int(n*data[2])
        exp = experiment(sample_size, n, eps, D=D)

        df = pd.DataFrame(exp)
        if save is not None:
            df.to_csv('./{}/{}_{:.4f}_{}.csv'.format(save, n, eps, D))

        rv['n'].append(n)
        rv['eps'].append(eps)
        rv['D'].append(D)
        rv['kernel_size'].append(df['kernel_size'].mean())
        rv['kernel_size_n'].append(df['kernel_size_n'].mean())
        rv['kernel_size_theoric'].append(df['kernel_size_theoric'].mean())
        rv['nc_diag_prekernel'].append(df['nc_diag_prekernel'].mean())
        rv['nc_diag_postkernel'].append(df['nc_diag_postkernel'].mean())
        rv['removed_instances'].append(df['removed_instances'].mean())
        rv['max_removed'].append(df['max_removed'].mean())
    
    return rv
