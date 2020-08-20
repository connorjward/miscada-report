#!/bin/bash

. ../../templates/particle_property_defaults.sh

envsubst < ../../templates/particle_property.txt > inputs/test.prm
envsubst < ../../templates/particle_property_ctrl.txt > inputs/ctrl.prm

