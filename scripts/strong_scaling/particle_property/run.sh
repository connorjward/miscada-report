#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

DATA_DIR=../../../var/strong_scaling/particle_property

# Remove old data
mkdir -p $DATA_DIR
rm -f $DATA_DIR/*.txt

# Avoid cold start effects.
mpirun -np 12 ./aspect tmp/input.prm

# Execute.
for n in {1..12}; do
  mpirun -np $n ./aspect tmp/input.prm | tee $DATA_DIR/${n}.txt
  mpirun -np $n ./aspect tmp/input_ctrl.prm | tee $DATA_DIR/${n}_ctrl.txt
done

# Clean up.
rm -r output
