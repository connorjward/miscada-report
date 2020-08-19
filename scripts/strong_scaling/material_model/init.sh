#!/bin/bash

export CACHE_TOL=0.0001
export N_REPS=3

envsubst < ../../templates/material_model.txt > inputs/test.prm
envsubst < ../../templates/material_model_ctrl.txt > inputs/ctrl.prm

