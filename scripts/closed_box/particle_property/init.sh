#!/bin/bash

mkdir -p tmp
rm -f tmp/*.prm

. ../../../data/templates/particle_property_defaults.sh
export END_TIME=3e6
export INITIAL_GLOBAL_REFINEMENT=5
export N_PARTICLES=2000

envsubst < ../../../data/templates/particle_property.txt > tmp/input.prm

