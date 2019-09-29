from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "yliu"}
    posts = [
        {"author": {"username": "user1"}, "body": "foo"},
        {"author": {"username": "user2"}, "body": "bar"},
    ]
    return render_template("index.html", title="microblog", user=user, posts=posts)

