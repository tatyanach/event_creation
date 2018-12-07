import sqlite3
# Connect ot Database - in local file app.db
conn = sqlite3.connect('app.db')
# Create a cursor - a
c = conn.cursor()
c.execute('''  
CREATE TABLE users( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        login TEXT,
        name TEXT, 
        city TEXT, 
        age INTEGER,  
        photo URL,
        preferences TEXT,
        alcohol TEXT,
        cigarettes TEXT,
        description TEXT,
        friends INTEGER
) 
''')
conn.commit()

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

c.execute('''
    INSERT INTO users(name, city, age)
    VALUES ("Nastya", "SPb", "26")
''')
conn.commit()


c.execute('''
    UPDATE users
    SET login="nastya"
    WHERE name="Nastya"
''')
conn.commit()



# Our base data
users = [
    {
        'login': 'nastya',
        'name': 'Nastya',
        'city': 'SPB',
        'age': '26'
    },
    {
        'login': 'ivan',
        'name': 'Ivan Kapustin',
        'city': 'SPB',
        'age': '25'
    }
]

c.execute('''
    INSERT INTO event (e_name, e_date, e_place)
    VALUES ("Party","2019-01-10 21:00:00", "Bar")
''')
conn.commit()

# Many to many connection
c.execute('''
CREATE TABLE users_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        event_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (event_id) REFERENCES event(e_id)
)
''')

conn.commit()


c.execute("INSERT INTO users_events (user_id, event_id) VALUES (1, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (3, 1)")
conn.commit()


c.execute("SELECT u.* "
          "FROM users_events ue "
          "JOIN users u ON (u.id=ue.user_id) "
          "WHERE ue.event_id=1")


conn.close()