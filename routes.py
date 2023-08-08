from flask import Flask, render_template, redirect, request, session, make_response
import usertools
import experimenttools
from app import app
import base64


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


@app.route("/experiment",methods=["GET", "POST"])
def experiment():
    profiles = experimenttools.select_posts(3)
    images = []
    for i in range(len(profiles)):
        image = profiles[i][4]
        response = make_response(bytes(image))
        images.append(response.headers.set("Content-Type", "image/jpeg"))
        #images.append(image)

    if request.method == "GET":
        return render_template("experiment.html", profiles=list((zip(profiles,images))))
    if request.method == "POST":
        return render_template("result.html", profiles=profiles)


@app.route("/admin")
def admin():
    return "Admin page"


@app.route("/logout")
def logout():
    del session["email"]
    del session["user_id"]
    return redirect("/")
