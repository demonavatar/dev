import sqlite3

con = sqlite3.connect('db1.sqlite')
cur = con.cursor()

cur.executescript('''
DROP TABLE ice_cream;

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY
);

ALTER TABLE ice_cream
ADD is_published BOOLEAN;
ALTER TABLE ice_cream
ADD is_on_main BOOLEAN;
''')

con.commit()
con.close()