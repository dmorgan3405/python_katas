.DEFAULT_GOAL := prepare
.PHONY: test
.PHONY: prepare

test:
	py.test -rwx -s test/

prepare:
	pip install -r requirements.pip
