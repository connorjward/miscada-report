#!/bin/bash

. ../../templates/material_model_defaults.sh

mkdir -p tmp

for pow in {2..5}; do
  export CACHE_TOL=1e-$pow
  envsubst < ../../templates/material_model.txt > tmp/1e-${pow}.prm

  export CACHE_TOL=5e-$pow
  envsubst < ../../templates/material_model.txt > tmp/5e-${pow}.prm
done
