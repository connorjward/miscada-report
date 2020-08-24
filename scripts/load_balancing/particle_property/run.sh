#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

OUTPUT_DIR=../../../var/load_balancing/particle_property

mkdir -p $OUTPUT_DIR

# Remove old data
rm -f $OUTPUT_DIR/*.txt

# Execute.
mpirun -np 12 ./aspect tmp/test.prm
mv output/statistics $OUTPUT_DIR/test.txt

mpirun -np 12 ./aspect tmp/ctrl.prm
mv output/statistics $OUTPUT_DIR/ctrl.txt

# Clean up.
rm -r output
