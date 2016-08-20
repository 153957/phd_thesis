#!/usr/bin/env bash

BASEDIR=$(dirname $0)
cd $BASEDIR

export max_print_line=200
latexmk -C thesis-figure.tex
latexmk -pdf -pvc --shell-escape -quiet thesis-figure.tex

. ./hide_aux.sh
