import sqlite3

con = sqlite3.connect('films.sqlite')
cur = con.cursor()

cur.execute('''
SELECT movies.name,
       slogans.name
FROM movies,slogans

''')

for result in cur:
    print(result)

con.commit()
con.close()