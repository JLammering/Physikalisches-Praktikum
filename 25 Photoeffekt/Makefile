ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot.py

build/orange.pdf: orange.py matplotlibrc header-matplotlib.tex Daten/orange.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python orange.py

build/gruen.pdf: gruen.py matplotlibrc header-matplotlib.tex Daten/gruen.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python gruen.py

build/tuerkis.pdf: tuerkis.py matplotlibrc header-matplotlib.tex Daten/tuerkis.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python tuerkis.py

build/blau.pdf: blau.py matplotlibrc header-matplotlib.tex Daten/blau.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python blau.py

build/violett.pdf: violett.py matplotlibrc header-matplotlib.tex Daten/violett.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python violett.py

build/Frequenz.pdf: Frequenz.py matplotlibrc header-matplotlib.tex Daten/Frequenz.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python Frequenz.py

build/c.pdf: c.py matplotlibrc header-matplotlib.tex Daten/c.txt Daten/c2.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python c.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/orange.pdf build/gruen.pdf build/tuerkis.pdf build/blau.pdf build/violett.pdf build/Frequenz.pdf build/c.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
