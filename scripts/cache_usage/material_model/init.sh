#!/bin/bash

export N_REPS=3

for pow in {2..5}; do
  export CACHE_TOL=1e-$pow
  envsubst < ../../templates/material_model.txt > inputs/1e-${pow}.prm

  export CACHE_TOL=5e-$pow
  envsubst < ../../templates/material_model.txt > inputs/5e-${pow}.prm
done
