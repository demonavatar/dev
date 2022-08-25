import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
# cur.execute('''
# CREATE TABLE IF NOT EXISTS ice_cream(
#     is_published INTERGER,
#     name TEXT,
#     release_year TEXT
# );
# ''')

cur.execute('''
CREATE TABLE IF NOT EXISTS directors(
    id INTEGER PRIMARY KEY,
    name TEXT,
    bithday_year INTEGER
);
''')
cur.execute('''
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    release_year INTEGER
);
''')

# cur.executescript('''
# INSERT INTO ice_cream VALUES(1, 'BRAT', 1992);
# INSERT INTO ice_cream VALUES(1, 'BRAT2', 1998);
# INSERT INTO ice_cream VALUES(1, 'BRAT3', 2005);
# ''')

# cur.execute('''
# DELETE FROM ice_cream;
# ''')


cur.execute('''
SELECT name, COUNT(*)
FROM ice_cream
GROUP BY name;
''')

for result in cur:
    print(result)
con.commit()  
con.close()