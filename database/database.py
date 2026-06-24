import sqlite3
connection = sqlite3.connect("orion.db")
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS documents(
id INTEGER PRIMARY KEY,
title TEXT,
category TEXT
)
""")
connection.commit()
connection.close()