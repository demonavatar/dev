import sqlite3

con = sqlite3.connect('ice.sqlite')
cur = con.cursor()

cur.execute('''
SELECT ice_cream.name, toppings.name
FROM ice_cream_toppings
JOIN ice_cream ON ice_cream.id = ice_cream_toppings.ice_cream_id
JOIN toppings ON toppings.id = ice_cream_toppings.topping_id
ORDER BY ice_cream.name
''')

for result in cur:
    print(result)

con.commit()
con.close()