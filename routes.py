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
        if len(email) < 4:
            return render_template("invalid.html",
                    message="The provided email is too short. Please include the whole address!")
        if len(email) > 30:
            return render_template("invalid.html",
                    message="The provided email is too long. Please enter a valid email!")

        password = request.form["password"]
        passwordrepeat = request.form["passwordrepeat"]
        if password != passwordrepeat:
            return render_template("invalid.html",
                    message="The provided passwords do not match!")
        if len(password) < 4:
            return render_template("invalid.html",
                    message="The provided password is too short!")
        if len(password) > 30:
            return render_template("invalid.html",
                    message="The provided password is too long!")

        if usertools.newuser(email, password):
            return redirect("/")
        return render_template("invalid.html",
                message="An account associated with this email already exists!")


@app.route("/experiment",methods=["GET", "POST"])
def experiment():
    user = session["email"]
    if not usertools.terms_accepted(user):
        return redirect("/terms")

    votes = []
    profiles = experimenttools.select_posts(3)
    index = 1
    if request.method == "GET":
        return render_template("experiment.html", profiles=profiles)
    if request.method == "POST":
        for profile in profiles:
            vote = request.form[str(index)]
            votes.append(vote)
            index +=1
        accuracy = experimenttools.record_votes(profiles, votes)
        #experimenttools.record_accuracy(accuracy)
        #accuracy = experimenttools.accuracy(profiles, votes)
        return render_template("result.html", profiles=profiles, accuracy=accuracy)


@app.route("/admin")
def admin():
    return "Admin page"


@app.route("/logout")
def logout():
    del session["email"]
    del session["user_id"]
    return redirect("/")


@app.route("/show/<int:id>")
def show(id):
    data = experimenttools.select_image(id)
    response = make_response(bytes(data))
    response.headers.set("Content-Type", "image/jpeg")
    return response


@app.route("/terms",methods=["GET", "POST"])
def terms():
    if request.method == "GET":
        return render_template("terms.html")
    if request.method == "POST":
        response = request.form["response"]
        if response == "1":
            user = session["email"]
            usertools.accept_terms(user)
            return redirect("/experiment")
        return redirect("/")


