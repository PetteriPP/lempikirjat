import db


def add_comment(review_id, user_id, content):
    sql = """INSERT INTO comments (review_id, user_id, content)
             VALUES (?, ?, ?)"""
    db.execute(sql, [review_id, user_id, content])


def get_comments(review_id):
    sql = """SELECT comments.id, comments.content, comments.sent_at,
                    users.id AS user_id, users.username
             FROM comments
             JOIN users ON users.id = comments.user_id
             WHERE comments.review_id = ?
             ORDER BY comments.id"""
    return db.query(sql, [review_id])
