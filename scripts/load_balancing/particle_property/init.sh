#!/bin/bash

TEMPLATE_DIR=../../../data/templates

mkdir -p tmp
rm -f tmp/*.prm

. $TEMPLATE_DIR/particle_property_defaults.sh
export N_PARTICLES=2000

envsubst < $TEMPLATE_DIR/particle_property.txt > tmp/test.prm
envsubst < $TEMPLATE_DIR/particle_property_ctrl.txt > tmp/ctrl.prm

