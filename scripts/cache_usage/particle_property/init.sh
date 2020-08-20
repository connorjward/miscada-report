#!/bin/bash

. ../../templates/particle_property_defaults.sh

for pow in {2..5}; do
  export CACHE_TOL=1e-$pow
  envsubst < ../../templates/particle_property.txt > inputs/1e-${pow}.prm

  export CACHE_TOL=5e-$pow
  envsubst < ../../templates/particle_property.txt > inputs/5e-${pow}.prm
done
