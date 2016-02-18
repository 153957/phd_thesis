#!/usr/bin/env bash

BASEDIR=$(dirname $0)
cd $BASEDIR

export max_print_line=200
rm thesis.bcf
latexmk -pdf -pv --shell-escape -latexoption='-file-line-error -halt-on-error' -g thesis.tex

if [[ "$OSTYPE" == "darwin"* ]]; then
    for i in *.{out,log,aux,toc,bbl,dvi,blg,synctex.gz,fdb_latexmk,bcf,fls,run.xml,tdo,auxlock,pyg};
        do chflags hidden $i;
    done

    for i in */*.aux;
        do chflags hidden $i;
    done

    for i in tikz/*.{dpth,md5,run.xml,log};
        do chflags hidden $i;
    done

    for i in _minted*;
        do chflags hidden $i;
    done
fi
