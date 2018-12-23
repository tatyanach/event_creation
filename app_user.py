from flask import render_template
import sqlite3

USER_ID = 1

def get_diet_advice():
    conn = sqlite3.connect('app.db')
    # conn.row_factory = dict_factory
    c = conn.cursor()

    # get user diet preferences - from users table
    c.execute("SELECT * from users WHERE id = %d" % USER_ID)
    user_data = c.fetchone()

    # user_data = {"id": 1, "login": "masha", "is_vegetarian": False, "allergy_milk": True, "allergy_gluten": False}

    # filter diet advice
    c.execute("SELECT * FROM events")

    diet_advices = list(c.fetchall())
    my_advices = []

    for advice in diet_advices:
        is_allowed = True
        # filters
        if user_data['is_vegetarian'] and advice['has_meat']:
            is_allowed = False

        if user_data['allergy_milk'] and advice['has_milk']:
            is_allowed = False

        if is_allowed:
            my_advices.append(advice)

    # Close connection
    conn.close()
    return render_template("user_diet_advices.html", diet_advices=my_advices)
