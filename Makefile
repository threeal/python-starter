.DEFAULT_GOAL := install

clean:
	rm -rf .venv

.venv/%:
	python3 -m venv .venv --upgrade --upgrade-deps
	.venv/bin/pip install -e .

install: .venv/%

.PHONY: clean install
