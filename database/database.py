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
cursor.execute("""
CREATE TABLE IF NOT EXISTS knowledge(
id INTEGER PRIMARY KEY,
filename TEXT,
chunk TEXT
)
""")
connection.commit()
connection.close()