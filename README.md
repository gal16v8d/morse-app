# morse-app

# Get started

## Unix
Install python3-venv:
sudo apt install python3-venv
Then create the folder for allocate the virtual environment:
python3 -m venv venv
Then activate the virtual env:
source venv/bin/activate
Now you can install python libs as you need it

Check our current installed packages:
pip list
De-activate virtual env:
deactivate

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
For generate requirements.txt file please execute:
pip3 freeze > requirements.txt

# launch
## Unix
python3 app.py
## Windows
py app.py