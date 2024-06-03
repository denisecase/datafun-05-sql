# datafun-05-sql

This project partially completes the requirements for [datafun-05-spec](https://github.com/denisecase/datafun-05-spec).

## Organization

The existing script assumes we will create and use two subfolders:

- `data` - to hold the .csv data files
- `sql` - to hold the .sql SQL scripts with commands for creating tables, etc.

## Python Standard Library

The project uses these packages from the Python Standard Library:

- `pathlib` - to work with folders and files
- `sqlite3` - to work with a Sqlite file-based database

If you want to avoid using a project virtual enviroment, it is possible to use the `csv` module from the Python Standard Library to read csv files. 

## External Packages & Project Virtual Environment

To work with csv files using a bit cleaner code, we choose to use pandas, an external library, not part of the Python Standard Library. 
Therefore, this project requires a project virtual environment, which we recommend creating in the .venv folder. 

Note: Installing pandas also requires installing pyarrow, so we will install both when managing our project virtual environment. 

## Suggested Commands - Windows

The following commands can be used in Windows PowerShell. 
Run one at a time, wait for each to finish. 

Create a virtual environment.

```shell
py -m venv .venv
```

Activate the virtual environment.

```shell
.venv\Scripts\Activate
```

Install pandas and pyarrow.

```shell
py -m pip install pandas pyarrow
```

Run the Python script.

```shell
py book_manager.py
```

## Suggested Commands - Mac/Linux

The following commands can be used in Mac/Linux zsh or bash shell.
Run one at a time, wait for each to finish. 

Create a virtual environment.

```shell
python3 -m venv .venv
```

Activate the virtual environment.

```shell
source .venv/bin/activate
```

Install pandas and pyarrow.

```shell
python3 -m pip install pandas pyarrow
```

Run the Python script.

```shell
python3 book_manager.py
```
