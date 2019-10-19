from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse


@app.route("/")
@app.route("/index")
@login_required
def index():

    posts = [
        {"author": {"username": "user1"}, "body": "foo"},
        {"author": {"username": "user2"}, "body": "bar"},
    ]
    return render_template("index.html", title="microblog", posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (user is None) or (not user.check_password(form.password.data)):
            flash(f"Login Failed")
            return redirect(url_for("login"))

        next_page = request.args.get("next")
        login_user(user)
        if not next_page or url_parse(next_page).netloc != "":
            return redirect(url_for("index"))
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

