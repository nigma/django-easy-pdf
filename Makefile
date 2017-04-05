.PHONY: all build demo shell _test test _check check _docs docs

all: demo

build:
	docker build -t django-easy-pdf .

demo: build
	docker run --rm -p=8000:8000 -e PORT=8000 django-easy-pdf

shell: build
	docker run --rm -it django-easy-pdf bash

_test:
	python tests/manage.py test

test: build
	docker run --rm -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/tests:/app/tests django-easy-pdf make _test

_check:
	flake8 easy_pdf
	mypy --py2 --ignore-missing-imports --strict-optional easy_pdf
	mypy --ignore-missing-imports --strict-optional easy_pdf

check: build
	docker run --rm -v `pwd`/easy_pdf:/app/easy_pdf django-easy-pdf make _check

_docs:
	$(MAKE) -C docs html

docs:
	docker run --rm -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs django-easy-pdf make _docs
