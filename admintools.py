from flask import session
from database import db
from sqlalchemy.sql import text


def get_participants():
    query = text("""
            SELECT DISTINCT email
            FROM users
            WHERE id IN (
                SELECT DISTINCT userId
                FROM results
                )
            """)
    result = db.session.execute(query)
    participants = result.fetchall()
    return participants    


def total_responses():
    query = text("""
            SELECT COUNT(id)
            FROM results
            """)
    result = db.session.execute(query)
    count = result.fetchone()[0]
    return count


def average_accuracy():
    query = text("""
            SELECT AVG(accuracy)
            FROM results
            """)
    result = db.session.execute(query)
    accuracy = result.fetchone()[0]
    return accuracy    


def remove_user(userId):
    query = text("""
            DELETE FROM votes
            WHERE userId=:userId
            """)
    db.session.execute(query, {"userId":userId})
    
    query = text("""
            DELETE FROM results
            WHERE userId=:userId
            """)
    db.session.execute(query, {"userId":userId})

    query = text("""
            DELETE FROM users
            WHERE id=:userId
            """)
    db.session.execute(query, {"userId":userId})

    db.session.commit()
    

def get_id(email):
    query = text("""
            SELECT id
            FROM users
            WHERE email=:email
            """)
    result = db.session.execute(query, {"email":email})
    userId = result.fetchone()
    return userId
