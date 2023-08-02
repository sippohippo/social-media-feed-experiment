from flask import Flask, render_template, redirect, request, session, make_response
import usertools
from app import app

# move these later
from database import db
from sqlalchemy.sql import text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if usertools.login(email, password):
            return redirect("/")
        return render_template("invalid.html")


@app.route("/newuser",methods=["GET", "POST"])
def newuser():
    if request.method == "GET":
        return render_template("newuser.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if usertools.newuser(email, password):
            return redirect("/")
        return render_template("invalid.html")


@app.route("/admin")
def admin():
    return "Admin page"


@app.route("/experiment")
def experiment():

    # REMOVE later, testing only
    sql = text("SELECT data FROM images WHERE id=1")
    result = db.session.execute(sql, {"id":id})
    data = result.fetchone()[0]
    response = make_response(bytes(data))
    response.headers.set("Content-Type", "image/jpeg")
    return response
#    return "Page 3"


@app.route("/logout")
def logout():
    del session["email"]
    del session["user_id"]
    return redirect("/")
