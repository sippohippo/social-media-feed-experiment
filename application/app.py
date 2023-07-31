from flask import Flask
from flask import render_template, render_template, request
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)

app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    username = request.form["username"]
    password = request.form["password"]
    # TODO: check username and password
    session["username"] = username
    return redirect("/main")

@app.route("/newuser")
def newuser():
    return redirect("/main")

@app.route("/main")
def main():
    return "Page 2"

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
