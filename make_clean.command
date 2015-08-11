#!/usr/bin/env bash

BASEDIR=$(dirname $0)
cd $BASEDIR

latexmk -C thesis.tex
rm -rf `biber --cache`
