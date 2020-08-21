#!/bin/bash

. ../../templates/material_model_defaults.sh

mkdir -p tmp

for n in {1..12}; do
  export N_REPS=$n
  envsubst < ../../templates/material_model.txt > tmp/${n}.prm
done
