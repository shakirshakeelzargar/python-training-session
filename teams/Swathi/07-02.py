import sqlite3
import json
import os
import time
def read_json_file(filepath):
    '''
    read_json_file() takes one arugument,returns quotes list from json data
    '''
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
        results=data.get("results",None)
        res_list=results[:]
        res = [ sub['content'] for sub in res_list ] 
    return res

data=read_json_file("gandhi.json")
print(data)
conn=sqlite3.connect("test.db")

def create_table():
    c=conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS QUOTES(quotes TEXT)')
# def data_entry():
#     c=conn.cursor()
#     c.execute("INSERT INTO QUOTES VALUES('Nothing is impossible, everything is possible')")
#     conn.commit()
#     c.close()
    
def dynamic_data_entry(data):
    c=conn.cursor()
    c.execute("INSERT INTO QUOTES (quotes) VALUES (?)",(data,))
    #print("inserted records succefully")
    conn.commit()
    c.close()
def get_quotes():
    '''
    getting data from db
    '''
    c=conn.cursor()
    cursor = c.execute("SELECT quotes from QUOTES")
    for row in cursor:
        print(f"quote : {row}")
    conn.commit()
    c.close()

create_table()
#data_entry()
for i in data:
    dynamic_data_entry(i)
    time.sleep(1)
get_quotes()
conn.close()
