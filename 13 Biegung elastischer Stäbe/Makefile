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
build/Stab1einfach.pdf: Stab1einfach.py matplotlibrc header-matplotlib.tex Stab1einfach.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab1einfach.py

build/Stab1einfachFehler.pdf: Stab1einfachFehler.py matplotlibrc header-matplotlib.tex Stab1einfach.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab1einfachFehler.py

build/Stab2einfach.pdf: Stab2einfach.py matplotlibrc header-matplotlib.tex Stab2einfach.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab2einfach.py

build/Stab2einfachFehler.pdf: Stab2einfachFehler.py matplotlibrc header-matplotlib.tex Stab2einfach.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab2einfachFehler.py

build/Stab2doppeltl.pdf: Stab2doppeltl.py matplotlibrc header-matplotlib.tex Stab2doppelt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab2doppeltl.py

build/Stab2doppeltr.pdf: Stab2doppeltr.py matplotlibrc header-matplotlib.tex Stab2doppelt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab2doppeltr.py

build/Stab2doppeltFehler.pdf: Stab2doppeltFehler.py matplotlibrc header-matplotlib.tex Stab2doppelt.txt | build
	TEXINPUTS="$(call translate,$(pwd):)" python Stab2doppeltFehler.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/Stab1einfach.pdf build/Stab1einfachFehler.pdf build/Stab2einfach.pdf build/Stab2einfachFehler.pdf build/Stab2doppeltl.pdf build/Stab2doppeltr.pdf build/Stab2doppeltFehler.pdf

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
