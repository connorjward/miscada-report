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
mpirun -np 12 ./aspect inputs/1e-2.prm > /dev/null

# Execute.
for pow in {2..5}; do
  mpirun -np 12 ./aspect inputs/1e-$pow.prm > /dev/null
  mv output/statistics data/1e-${pow}.txt

  mpirun -np 12 ./aspect inputs/5e-$pow.prm > /dev/null
  mv output/statistics data/5e-${pow}.txt
done

# Clean up.
rm -r output
