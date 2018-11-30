import sqlite3
conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''  
CREATE TABLE users( 
id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT, 
city TEXT, 
age INTEGER, 
alcohol BOOLEAN, 
cigarettes BOOlEAN, 
preferences TEXT,
description TEXT,
friends INTEGER,
) 
''')

c.execute(''' 
CREATE TABLE event( 
e_id INTEGER PRIMARY KEY AUTOINCREMENT, 
e_name TEXT, 
e_creator INTEGER,  
e_place TEXT, 
e_date INTEGER, 
e_time INTEGER, 
e_cluster TEXT, 
e_preferences TEXT, 
e_user_preferences TEXT,
FOREIGN KEY (e_creator) REFERENCES users(id) 
) 
''')

conn.commit()