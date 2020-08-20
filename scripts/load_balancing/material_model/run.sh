#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

# Remove old data
rm data/*.txt

# Execute.
mpirun -np 12 ./aspect inputs/test.prm
mv output/statistics data/test.txt

mpirun -np 12 ./aspect inputs/ctrl.prm
mv output/statistics data/ctrl.txt

# Clean up.
rm -r output
