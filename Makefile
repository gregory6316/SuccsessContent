SHELL := /bin/bash
VENV_NAME?=success_venv
PYTHON=${VENV_NAME}/bin/python3

run: prepare_venv mo
	${PYTHON} Havau/local_run.py

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	test -d ${VENV_NAME} || virtualenv ${VENV_NAME}
	. ${VENV_NAME}/bin/activate; pip install -Ur requirements.txt
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/touchfile


pot: prepare_venv
	. ${VENV_NAME}/bin/activate; pybabel extract --msgid-bugs-address='https://github.com/gregory6316/SuccsessContent/issues' --copyright-holder='Succsess Content 2022' --project='}{avau' --version=0.1 Havau/widgets/custom_widgets/description.py -o Havau/locales/custom.pot 
	. ${VENV_NAME}/bin/activate; pybabel extract --msgid-bugs-address='https://github.com/gregory6316/SuccsessContent/issues' --copyright-holder='Succsess Content 2022' --project='}{avau' --version=0.1 Havau/main.py -o Havau/locales/main.pot 
	. ${VENV_NAME}/bin/activate; pybabel extract --msgid-bugs-address='https://github.com/gregory6316/SuccsessContent/issues' --copyright-holder='Succsess Content 2022' --project='}{avau' --version=0.1 Havau/widgets/mood_screen/description.py -o Havau/locales/mood_screen.pot 

po: prepare_venv pot
	. ${VENV_NAME}/bin/activate; pybabel init -l ru_RU -i Havau/locales/main.pot -d Havau/locales -D main
	. ${VENV_NAME}/bin/activate; pybabel init -l en_US -i Havau/locales/main.pot -d Havau/locales -D main
	. ${VENV_NAME}/bin/activate; pybabel init -l ru_RU -i Havau/locales/custom.pot  -d Havau/locales -D custom
	. ${VENV_NAME}/bin/activate; pybabel init -l en_US -i Havau/locales/custom.pot  -d Havau/locales -D custom
	. ${VENV_NAME}/bin/activate; pybabel init -l ru_RU -i Havau/locales/mood_screen.pot  -d Havau/locales -D mood_screen
	. ${VENV_NAME}/bin/activate; pybabel init -l en_US -i Havau/locales/mood_screen.pot  -d Havau/locales -D mood_screen

mo: prepare_venv
	. ${VENV_NAME}/bin/activate; pybabel compile -d Havau/locales --domain='custom main mood_screen'



docs: prepare_venv
	. ${VENV_NAME}/bin/activate && cd Havau/docs && make html
	 xdg-open Havau/docs/_build/html/index.html

sdist: prepare_venv
	git clean -fd
	find . | grep -E "__pycache__$$" | xargs rm -rf
	. ${VENV_NAME}/bin/activate; python3 -m build -s
	
	

test: prepare_venv
	 > Havau/storage.dict
	. ${VENV_NAME}/bin/activate; python3 -m pytest Havau/tests -W ignore::DeprecationWarning
	. ${VENV_NAME}/bin/activate; pylint $$(git ls-files '*.py')
	. ${VENV_NAME}/bin/activate; pydocstyle $$(git ls-files '*.py')

clean_venv:
	rm -rf success_venv

deploy: prepare_venv mo
	. ${VENV_NAME}/bin/activate && cd Havau/docs && make html
	find . | grep -E "__pycache__$$" | xargs rm -rf
	. ${VENV_NAME}/bin/activate; python3 -m build -w

install: prepare_venv deploy
	. ${VENV_NAME}/bin/activate; pip3 install dist/success_content-0.0.1-py3-none-any.whl 


clean:
	git clean -fd
