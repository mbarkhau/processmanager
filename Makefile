
SHELL := /bin/bash
.SHELLFLAGS := -O extglob -eo pipefail -c
.SUFFIXES:


## Create python sdist and bdist_wheel files
.PHONY: dist_build
dist_build:
	python setup.py sdist;
	python setup.py bdist_wheel --python-tag=py2.py3;
