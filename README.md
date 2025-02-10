# datafun-05-sql

This project partially completes the requirements for [datafun-05-spec](https://github.com/denisecase/datafun-05-spec).

## Python Standard Library

The project uses these packages from the Python Standard Library:

- pathlib - to work with folders and files
- sqlite3 - to work with a Sqlite file-based database

If you want to avoid using a project virtual environment, it is possible to use the csv module from the Python Standard Library to read csv files. 

## External Packages & Project Virtual Environment

To work with csv files using a bit cleaner code, we choose to use pandas, an external library, not part of the Python Standard Library. 
Therefore, this project requires a project virtual environment, which we recommend creating in the .venv folder. 

## Organization

This project organizes SQL scripts and Python scripts into separate folders to ensure a structured and maintainable workflow for database management.

- data/ – Stores the SQLite database (db.sqlite).
- sql_create/ – Contains SQL scripts for database setup:
  - 01_drop_tables.sql – Drops any existing tables
  - 02_create_tables.sql – Creates tables
  - 03_insert_records.sql – Inserts initial data
- sql_features/ – Contains SQL scripts for feature engineering and schema modifications.
- sql_analytics/ – Contains SQL scripts for analytics queries and aggregations.

## Run Scripts

First: Create a virtual environment, activate it, and install requirements.txt (see requirements.txt for commands). 

1. Activate the .venv
2. Run the Python file 

Windows Example
```powershell
.\.venv\Scripts\activate
py db01_setup.py
```


Mac/Linux Example
```shell
source .venv/bin/activate
python3 db01_setup.py
```