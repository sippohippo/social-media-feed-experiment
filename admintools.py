from flask import session
from database import db
from sqlalchemy.sql import text


def get_participants():
    query = text("""
            SELECT DISTINCT email
            FROM users
            WHERE id IN (
                SELECT DISTINCT id
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


def add_post():
    pass


def remove_user(userId):
    pass
