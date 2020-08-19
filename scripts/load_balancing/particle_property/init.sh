#!/bin/bash

export CACHE_TOL=0.0001
export N_PARTICLES=1000

envsubst < ../../templates/particle_property.txt > inputs/test.prm
envsubst < ../../templates/particle_property_ctrl.txt > inputs/ctrl.prm

