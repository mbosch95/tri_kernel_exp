# Triangulations of Convex Polygons Experiments

A set of experiments to measure the effect of an improved kernel for the minimum flip distance between triangulations of convex polygons problem.

## Description

This project is used to get data on how the improved kernel for the minimum flip distance between triangulations of convex polygons problem performs in practise. The project consists in a file modelling the triangulations, a file modelling the experiments and a main file to execute. We have also included in the folder "data" the results we have used in our article, and in the folder "figures" the figure we have used, extra figures for different parameters, and the data for the table of the size of the maximum instance removed in the file "max_removed.txt".

The main program uses as inputs:
* "n_array": A list of all the sizes of the triangulations we want to compute experiments for.
* "D_array": A list of all the D values we want to compute experiments for. The D value is the number of random flips used to generate the second triangulation of a pair. 
* "eps_array": A list of all the values of epsilon of the kernel we want to compute experiments for.

And will output in a file the following data regarding pairs of triangulations:

*  kernel_size: The size of the instance after applying the kernel.
*  kernel_size_n: The size of the instance after applying the kernel as a fraction of n.
*  kernel_size_theoric: The theoretical lower bound of the upper bound of the size of the kernel, computed based on the non-common diagonals before applying the kernel.
*  nc_diag_prekernel: The number of non-common diagonals before applying the kernel.
*  nc_diag_postkernel: The number of non-common diagonals after applying the kernel.
*  removed_instances: Number of instances removed when applying the kernel.
*  max_removed: Size of the instance of maximum size that was removed.


## Getting Started

### Dependencies

The program requires python 3.9.0. The dependencies can be found in the file "experiments.txt".

### Installing and executing the program

The program is executed through a python virtual machine.

To execute the program execute the file "tri_kernel_exp.py". Then the program will run an experiment for each combination of n, eps and D in n_array, eps_array and D_array. The results will be saved to the indicated direction. If the argument "data" has a value different from "None", then it will also salve a file for each of the individual experiments.

## Authors

Miguel Bosch Calvo
[Steven Kelk](http://skelk.sdf-eu.org)