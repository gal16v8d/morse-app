# morse-app

# Get started

## Unix

Install pipenv:
pip3 install pipenv
Then create the folder for allocate the virtual environment:
mkdir .venv
Launch pipenv:
pipenv install --skip-lock
Then activate the virtual env:
pipenv shell
Run command inside virtualenv:
pipenv run
Exit virtual env:
exit or deactivate

## Windows

Update pip:
py -m pip install --upgrade pip
Install python3-venv:
py -m pip install virtualenv
Then create the folder for allocate the virtual environment:
py -m virtualenv env
Then activate the virtual env:
Set-ExecutionPolicy Unrestricted -Scope Process (run if UnauthorizedAccess in powershell console)
.\venv\Scripts\activate.ps1
Now you can install python libs as you need it

Check our current installed packages:
py -m pip list
De-activate virtual env:
deactivate

# set up

Configure all your dependencies in Pipfile.
See: https://pypi.org/

# launch

## Unix

python3 morse/app.py

## Windows

py morse/app.py
