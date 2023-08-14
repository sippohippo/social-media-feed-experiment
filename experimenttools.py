from flask import session
from random import sample, randint, shuffle
from database import db
from sqlalchemy.sql import text

def select_posts(n_posts):
    query = text("""
            SELECT p.name, p.handle, p.content, p.type, i.id, p.id
            FROM posts p, images i
            WHERE p.profilePicId = i.id
            """)
    result = db.session.execute(query).fetchall()
    posts = sample(result, n_posts)
    shuffle(posts)
    return posts


def select_image(id):
    query = text("""
            SELECT data
            FROM images
            WHERE id=:id
            """)
    result = db.session.execute(query, {"id":id})
    data = result.fetchone()[0]
    return data


def record_votes(profiles, votes):
    profilesIds = []
    profileLabel = []
    total_correct = 0

    for i in profiles:
        profilesIds.append(i[5])
        label = i[3]
        if label == "bot":
            profileLabel.append("TRUE")
        else:
            profileLabel.append("FALSE")

    for i in range(0, len(votes)):
        vote = votes[i]
        post = profilesIds[i]
        true_label = profileLabel[i]
        if vote == true_label:
            total_correct += 1

        user = session["user_id"]
        query = text("""
                INSERT INTO votes (isBot, postId, userId)
                VALUES (:isBot, :postId, :userId)
                """)
        db.session.execute(query, {"isBot":vote, "postId":post, "userId":user})
    db.session.commit()
    return round(total_correct/len(profiles), 2)*100


def record_accuracy(accuracy):
    pass
