#!/bin/bash

. ../../templates/material_model_defaults.sh

for n in {1..12}; do
  export N_REPS=$n
  envsubst < ../../templates/material_model.txt > inputs/test${n}.prm
  envsubst < ../../templates/material_model_ctrl.txt > inputs/ctrl${n}.prm
done
