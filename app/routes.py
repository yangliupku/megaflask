from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import login_user, current_user
from app.models import User


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
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        else:
            flash(f"Login Failed")
            return redirect(url_for("login"))
    return render_template("login.html", title="Sign In", form=form)

