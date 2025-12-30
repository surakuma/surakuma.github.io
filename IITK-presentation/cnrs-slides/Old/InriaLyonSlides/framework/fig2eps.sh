#!/bin/bash

FILE=Chameleon
src=$FILE.fig
layer1="+18,21,25,40,41,48,49,51,59"
layer2="+18,19,21,25,40,41,46,47,48,51,58"
layer2="+18,19,21,25,40,41,46,47,51,58"
layer3="+18,19,21,25,41,46,47,48,51,58"
layer3="+18,19,21,25,41,46,47,51,58"
layer4="+18,19,21,24,41,44,45,46,51,57"
layer5="+18,20,24,41,43,45,46,51,57"


layer11="+40,41,48,49,51"
layer21="+40,41,46,47,51"
layer31="+41,46,47,48,51"
layer41="+41,44,45,46,51"
layer51="+41,43,45,46,51"

fig2dev -L eps -D $layer1 $src Actual_execution.eps
fig2dev -L eps -D $layer2 $src Simulation.eps
fig2dev -L eps -D $layer3 $src Simulation_nocomm.eps
fig2dev -L eps -D $layer4 $src Emulation_FeasibleSolution.eps
fig2dev -L eps -D $layer5 $src Emulation_Area.eps


fig2dev -L eps -D $layer11 $src Actual_execution_box.eps
fig2dev -L eps -D $layer21 $src Simulation_box.eps
fig2dev -L eps -D $layer31 $src Simulation_nocomm_box.eps
fig2dev -L eps -D $layer41 $src Emulation_FeasibleSolution_box.eps
fig2dev -L eps -D $layer51 $src Emulation_Area_box.eps
