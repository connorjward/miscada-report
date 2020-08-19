#!/bin/bash

export CACHE_TOL=0.0001

for n in {1..12}; do
  export N_PARTICLES=$((n*400))
  envsubst < ../../templates/particle_property.txt > inputs/test$n.prm
  envsubst < ../../templates/particle_property_ctrl.txt > inputs/ctrl$n.prm
done
