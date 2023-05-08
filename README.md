## Installation
Create your virtual environment
```bash
python3.9 -m venv .env
```
Activate your virtual environment
```bash
.env/Scripts/activate
```
Install dependencies using pip package manager
```bash
pip install -r requirement.txt
```

##Configuration
configure your database with postgresql : modify DATABASES setting in 'settings.py' file

##Start Projet
To start project 
```
python manage.py migrate
python manage.py overload
```
In other terminal :
```bash
python manage.py runserver
```
