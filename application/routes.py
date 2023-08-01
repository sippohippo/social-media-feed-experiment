from app import app
from flask import Flask
from flask import render_template, redirect, request

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
	    return redirect("/")

@app.route("/newuser",methods=["GET", "POST"])
def newuser():
    if request.method == "GET":
    	return render_template("newuser.html")

    if request.method == "POST":
	    email = request.form["email"]
	    password = request.form["password"]
	    return redirect("/")   

@app.route("/admin")
def admin():
    return "Admin page"

@app.route("/experiment")
def experiment():
    return "Page 3"

@app.route("/logout")
def logout():
    del session["email"]
    return redirect("/")
