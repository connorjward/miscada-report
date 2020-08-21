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
for pow in {2..5}; do
  echo "Now running with the cache tolerance set to 1e-${pow}..."
  mpirun -np 12 ./aspect tmp/1e-${pow}.prm
  mv output/statistics data/1e-${pow}.txt

  echo "Now running with the cache tolerance set to 5e-${pow}..."
  mpirun -np 12 ./aspect tmp/5e-${pow}.prm
  mv output/statistics data/5e-${pow}.txt
done

# Clean up.
rm -r output
