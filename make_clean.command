#!/usr/bin/env bash

BASEDIR=$(dirname $0)
cd $BASEDIR

latexmk -C thesis.tex
