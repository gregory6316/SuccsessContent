SHELL := /bin/bash
VENV_NAME?=success_venv
PYTHON=${VENV_NAME}/bin/python3

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	test -d ${VENV_NAME} || virtualenv ${VENV_NAME}
	. ${VENV_NAME}/bin/activate; pip install -Ur requirements.txt
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/touchfile

run: prepare_venv
	${PYTHON} main.py

docs: prepare_venv
	. ${VENV_NAME}/bin/activate && cd docs && make html
	 xdg-open docs/build/html/index.html
	
	

test: prepare_venv
	 > storage.dict
	. ${VENV_NAME}/bin/activate; python3 -m pytest tests -W ignore::DeprecationWarning
	. ${VENV_NAME}/bin/activate; pylint $$(git ls-files '*.py')
	. ${VENV_NAME}/bin/activate; pydocstyle $$(git ls-files '*.py')

clean_venv:
	rm -rf success_venv

deploy:
	echo 'buildozer is dead :('

clean:
	git clean -fd
