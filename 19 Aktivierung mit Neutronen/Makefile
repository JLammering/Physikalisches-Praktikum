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

build/Jod.pdf: Jod.py matplotlibrc header-matplotlib.tex Daten/Jod.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Jod.py

build/RhodiumM.pdf: RhodiumM.py matplotlibrc header-matplotlib.tex Daten/Rhodium.txt Daten/Rhodium2.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python RhodiumM.py

build/Rhodium.pdf: Rhodium.py matplotlibrc header-matplotlib.tex Daten/Rhodium.txt Daten/Rhodium2.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python Rhodium.py

build/Rhodium2.pdf: Rhodium2.py matplotlibrc header-matplotlib.tex Daten/Rhodium2.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python Rhodium2.py

build/RhodiumE.pdf: RhodiumE.py matplotlibrc header-matplotlib.tex Daten/Rhodium.txt Daten/Rhodium2.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python RhodiumE.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/Jod.pdf build/RhodiumM.pdf build/Rhodium.pdf build/Rhodium2.pdf build/RhodiumE.pdf

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
