.PHONY: all build demo shell _docs docs

all: demo

build:
	docker build -t django-easy-pdf .

demo: build
	docker run --rm -p=8000:8000 django-easy-pdf

shell: build
	docker run --rm -it django-easy-pdf bash

_docs:
	$(MAKE) -C docs html

docs:
	docker run --rm -v `pwd`/easy_pdf:/app/easy_pdf -v `pwd`/docs:/app/docs django-easy-pdf make _docs
