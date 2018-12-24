from flask import Flask
from flask import render_template
from flask import request, redirect
import db
import sqlite3
app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def hello_world():
    # Connecting to DB
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute('''
    SELECT * FROM users
    ''')
    users = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page01.html', users=users)


@app.route('/user/<login>/')
def user_page(login):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute('''
    SELECT * FROM users WHERE login="%s"''' % (login))
    user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("userpage.html", user=user_data)

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    user_in_base = False

    if request.method == 'POST':
        users = {}
        users['login'] = request.form.get('login')

        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''
        SELECT * FROM users where login="%s"''' % users['login'])
        if c.fetchone():
            user_in_base = True
            return redirect('/user/%s/' % users['login'])
        else:
            user_in_base = False

        return render_template("entry2.html")
    return render_template(
        "entry.html",
        user_in_base=user_in_base
    )

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['login'] = request.form.get('login')
        user['name'] = request.form.get('name')
        user['age'] = request.form.get('age')
        user['photo'] = request.form.get('photo')
        user['alcohol'] = request.form.get('alcohol')
        user['cigarettes'] = request.form.get('cigarettes')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''
        SELECT * FROM users where login="%s"''' % (user['login']))
        if c.fetchone():
            error_message = "user_exists"
            return render_template("add_user2.html")
        else:
            c.execute('''INSERT INTO users (login, name, age, photo, alcohol, cigarettes)
                      VALUES ('{login}','{name}','{age}','{photo}','{alcohol}','{cigarettes}')
                      '''.format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        return redirect('/user/%s/' % user['login'])


    return render_template(
        "add_user.html",
        user_created=user_created,
        error_message=error_message
    )

@app.route('/create_event', methods=['GET', 'POST'])
def create_event():

    event_created = False

    if request.method == 'POST':
        event = {}
        event['e_name'] = request.form.get('e_name')
        event['e_creator'] = request.form.get('e_creator')
        event['e_description'] = request.form.get('e_description')
        event['e_place'] = request.form.get('e_place')
        event['e_date'] = request.form.get('e_date')
        event['e_time'] = request.form.get('e_time')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute('''
        SELECT * FROM event where e_name="%s"''' % (event['e_name']))
        if c.fetchone():
            return render_template("create_event2.html")
        else:
            c.execute('''INSERT INTO event (e_name, e_creator, e_description, e_place, e_date, e_time) 
                     VALUES ('{e_name}','{e_creator}','{e_description}','{e_place}','{e_date}','{e_time}'
                     '''.format(**event))
            conn.commit()
            event_created = True
        conn.close()
        # redirect to event page
        return redirect('/event/%s/' % event['e_name'])


    return render_template(
        "create_event.html",
        event_created=event_created
    )

@app.route('/event/<e_name>/')
def event_page(e_name):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute('''
    SELECT * FROM event WHERE e_name="%s"''' % (e_name))
    event_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("eventpage.html", event=event_data)

@app.route('/search_event/<id>/')
def search_for_event(id):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute('''
    SELECT 
    DISTINCT(event_id) AS event_id, 
    COUNT(*) AS users 
    FROM users_events 
    WHERE user_id IN 
     SELECT user2 
     FROM friends 
     WHERE user1 = id 
    GROUP BY users
    '''.format(id=id))
    results = list(c.fetchall())

    # Close connection
    conn.close()
    return render_template("search_event", event=results)

@app.route('/events')
def show_events():
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()
    c.execute('''
    SELECT * FROM event
    ''')
    event_data = c.fetchall()
    conn.close()
    return render_template('events_results.html', event=event_data)

@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('search_results.html', q=q, users=users)

app.run()


