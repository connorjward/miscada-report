#!/bin/bash

mkdir -p tmp
rm -f tmp/*.prm

. ../../../data/templates/material_model_defaults.sh
export END_TIME=3e6
export INITIAL_GLOBAL_REFINEMENT=4

envsubst < ../../../data/templates/material_model.txt > tmp/input.prm

