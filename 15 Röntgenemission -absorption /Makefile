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

build/emissionsspektrumKalpha.pdf: emissionsspektrumKalpha.py matplotlibrc header-matplotlib.tex Daten/emissionsspektrumKalpha.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python emissionsspektrumKalpha.py

build/emissionsspektrumKbetha.pdf: emissionsspektrumKbetha.py matplotlibrc header-matplotlib.tex Daten/emissionsspektrumKbetha.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python emissionsspektrumKbetha.py

build/Moseley.pdf: Moseley.py matplotlibrc header-matplotlib.tex Daten/Moseley.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Moseley.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/emissionsspektrumKalpha.pdf build/emissionsspektrumKbetha.pdf build/Moseley.pdf

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
