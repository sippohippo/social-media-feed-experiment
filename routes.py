from flask import Flask, render_template, redirect, request, session, make_response
import usertools
import experimenttools
from app import app


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
        return render_template("invalid.html", message="Invalid username or password!")


@app.route("/newuser",methods=["GET", "POST"])
def newuser():
    if request.method == "GET":
        return render_template("newuser.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if usertools.newuser(email, password):
            return redirect("/")
        return render_template("invalid.html",
                message="An account associated with this email already exists!")


@app.route("/admin")
def admin():
    return "Admin page"


@app.route("/experiment",methods=["GET", "POST"])
def experiment():
    profiles = experimenttools.select_posts(3)
    return render_template("experiment.html", profiles=profiles)


@app.route("/logout")
def logout():
    del session["email"]
    del session["user_id"]
    return redirect("/")
