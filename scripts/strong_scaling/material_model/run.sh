#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

# Create data directory if it does not exist.
mkdir -p data

# Remove old data
rm -f data/*.txt

# Avoid cold start effects.
mpirun -np 12 ./aspect tmp/input.prm

for n in {1..12}; do
  mpirun -np $n ./aspect tmp/input.prm | tee data/${n}.txt
done

# Clean up.
rm -r output
