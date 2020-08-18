#!/bin/csh

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

# Avoid cold start effects.
./aspect batch.prm > /dev/null

mpirun -np 12 ./aspect batch.prm

# Clean up.
mv output-box_batch/statistics batch_statistics
rm -r output-box_batch
