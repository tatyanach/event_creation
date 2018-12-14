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
) 
''')
conn.commit()

c.execute('''
CREATE TABLE friends (
    user1 INTEGER,
    user2 INTEGER
)
''')
conn.commit()

######################################################################################
############################## USER FRIENDS ##########################################
######################################################################################
# создаем базу данных - социальный граф для пар друзей, с дублированной записью для каждого отношения
"""
 1 2
 2 1
 2 3
 3 2
 3 4
 4 3
 3 1
 1 3
"""

# GET ALL FRIENDS
user_id = 1
c.execute("""
 SELECT user1 FROM friends WHERE user2 = {user_id}
""".format(user_id = user_id))

all_friends = list(c.fetchall())
# all_friends = [2,3]
# выбираем список друзей определенного пользователя, сохраняем в новую переменную all_friends

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

#### GET EVENTS WITH MY FRIENDS
# all_friends = [2, 3] - we get this from DB

"""
SELECT DISTINCT(event_id) AS event_id, COUNT(*) AS users FROM users_events WHERE user_id IN 
 SELECT user2 FROM friends WHERE user1 = {user_id}
GROUP BY event_id


event_id|users
14        1
23        2
"""

"""
event_id user_id
14 2
23 2
23 3
"""
 # выбираем все мероприятия с друзьями, сортируем мероприятия,, начиная с большим количеством друзей среди участников и заканчивая мероприятием с наименьшим количеством, сохраняем в таблицу с проранжированными мероприятиями


def get_events_by_friends:
    results = []
    for event in event:
        if q.lower() in user['name'].lower():
            results.append(event)
    return results
