from database import db
from sqlalchemy.sql import text

def select_profiles(n):
    pass


def select_real_posts(n):
    query = text("SELECT name, handle, content, ")
    result = db.session.execute(query, {"email":email})

    return result

def select_fake_posts(n):
    pass