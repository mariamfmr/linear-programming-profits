.PHONY: test clean checkpy

# Define the python command and the script to run
PYTHON := python3
SCRIPT := proj.py

# Define the input and output directories
IN_DIR := testsTime
OUT_DIR := testsTime

# Define the input and output file extensions
IN_EXT := .in
OUT_EXT := .out

# Get a list of all input files
IN_FILES := $(wildcard $(IN_DIR)/*$(IN_EXT))

# Define the corresponding output files
OUT_FILES := $(patsubst $(IN_DIR)/%$(IN_EXT),$(OUT_DIR)/%$(OUT_EXT),$(IN_FILES))

# Rule to run the tests
test: $(OUT_FILES)

# Rule to generate an output file from an input file
$(OUT_DIR)/%$(OUT_EXT): $(IN_DIR)/%$(IN_EXT)
	$(PYTHON) $(SCRIPT) < $< > $@

# Rule to clean the results
clean:
	rm -f $(OUT_DIR)/*$(OUT_EXT)

# Rule to check the python version
checkpy:
	$(PYTHON) --version
