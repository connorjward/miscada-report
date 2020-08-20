#!/bin/bash

. ../../templates/particle_property_defaults.sh

export END_TIME=3e6
export INITIAL_GLOBAL_REFINEMENT=5
export N_PARTICLES=2000

envsubst < ../../templates/particle_property.txt > input.prm

