VENV_DIR = venv
PYTHON = python3

.PHONY: venv activate deactivate clean

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)."

# Activate virtual environment (for Linux/Mac)
activate:
	@echo "Run the following command to activate the virtual environment:"
	@echo "source $(VENV_DIR)/bin/activate"

# Deactivate virtual environment
deactivate:
	@echo "Run 'deactivate' inside the virtual environment to deactivate it."

# Execute python program
run:
	$(PYTHON) main.py 