from random import sample, randint, shuffle
from database import db
from sqlalchemy.sql import text

def select_posts(n_posts):
    query = text("""
            SELECT p.name, p.handle, p.content, p.type, i.data
            FROM posts p, images i
            WHERE p.profilePicId = i.id
            """)
    result = db.session.execute(query).fetchall()
    posts = sample(result, n_posts)
    shuffle(posts)
    return posts
