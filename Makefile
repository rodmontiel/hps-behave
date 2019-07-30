default: test
.PHONY: default

install_prerequisites:
	pip install behave
.PHONY: install_prerequisites

generate_tests:
	hiptest-publisher -c behave.conf -t "$(SECRET_TOKEN)" --without=actionwords
.PHONY: generate_tests

test: install_prerequisites
	behave
.PHONY: test
