import os
import sqlite3

# Define the path to the database file in the project folder
DB_PATH = os.path.join(os.path.dirname(__file__), "dinopark.db")


def init_db() -> None:
    """Creates the database file and the dinosaurs table
    if they don't exist.
    """
    # Connecting to the database (if the file doesn't exist,
    # sqlite3 will create it)
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    # Creating a table using SQL
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dinosaurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        type TEXT NOT NULL,
        golden_chest INTEGER NOT NULL,
        totems INTEGER NOT NULL,
        lvl_1 INTEGER DEFAULT 0,
        lvl_2 INTEGER DEFAULT 0,
        lvl_3 INTEGER DEFAULT 0,
        lvl_4 INTEGER DEFAULT 0,
        lvl_5 INTEGER DEFAULT 0,
        lvl_6 INTEGER DEFAULT 0
    )
    """)

    # Saving changes to the file and closing the connection
    connection.commit()
    connection.close()
    print(True)  # Information that the database has been initialized


if __name__ == "__main__":
    init_db()
