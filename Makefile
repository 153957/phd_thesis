PHONY: clean pdf pdfc figure hide

clean:
	latexmk -C thesis.tex

pdf: clean
	latexmk -pdf -pv --shell-escape -latexoption='-file-line-error -halt-on-error' thesis.tex
	$(MAKE) hide

pdfc:
	latexmk -pdf -pvc --shell-escape -quiet thesis.tex

figure:
	latexmk -C thesis-figure.tex
	latexmk -pdf -pvc --shell-escape -quiet thesis-figure.tex
	$(MAKE) hide

hide:
	./hide_aux.sh
