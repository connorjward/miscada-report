#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

DATA_DIR="../../../var/load_balancing/material_model"

# Remove old data
mkdir -p $DATA_DIR
rm -f $DATA_DIR/*.txt 

# Execute.
mpirun -np 12 ./aspect tmp/input.prm
mv output/statistics $DATA_DIR/data.txt

# Clean up.
rm -r output
