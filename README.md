# FastAPI---Postgresql

FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface.

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.

An updated version of this uses the latest version of FastAPI and SQLAlchemy and its source code is here
 
Setting up the database
Install PostgreSQL and create your user and database

Change this line in database.py to

engine=create_engine("postgresql://{YOUR_DATABASE_USER}:{YOUR_DATABASE_PASSWORD}@localhost/{YOUR_DATABASE_NAME}",
    echo=True
)
Create a virtual environment
This can be done with python -m venv env

activate the virtual environment with

env/bin/activate
or

env\Scripts\activate
Install the requirements
pip install -r requirements.txt
Create the database
python create_db.py

Install FastAPI, Uvicorn
Run the API
-m uvicorn test:app --reload 
