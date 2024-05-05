# School Management
School Management is a Python application designed to for school registration management..

## Technologies Used
- Python: The core programming language used for backend development.

- Django: Framework for building and running web applications using Python.

- Django REST framework: Powerful and flexible toolkit for building Web APIs.

- PostgreSQL: Relational database management system used to store data.


# Getting Started
Clone the Repository:
```
git clone https://github.com/andreappereira/school_management.git
```
## Run the PostgreSQL Database with Docker Compose:

Navigate to the root directory of the project.
Run the following command to start the PostgreSQL database using Docker Compose:
```
docker-compose up -d
```
## Set Up the Application:

Open the settings.py file located in setup.
Configure the database connection properties to match the PostgreSQL database running in Docker Compose.

## Create virtual environment
Unix/MacOS:
```
python3 -m venv ./venv
```

Windows:
```
py -m venv ./venv
```

## Activate the environment
Unix/MacOS:
```
source venv/bin/activate
```

Windows:
```
venv\Scripts\activate.bat
```

##  Install all dependencies:
```
pip install -r requirements.txt
```

## Migrate
Run the migrate command:
```
python manage.py migrate
```

##  Run the Application:
```
python manage.py runserver
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.
