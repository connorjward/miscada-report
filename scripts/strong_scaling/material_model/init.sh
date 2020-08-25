#!/bin/bash

mkdir -p tmp
rm -f tmp/*.prm

. ../../../data/templates/material_model_defaults.sh

envsubst < ../../../data/templates/material_model.txt > tmp/input.prm

