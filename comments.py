import db
import pagination


def add_comment(review_id, user_id, content):
    sql = """INSERT INTO comments (review_id, user_id, content)
             VALUES (?, ?, ?)"""
    db.execute(sql, [review_id, user_id, content])


def count_comments(review_id):
    sql = "SELECT COUNT(*) FROM comments WHERE review_id = ?"
    return db.query(sql, [review_id])[0][0]


def get_comments(review_id, page=1):
    sql = """SELECT comments.id, comments.content, comments.sent_at,
                    users.id AS user_id, users.username
             FROM comments
             JOIN users ON users.id = comments.user_id
             WHERE comments.review_id = ?
             ORDER BY comments.id
             LIMIT ? OFFSET ?"""
    params = [review_id, pagination.PAGE_SIZE, (page - 1) * pagination.PAGE_SIZE]
    return db.query(sql, params)
