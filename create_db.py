import sqlite3
# Connect ot Database - in local file app.db
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('app.db')
# Create a cursor - a
c: Cursor = conn.cursor()

###OUR DATA BASE FOR USERS (contain information about each user)###

c.execute('''
CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        login TEXT,
        name TEXT, 
        age INTEGER,  
        photo URL,
        alcohol TEXT,
        cigarettes TEXT
) 
''')
conn.commit()

c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (1, "vasya", "Vasily", 19, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (2, "dimon", "Dimitrii", 22, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (3, "pumba", "Artem", 18 , "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","no", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (4, "losyash", "Aleksey", 19, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (5, "alcoholic", "Alexander", 24, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (6, "nothappy", "Ruslan", 20, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","no", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (7, "mr1", "Vladimir", 21, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (8, "mr2", "Oleg", 23, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (9, "mr3", "Misha", 25, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (10, "mr4", "Vlad", 26, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","no", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (11, "mr5", "Pasha", 27, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (12, "mr66", "Daniil", 26, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (13, "mr777", "Petr", 25, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, photo, alcohol, cigarettes) VALUES (14, "mr88", "Andrey", 24, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-psAclYTuPdzolkVtik5LTc2pIV2KIM__DnGIR108QNQT8GHa","no", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (15, "mr9999", "Ilya", 23,"yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (16, "mrs1", "Masha", 19,"yes", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (17, "mrs22", "Frosya", 22 ,"no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (18, "mrs333", "Mila", 18, "no", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (19, "mrs4you", "Lena", 22 ,"no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (20, "mrs5", "Tanya", 24 ,"yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (21, "mrs666", "Nastya", 25 ,"yes", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (22, "mrs7", "Diana", 19 ,"no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age,alcohol, cigarettes) VALUES (23, "mrs88", "Sasha", 20,"yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (24, "mrs9", "Dasha", 21 ,"yes", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age,alcohol, cigarettes) VALUES (25, "mrss1", "Liza", 24,"no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (26, "mrss22", "Olya", 27,"no", "no")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (27, "mrsss3", "Galya", 18, "yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (28, "mrs4mr", "Zina", 25,"yes", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (29, "mrsss555", "Frosya", 22, "no", "yes")
''')
conn.commit()
c.execute('''
INSERT INTO users (id, login, name, age, alcohol, cigarettes) VALUES (30, "mrssss6", "Ira", 23 ,"yes", "yes")
''')
conn.commit()



######################################################################################
############################## USER FRIENDS ##########################################
######################################################################################
# создаем базу данных - социальный граф для пар друзей, с дублированной записью для каждого отношения
c.execute('''
CREATE TABLE friends (
    user1 INTEGER,
    user2 INTEGER
)
''')
conn.commit()


c.execute('''
INSERT INTO friends (user1, user2) VALUES (2, 1)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (1, 2)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (3, 1)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (1, 3)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (2, 3)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (3, 2)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (3, 4)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (4, 3)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (4, 2)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (2, 4)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (1, 4)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (4, 1)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (9, 3)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (3, 9)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (10, 1)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (1, 10)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (11, 12)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (12, 11)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (12, 3)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (3, 12)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (2, 11)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (11, 2)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (13, 14)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (14, 13)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (14, 15)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (15, 14)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (13, 15)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (15, 13)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (16, 17)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (17, 16)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (16, 18)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (18, 16)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (19, 20)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (20, 19)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (20, 16)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (16, 20)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (21, 20)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (20, 21)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (21, 23)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (23, 21)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (22, 21)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (21, 22)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (24, 26)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (26, 24)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (3, 21)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (21, 3)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (27, 1)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (1, 27)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (2, 28)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (28, 2)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (27, 28)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (28, 27)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (29, 11)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (11, 29)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (30, 12)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (12, 30)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (29, 30)
''')
conn.commit()
c.execute('''
INSERT INTO friends (user1, user2) VALUES (30, 29)
''')
conn.commit()


# GET ALL FRIENDS
user_id = 1
c.execute('''
 SELECT user1 FROM friends WHERE user2 = {user_id}
'''.format(user_id=user_id))

all_friends = list(c.fetchall())
# выбираем список друзей определенного пользователя, сохраняем в новую переменную all_friends


###СОЗДАЕМ НОВУЮ БАЗУ ДАННЫХ ДЛЯ МЕРОПРИЯТИЙ###
c.execute(''' 
CREATE TABLE event( 
    e_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    e_name TEXT,
    e_description TEXT, 
    e_creator INTEGER,  
    e_place TEXT, 
    e_date TEXT, 
    e_time TEXT
   
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



### (Many to many connection) CREATE NEW DATABASE FOR EVENTS AND PARTICIPANTS###
c.execute('''
CREATE TABLE users_events (
        id_ue INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        event_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (event_id) REFERENCES event(e_id)
)
''')
conn.commit()


c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (1, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (3, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (1, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (2, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (4, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (5, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (7, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (6, 8)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (8, 8)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (9, 7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (10, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (11, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (12, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (13, 9)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (14, 8)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (15,7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (16, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (17, 5)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (18, 4)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (19, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (20, 2)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (21, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (22, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (23, 2)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (24, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (25, 4)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (26, 5)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (27, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (28, 7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (29, 8)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (30, 9)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (30, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (30, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (29, 2)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (28, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (27, 4)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (26, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (25, 2)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (24, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (23, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (22, 2)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (21, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (20, 4)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (19, 5)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (18, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (17, 7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (16, 8)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (15, 9)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (14, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (13, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (12, 2)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (11, 3)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (10, 4)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (9, 5)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (8, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (7, 7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (6, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (5, 9)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (4, 8)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (3, 7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (2, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (1, 5)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (5, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (10, 9)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (15, 10)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (20, 7)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (25, 1)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (30, 6)
''')
conn.commit()
c.execute('''
INSERT INTO users_events (user_id, event_id) VALUES (2, 10)
''')
conn.commit()

c.execute('''
SELECT u.* 
FROM users_events ue 
JOIN users u ON (u.id=ue.user_id) 
WHERE ue.event_id=1
''')

conn.close()

#### GET EVENTS WITH MY FRIENDS
# all_friends = [2, 3, 4, 10, 27] - we get this from DB


c.execute('''
SELECT 
DISTINCT(event_id) AS event_id, 
COUNT(*) AS users 
FROM users_events 
WHERE user_id IN 
 SELECT user2 
 FROM friends 
 WHERE user1 = {user_id}
GROUP BY users
''')

events_with_friends = list(c.fetchall())
 # выбираем все мероприятия с друзьями, сортируем мероприятия,, начиная с большим количеством друзей среди участников и заканчивая мероприятием с наименьшим количеством, сохраняем в таблицу с проранжированными мероприятиями

