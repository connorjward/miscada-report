#!/bin/bash

. ../../templates/material_model_defaults.sh

mkdir -p tmp

envsubst < ../../templates/material_model.txt > tmp/input.prm

