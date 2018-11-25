COP-4045 Python FinalProject

Getting Started.
Install at minimum python 3.5x. Install python flask. Have Sqlite3 installed. Sqlite3 for python comes standard with python installation.

Project structure.
shopping            # main python code folder
    db              # database python module, and sqlite3 database.
    business        # middle/business tier python objects
    test            # python testing programs
    web             # python/flask web files

Database initialization.
cd ./shopping/db
sqlite3 _products.db < create_shopping_db.sql

To run application
cd to application root (from where git project was downloaded)
python -m shopping.web.main
