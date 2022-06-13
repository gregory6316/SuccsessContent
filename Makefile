VENV_NAME?=success_venv
PYTHON=${VENV_NAME}/bin/python

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate

run: prepare_venv
	${PYTHON} main.py

build_docs: prepare_venv
	echo 'docs :)'

test:
	pytest tests

clean_venv:
	rm -rf success_venv

deploy:
	echo 'buildozer is dead :('

clean:
	git clean -fd
