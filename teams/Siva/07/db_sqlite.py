import json
import sqlite3
# import pandas as pd
# from pandas import DataFrame

traffic = json.load(open('gandhi.json'))
columns = list(traffic.keys())
# print(columns)


db = sqlite3.connect('test.db')
c = db.cursor()
c.execute('''create table gandhi
         (id text primary key,
          content text,
          author text,
          length integer)''')
          
for el in traffic['results']:
    c.execute('insert into gandhi values (?, ?, ?, ?)',
    [el['_id'], el['content'], el['author'], el['length']])
    db.commit()

c.execute('''
SELECT *
FROM gandhi''')
# df = DataFrame(c.fetchall(), columns=['id','content','author', 'length'])
print (' ---- > ', c.fetchall())

db.close()