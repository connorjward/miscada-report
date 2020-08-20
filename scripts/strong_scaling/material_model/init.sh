#!/bin/bash

. ../../templates/material_model_defaults.sh

envsubst < ../../templates/material_model.txt > inputs/test.prm
envsubst < ../../templates/material_model_ctrl.txt > inputs/ctrl.prm

