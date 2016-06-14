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
build/einzelspalt1.pdf: einzelspalt1.py daten/einzelspalte.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python einzelspalt1.py

build/einzelspalt2.pdf: einzelspalt2.py daten/einzelspalte.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python einzelspalt2.py

build/einzelspalt3.pdf: einzelspalt3.py daten/einzelspalte.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python einzelspalt3.py

build/doppelspalt.pdf: doppelspalt.py daten/doppelspalt.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python doppelspalt.py

build/vergleich.pdf: vergleich.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python vergleich.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/einzelspalt1.pdf build/einzelspalt2.pdf build/einzelspalt3.pdf build/doppelspalt.pdf build/vergleich.pdf

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
