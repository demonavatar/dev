import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS wrappers(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT,
wrapper_id INTEGER UNIQUE,
FOREIGN KEY(wrapper_id) REFERENCES wrappers(id)
);
''')
con.commit()
con.close()