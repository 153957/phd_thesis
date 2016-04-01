#!/usr/bin/env bash

BASEDIR=$(dirname $0)
cd $BASEDIR

export max_print_line=200
latexmk -pdf -pv --shell-escape -latexoption='-file-line-error -halt-on-error' -g thesis.tex

. ./hide_aux.sh
