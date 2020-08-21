#!/bin/bash

. ../../templates/particle_property_defaults.sh

mkdir -p tmp

for n in {1..12}; do
  export N_PARTICLES=$((n*400))
  envsubst < ../../templates/particle_property.txt > tmp/${n}.prm
  envsubst < ../../templates/particle_property_ctrl.txt > inputs/${n}_ctrl.prm
done
