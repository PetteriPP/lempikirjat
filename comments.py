import db


def add_comment(review_id, user_id, content):
    sql = """INSERT INTO comments (review_id, user_id, content)
             VALUES (?, ?, ?)"""
    db.execute(sql, [review_id, user_id, content])
