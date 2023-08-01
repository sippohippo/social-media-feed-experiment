from app import app
from flask import Flask, render_template, redirect, request, session
import usertools

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
	    else:
	    	return "error"	    	
	    return redirect("/")


@app.route("/newuser",methods=["GET", "POST"])
def newuser():
    if request.method == "GET":
    	return render_template("newuser.html")

    if request.method == "POST":
	    email = request.form["email"]
	    password = request.form["password"]
	    if usertools.newuser(email, password):
	    	return redirect("/")
	    else:
	    	return "error"


@app.route("/admin")
def admin():
    return "Admin page"


@app.route("/experiment")
def experiment():
    return "Page 3"


@app.route("/logout")
def logout():
    del session["email"]
    del session["user_id"]
    return redirect("/")
