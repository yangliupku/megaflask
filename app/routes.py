from app import app
from flask import render_template, flash, redirect, url_for
from app.login import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "yliu"}
    posts = [
        {"author": {"username": "user1"}, "body": "foo"},
        {"author": {"username": "user2"}, "body": "bar"},
    ]
    return render_template("index.html", title="microblog", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login Requested. Username={form.username.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)

