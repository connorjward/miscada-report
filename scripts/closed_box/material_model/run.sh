#!/bin/bash

#############################################################################

#SBATCH  -n  12 
#SBATCH  -p  par7.q

#############################################################################

module purge
module load use.own aspect/release
module load gsl/gcc/64/1.15 # required to avoid dynamic library error

DATA_DIR=../../../var/closed_box/material_model
mkdir -p $DATA_DIR
rm -f -r $DATA_DIR

mpirun -np 12 ./aspect tmp/input.prm

mv output $DATA_DIR
