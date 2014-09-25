#!/bin/sh

BASEDIR=$(dirname $0)
cd $BASEDIR

latexmk -pdf -pv thesis.tex

for i in *.{out,log,aux,toc,bbl,dvi,blg,synctex.gz,fdb_latexmk,bcf,fls};
    do chflags hidden $i;
done
