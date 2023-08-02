from database import db
from sqlalchemy.sql import text
from random import sample, randint, shuffle

def select_posts(n):
    fake_posts = []
    real_posts = []
    n_real = randint(0, n)
    n_fake = n-n_real
    
    if n_real >0:
        real_posts = select_real_posts(n_real)
    
    if n_fake >0:
        fake_posts = select_fake_posts(n_fake)

    posts = real_posts+fake_posts
    shuffle(posts)

    return posts


def select_real_posts(n):
    query = text("""
            SELECT r.name, r.handle, r.content, i.data
            FROM real_posts r, images i
            WHERE r.profilePicId = i.id
            """)
    result = db.session.execute(query).fetchall()
    return sample(result, n)


def select_fake_posts(n):
    query = text("""
            SELECT pr.name, pr.handle, po.content, i.data
            FROM fake_posts po, fake_profiles pr, images i
            WHERE pr.profilePicId = i.id
            """)
    result = db.session.execute(query).fetchall()
    return sample(result, n)