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

build/plotvwinkel15.pdf: v_winkel15.py matplotlibrc header-matplotlib.tex daten/v_winkel15.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python v_winkel15.py

build/plotvwinkel30.pdf: v_winkel30.py matplotlibrc header-matplotlib.tex daten/v_winkel30.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python v_winkel30.py

build/plotvwinkel60.pdf: v_winkel60.py matplotlibrc header-matplotlib.tex daten/v_winkel60.txt| build
	TEXINPUTS="$(call translate,$(pwd):)" python v_winkel60.py

build/plotvprofil70.pdf: plotvprofil70.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotvprofil70.py

build/plotvprofil45.pdf: plotvprofil45.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotvprofil45.py

build/plotintensprofil70.pdf: plotintensprofil70.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotintensprofil70.py

build/plotintensprofil45.pdf: plotintensprofil45.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plotintensprofil45.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf build/plotvwinkel15.pdf build/plotvwinkel30.pdf build/plotvwinkel60.pdf build/plotvprofil70.pdf build/plotvprofil45.pdf build/plotintensprofil70.pdf build/plotintensprofil45.pdf

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
