.PHONY: install test run clean

install:
	pip install -r requirements.txt

test:
	pytest

run:
	python main.py

clean:
	rm -rf __pycache__ *.pyc venv
