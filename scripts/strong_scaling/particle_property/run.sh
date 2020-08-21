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

# Avoid cold start effects.
mpirun -np 12 ./aspect tmp/input.prm

# Execute.
for n in {1..12}; do
  mpirun -np $n ./aspect tmp/input.prm | tee data/${n}.txt
  mpirun -np $n ./aspect tmp/input_ctrl.prm | tee data/${n}_ctrl.txt
done

# Clean up.
rm -r output
