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
    c.execute("SELECT * FROM users")
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
    c.execute("SELECT * FROM users WHERE login='%s'" % login)
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
        c.execute("SELECT * FROM users where login='%s'" % users['login'])
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
        c.execute("SELECT * FROM users where login='%s'" % user['login'])
        if c.fetchone():
            error_message = "user_exists"
            return render_template("add_user2.html")
        else:
            c.execute("INSERT INTO users "
                      "(login, name, age, photo, alcohol, cigarettes) "
                      "VALUES "
                      "('{login}','{name}','{age}','{photo}','{alcohol}','{cigarettes}'"
                      "".format(**user))
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


@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('search_results.html', q=q, users=users)

app.run()


