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
for pow in {2..5}; do
  echo "Now testing 1e-${pow}..."
  mpirun -np 12 ./aspect inputs/1e-${pow}.prm
  mv output/statistics data/1e-${pow}.txt

  echo "Now testing 5e-${pow}..."
  mpirun -np 12 ./aspect inputs/5e-${pow}.prm
  mv output/statistics data/5e-${pow}.txt
done

# Clean up.
rm -r output
