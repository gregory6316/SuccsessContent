SHELL := /bin/bash
VENV_NAME?=success_venv
PYTHON=${VENV_NAME}/bin/python3

run: prepare_venv mo
	${PYTHON} main.py

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	test -d ${VENV_NAME} || virtualenv ${VENV_NAME}
	. ${VENV_NAME}/bin/activate; pip install -Ur requirements.txt
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/touchfile


pot: prepare_venv
	. ${VENV_NAME}/bin/activate; pybabel extract --msgid-bugs-address='https://github.com/gregory6316/SuccsessContent/issues' --copyright-holder='Succsess Content 2022' --project='}{avau' --version=0.1 widgets/custom_widgets/description.py -o locales/custom.pot 
	. ${VENV_NAME}/bin/activate; pybabel extract --msgid-bugs-address='https://github.com/gregory6316/SuccsessContent/issues' --copyright-holder='Succsess Content 2022' --project='}{avau' --version=0.1 main.py -o locales/main.pot 
	. ${VENV_NAME}/bin/activate; pybabel extract --msgid-bugs-address='https://github.com/gregory6316/SuccsessContent/issues' --copyright-holder='Succsess Content 2022' --project='}{avau' --version=0.1 widgets/mood_screen/description.py -o locales/mood_screen.pot 

po: prepare_venv pot
	. ${VENV_NAME}/bin/activate; pybabel init -l ru_RU -i locales/main.pot -d locales -D main
	. ${VENV_NAME}/bin/activate; pybabel init -l en_US -i locales/main.pot -d locales -D main
	. ${VENV_NAME}/bin/activate; pybabel init -l ru_RU -i locales/custom.pot  -d locales -D custom
	. ${VENV_NAME}/bin/activate; pybabel init -l en_US -i locales/custom.pot  -d locales -D custom
	. ${VENV_NAME}/bin/activate; pybabel init -l ru_RU -i locales/mood_screen.pot  -d locales -D mood_screen
	. ${VENV_NAME}/bin/activate; pybabel init -l en_US -i locales/mood_screen.pot  -d locales -D mood_screen

mo: prepare_venv
	. ${VENV_NAME}/bin/activate; pybabel compile -d locales --domain='custom main mood_screen'



docs: prepare_venv
	. ${VENV_NAME}/bin/activate && cd docs && make html
	 xdg-open docs/build/html/index.html

sdist: prepare_venv
	git clean -fd
	. ${VENV_NAME}/bin/activate; python3 -m build -s

	
	

test: prepare_venv
	 > storage.dict
	. ${VENV_NAME}/bin/activate; python3 -m pytest tests -W ignore::DeprecationWarning
	. ${VENV_NAME}/bin/activate; pylint $$(git ls-files '*.py')
	. ${VENV_NAME}/bin/activate; pydocstyle $$(git ls-files '*.py')

clean_venv:
	rm -rf success_venv

deploy: prepare_venv mo
	. ${VENV_NAME}/bin/activate && cd docs && make html
	. ${VENV_NAME}/bin/activate; python3 -m build -w

install: prepare_venv deploy
	. ${VENV_NAME}/bin/activate; pip3 install dist/success_content-0.0.1-py3-none-any.whl 


clean:
	git clean -fd
