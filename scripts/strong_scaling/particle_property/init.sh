#!/bin/bash

TEMPLATE_DIR=../../../data/templates

mkdir -p tmp
rm -f tmp/*.prm

. $TEMPLATE_DIR/particle_property_defaults.sh

envsubst < $TEMPLATE_DIR/particle_property.txt > tmp/input.prm
envsubst < $TEMPLATE_DIR/particle_property_ctrl.txt > tmp/input_ctrl.prm

