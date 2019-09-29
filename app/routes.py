from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "yliu"}
    return render_template("index.html", title="microblog", user=user)

