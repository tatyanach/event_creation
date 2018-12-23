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
        age INTEGER,  
        photo URL,
        preferences TEXT,
        alcohol TEXT,
        cigarettes TEXT
) 
''')
conn.commit()

c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (1, "vasya", "Vasily", 19, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (2, "dimon", "Dimitrii", 22, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (3, "pumba", "Artem", 18 , https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"no", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (4, "losyash", "Aleksey", 19, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (5, "alcoholic", "Alexander", 24, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (6, "nothappy", "Ruslan", 20, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"no", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (7, "mr1", "Vladimir", 21, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (8, "mr2", "Oleg", 23, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (9, "mr3", "Misha", 25, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (10, "mr4", "Vlad", 26, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"no", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (11, "mr5", "Pasha", 27, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (12, "mr66", "Daniil", 26, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (13, "mr777", "Petr", 25, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (14, "mr88", "Andrey", 24, https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa ,"no", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (15, "mr9999", "Ilya", 23, madata:ige/jpeg;base64,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,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (16, "mrs1", "Masha", 19,data:image/jpeg;base64,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 ,"yes", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (17, "mrs22", "Frosya", 22 ,"no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (18, "mrs333", "Mila", 18, "no", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (19, "mrs4you", "Lena", 22 ,"no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (20, "mrs5", "Tanya", 24 ,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (21, "mrs666", "Nastya", 25, ,"yes", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (22, "mrs7", "Diana", 19 ,"no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age,alcohol, cigarettes) VALUES (23, "mrs88", "Sasha", 20,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (24, "mrs9", "Dasha", 21 ,"yes", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age,alcohol, cigarettes) VALUES (25, "mrss1", "Liza", 24,"no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (26, "mrss22", "Olya", 27,"no", "no")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (27, "mrsss3", "Galya", 18,,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (28, "mrs4mr", "Zina", 25,"yes", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (29, "mrsss555", "Frosya", 22, "no", "yes")
conn.commit()
c.execute("INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (30, "mrssss6", "Ira", 23 ,"yes", "yes")
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

# Our base data for friends
c.execute("INSERT INTO friends (user1, user2) VALUES (2, 1)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (1, 2)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (3, 1)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (1, 3)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (2, 3)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (3, 2)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (3, 4)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (4, 3)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (4, 2)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (2, 4)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (1, 4)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (4, 1)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (9, 3)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (3, 9)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (10, 1)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (1, 10)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (11, 12)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (12, 11)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (12, 3)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (3, 12)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (2, 11)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (11, 2)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (13, 14)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (14, 13)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (14, 15)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (15, 14)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (13, 15)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (15, 13)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (16, 17)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (17, 16)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (16, 18)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (18, 16)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (19, 20)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (20, 19)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (20, 16)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (16, 20)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (21, 20)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (20, 21)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (21, 23)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (23, 21)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (22, 21)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (21, 22)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (24, 26)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (26, 24)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (3, 21)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (21, 3)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (27, 1)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (1, 27)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (2, 28)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (28, 2)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (27, 28)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (28, 27)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (29, 11)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (11, 29)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (30, 12)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (12, 30)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (29, 30)")
conn.commit()
c.execute("INSERT INTO friends (user1, user2) VALUES (30, 29)")
conn.commit()
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
    e_description TEXT, 
    e_creator INTEGER,  
    e_place TEXT, 
    e_date TEXT, 
    e_time TEXT, 
   
) 
''')
conn.commit()


c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (1, "Flat party", "Come to party and don`t forget some drinks!", 1, "Saint-Petersburg, Nevskyi prospect 60, 137 flat", "20 November 2018", "21:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (2, "New Year party", "Santa Claus will wait you at our party!Come with friends and take presents!", 3, "Leningradskaya oblast`, Murino, Veselaya, street house 20", "31 December 2018", "21:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (3, "Halloween night", "Spend this night of horror and fear in costumed party!", 10, "Sain-Petersburg, Nevskyi prospect 99, 999 flat", "31 October 2018", "17:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (4, "Reading evening", "Come to our flat with your favorite books and read and discuss them", 1, "Sain-Petersburg, Ligovskyi prospect 77, 177 flat", "22 December 2018", "18:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (5, "Chess event", "Let`s play chess, watch films and drink coffee!", 15, "Saint-Petersburg, Dachnyi prospect 33 k.2 , 68 flat", "20 September 2018", "16:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (6, "Mafia game", "Come to play Mafia and drink whiskey", 7, "Saint-Petersburg, Lesnoi prospect 11, 167 flat", "20 June 2018", "21:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (7, "Poetic evening", "Are you writing poems? Come to us and share!", 30, "Saint-Petersburg, Lensoveta street 23, 12 flat", "23 December 2018", "16:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (8, "Football match looking", "Are you going to look the next football game? Come to us, let`s watch it together!", 8, "Saint-Petersburg, Bakunina 5, Hooligan`s pub", "11 February 2019", "23:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (9, "Sing and drink", "Are you loving to sing songs? Let`s drink and sing together!", 12, "Saint-Petersburg, Chernyshebskaya 60, Karaoke bar Nebo", "24 March 2019", "21:00" )
''')
conn.commit()
c.execute('''
    INSERT INTO event(e_id,e_name, e_description, e_creator, e_place,e_date,e_time)
    VALUES (10, "Dog club", " Have a dog? Come together and and fun!", 16, "Saint-Petersburg, Pushkinskaya 54, office 23", "25 april 2019", "12:00" )
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
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (1, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (2, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (4, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (5, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (7, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (6, 8)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (8, 8)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (9, 7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (10, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (11, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (12, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (13, 9)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (14, 8)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (15,7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (16, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (17, 5)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (18, 4)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (19, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (20, 2)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (21, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (22, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (23, 2)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (24, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (25, 4)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (26, 5)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (27, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (28, 7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (29, 8)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (30, 9)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (30, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (30, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (29, 2)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (28, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (27, 4)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (26, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (25, 2)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (24, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (23, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (22, 2)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (21, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (20, 4)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (19, 5)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (18, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (17, 7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (16, 8)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (15, 9)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (14, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (13, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (12, 2)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (11, 3)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (10, 4)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (9, 5)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (8, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (7, 7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (6, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (5, 9)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (4, 8)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (3, 7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (2, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (1, 5)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (5, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (10, 9)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (15, 10)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (20, 7)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (25, 1)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (30, 6)")
conn.commit()
c.execute("INSERT INTO users_events (user_id, event_id) VALUES (2, 10)")
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
