#!/bin/bash

. ../../templates/material_model_defaults.sh

for pow in {2..5}; do
  export CACHE_TOL=1e-$pow
  envsubst < ../../templates/material_model.txt > inputs/1e-${pow}.prm

  export CACHE_TOL=5e-$pow
  envsubst < ../../templates/material_model.txt > inputs/5e-${pow}.prm
done
