.PHONY: all help clean clean-build clean-pyc demo lint mypy test test-all docs release sdist dist upload docker-build docker-demo docker-shell

all: docker-demo

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "mypy - check types with mypy"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "sdist - package"
	@echo "dist - package sdist and wheel"
	@echo "upload - upload to PyPI"
	@echo "release - package and upload a release"
	@echo "docker-demo - build and run demo using Docker image"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	flake8 easy_pdf tests

mypy:
	mypy --ignore-missing-imports --strict-optional easy_pdf tests  --verbose

test:
	python runtests.py

test-all:
	tox

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	sphinx-build -b linkcheck ./docs _build/
	sphinx-build -b html ./docs _build/

release: lint test docs clean dist upload

sdist: clean
	python setup.py sdist
	ls -l dist

dist: clean
	python setup.py sdist bdist_wheel

upload:
	twine upload -s dist/*

demo:
	python demo.py

# Docker workflow

docker-build:
	docker build -t django-easy-pdf .

docker-demo: docker-build
	docker run --rm -it -p 8000:8000 -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs -v `pwd`/dist:/app/dist -v `pwd`/tests:/app/tests django-easy-pdf make demo

docker-shell: docker-build
	docker run --rm -it -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs -v `pwd`/dist:/app/dist -v `pwd`/tests:/app/tests django-easy-pdf bash

docker-upload:
	docker run --rm -it -v ~/.pypirc:/root/.pypirc -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs -v `pwd`/dist:/app/dist -v `pwd`/tests:/app/tests django-easy-pdf make upload

docker-%: docker-build
	docker run --rm -it -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs -v `pwd`/dist:/app/dist -v `pwd`/tests:/app/tests django-easy-pdf make $*

ci-docker-%: docker-build
	docker run -it -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs -v `pwd`/dist:/app/dist -v `pwd`/tests:/app/tests django-easy-pdf make $*
