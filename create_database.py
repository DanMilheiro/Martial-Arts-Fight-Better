import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('C:\\Users\\Service 2\\Martial-Arts-Fight-Better\\mma_fighters.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table for fighters
cursor.execute('''
CREATE TABLE IF NOT EXISTS fighters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    nickname TEXT,
    division_title TEXT,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    height REAL,
    weight REAL,
    reach REAL,
    fighting_style TEXT,
    age INTEGER,
    hometown TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
