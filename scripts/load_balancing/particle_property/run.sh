#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

# Remove old data
mkdir -p data
rm -f data/*.txt

# Execute.
mpirun -np 12 ./aspect tmp/test.prm
mv output/statistics data/test.txt

mpirun -np 12 ./aspect tmp/ctrl.prm
mv output/statistics data/ctrl.txt

# Clean up.
rm -r output
