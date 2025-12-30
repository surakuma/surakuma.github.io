#!/bin/bash

FILE=heteroprio
src=$FILE.fig
layer1="+45,48,49,50"
layer2="+44,45,49,50"
layer3="+44,49,50,55"
layer4="+42,43,49,50,55,56"

fig2dev -L eps -D $layer1 $src heteroprio1.eps 
fig2dev -L eps -D $layer2 $src heteroprio2.eps 
fig2dev -L eps -D $layer3 $src heteroprio3.eps 
fig2dev -L eps -D $layer4 $src heteroprio4.eps 

