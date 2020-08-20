#!/bin/bash

. ../../templates/material_model_defaults.sh

export END_TIME=3e6
export INITIAL_GLOBAL_REFINEMENT=4

envsubst < ../../templates/material_model.txt > input.prm

