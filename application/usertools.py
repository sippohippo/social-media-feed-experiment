import os
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
from flask import session
from database import db

def login(email, password):
	query = text("SELECT email, password FROM users WHERE email=:email")
	result = db.session.execute(query, {"email":email})
	user = result.fetchone()

	if email_exists(email):
		if check_password_hash(user.password, password):
			session["user_id"] = user[0]
			return True
		return False		
	return False



def newuser(email, password):
	hashed_password = generate_password_hash(password)
	if email_exists(email):
		return False

	query = text("""INSERT INTO users (email,password,admin,acceptTerms) 
	VALUES (:email,:password,FALSE,FALSE)""")
	db.session.execute(query, {"email":email, "password":hashed_password})
	db.session.commit()
	return login(email, password)


def email_exists(email):
	query = text("SELECT email FROM users WHERE email=:email")
	result = db.session.execute(query, {"email":email})
	if not result.fetchone():
		return False
	return True
