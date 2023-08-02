from database import db
from sqlalchemy.sql import text
from random import sample

def select_profiles(n):
    pass


def select_real_posts(n):
    query = text("""
            SELECT r.name, r.handle, r.content, i.data
            FROM real_posts r, images i
            WHERE r.profilePicId = i.id
            """)
    result = db.session.execute(query).fetchall()
    return sample(result, n)


def select_fake_posts(n):
    pass