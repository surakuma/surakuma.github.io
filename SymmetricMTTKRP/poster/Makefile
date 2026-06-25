.PHONY: main clean FORCE

main: mttkrp.pdf

mttkrp.pdf: FORCE
	latexmk -pdflatex='lualatex -interaction nonstopmode' -pdf mttkrp.tex

clean:
	latexmk -pdf -C
