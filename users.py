import db


def get_user(user_id):
    sql = """SELECT u.id, u.username, COUNT(r.id) AS review_count
             FROM users u LEFT JOIN reviews r ON r.user_id = u.id
             WHERE u.id = ?
             GROUP BY u.id, u.username"""
    result = db.query(sql, [user_id])
    return result[0] if result else None
