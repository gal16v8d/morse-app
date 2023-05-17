# morse-app

Converts an user input into its morse equivalent

# Get started

## Unix

Install pipenv:

```bash
sudo apt install python3-venv
pip3 install pipenv
```

Then create the folder for allocate the virtual environment:

```bash
mkdir .venv
```

Launch pipenv:

```bash
pipenv install
```

Then activate the virtual env:

```bash
pipenv shell
```

Run command inside virtualenv:

```bash
pipenv run
```

Exit virtual env:

```bash
exit
```

or

```bash
deactivate
```

## Windows

Update pip:

```bash
py -m pip install --upgrade pip
```

Install python3-venv:

```bash
py -m pip install virtualenv
```

Then create the folder for allocate the virtual environment:

```bash
py -m virtualenv env
```

Optional (run if UnauthorizedAccess in powershell console):

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate the virtual env:

```bash
.\venv\Scripts\activate.ps1
```

Now you can install python libs as you need it

# set up

Configure all your dependencies in Pipfile.
See: [Pypi](https://pypi.org/)

# dependencies

For generate requirements.txt file please execute:

```bash
pip3 freeze > requirements.txt
```

# launch

## Unix

```bash
python3 morse/app.py
```

## Windows

```bash
py morse/app.py
```
