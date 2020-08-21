#!/bin/bash

. ../../templates/particle_property_defaults.sh

mkdir -p tmp
rm -f tmp/*.prm

envsubst < ../../templates/particle_property.txt > tmp/test.prm
envsubst < ../../templates/particle_property_ctrl.txt > tmp/ctrl.prm

