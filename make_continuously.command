#!/bin/sh

BASEDIR=$(dirname $0)
cd $BASEDIR

latexmk -pdf -pvc -quiet thesis.tex
