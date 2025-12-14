help:
	@echo "Usage:"
	@echo "    make help        show this message"
	@echo "    make setup       create virtual environment and install dependencies"
	@echo "    make activate    enter virtual environment"
	@echo "    make test        run the tests"


POETRY := $(shell command -v poetry 2> /dev/null)

setup:
ifndef POETRY
	@echo "Poetry not found. Installing..."
	curl -sSL https://install.python-poetry.org | python3 -
	export PATH="$$HOME/.local/bin:$$PATH"
endif
	poetry install

activate:
	poetry shell

test:
	poetry run pytest