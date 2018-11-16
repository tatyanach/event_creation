from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("page01.html")

@app.route("/user/<username>")
def user_page(username):
    return render_template("with_events.html", user=username)

app.run()


