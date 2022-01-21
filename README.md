# About

Framework for REST API automation testing in python

Stack: python, requests, pytest

# How to install and run framework?

1) Clone this git repository: git clone https://github.com/Maximweller/api-framework.git
2) Open file and install virtual environment: python3 -m venv env
3) Activate virtual environment: source vir/bin/activate
4) Install all requirements:  pip install -r requirements.txt

# How to run?

python3 -m pytest -s tests

or

python3 -m pytest --alluredir=test_results/ tests/test_user_edit.py
allure serve test_results/
