
This application allows users from all over the world to create their own tables with the necessary fields in the database and interact with them.

Author: Siarhei Harelik <kelinsobw@gmail.com>

Source link: https://github.com/kelinsobw/socialnote

Requirements:

    Python 3.8, PostgreSQL 12.9


Setup dev environment
---------------------

1. Install base system packages (second line for production servers)

        $ sudo apt-get install -y wget python3-pip python3-dev postgresql



2. Install [Python 3.8](https://www.python.org/downloads/source/)
   
3. Install [Postgres server](https://www.postgresql.org/download/linux/ubuntu/)



Build and run app in dev mode
-----------------------------

1. Create virtual environment and install project dependencies

        $ python3.9 -m venv --prompt="mnt" .venv/
        $ source ../venv/bin/activate
        $ pip install -r requirements.txt


2. Create user and database

        $ sudo su postgres && psql
        # CREATE USER note WITH PASSWORD 'note' CREATEDB;

        $ psql -h localhost -U note
        # CREATE DATABASE manti_by;


4. Migrate, collect static files and create admin user

        $ ./manage.py makemigrations
        $ ./manage.py migrate
        $ ./manage.py createsuperuser


5. Run local development server

        $ ./manage.py runserver 127.0.0.1:8000


