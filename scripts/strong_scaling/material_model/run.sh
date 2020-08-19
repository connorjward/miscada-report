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

# Avoid cold start effects.
mpirun -np 12 ./aspect inputs/test.prm > /dev/null

for i in {1..12}; do
  mpirun -np ./aspect inputs/test.prm | tee data/test$n.txt
  mpirun -np ./aspect inputs/ctrl.prm | tee data/ctrl$n.txt
done

# Clean up.
rm -r output
