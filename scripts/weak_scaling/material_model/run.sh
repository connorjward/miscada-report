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
mpirun -np 12 ./aspect inputs/test1.prm > /dev/null

# Execute.
for n in {1..12}; do
  mpirun -np $n ./aspect inputs/test$n.prm | tee data/test$n.txt
  mpirun -np $n ./aspect inputs/ctrl$n.prm | tee data/ctrl$n.txt
done

# Clean up.
rm -r output