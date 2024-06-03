'''
This Python script requires an external dependency (pandas),
so we'll need a project virtual environment.

Note: pandas now requires pyarrow to be installed as well.

For Windows, my commands are:

py -m venv .venv
.venv\Scripts\Activate
py -m pip install pandas pyarrow
py book_manager.py
'''

# Import from Python Standard Library first
import sqlite3
import pathlib

# Import from external packages
import pandas as pd

# Define paths using joinpath
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql").joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")


def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            print(f"Creating folder: {folder}")
            folder.mkdir(parents=True, exist_ok=True)
        else:
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"Error inserting data: {e}")

def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)
    
    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()
