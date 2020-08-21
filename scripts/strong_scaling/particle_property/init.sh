#!/bin/bash

. ../../templates/particle_property_defaults.sh

mkdir -p tmp

envsubst < ../../templates/particle_property.txt > tmp/input.prm
envsubst < ../../templates/particle_property_ctrl.txt > tmp/input_ctrl.prm

