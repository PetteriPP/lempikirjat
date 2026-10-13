import sqlite3
import db


def create_user(username, password_hash):
    sql = """INSERT INTO users (username, password_hash)
             SELECT ?, ?
             WHERE NOT EXISTS (
                 SELECT id FROM users WHERE casefold(username) = ?
             )"""
    try:
        return db.execute(sql, [username, password_hash, username.casefold()]) > 0
    except sqlite3.IntegrityError:
        return False


def get_user_by_username(username):
    sql = """SELECT id, username, password_hash
             FROM users
             WHERE casefold(username) = ?"""
    result = db.query(sql, [username.casefold()])
    return result[0] if result else None


def get_user(user_id):
    sql = """SELECT u.id, u.username, COUNT(r.id) AS review_count
             FROM users u LEFT JOIN reviews r ON r.user_id = u.id
             WHERE u.id = ?
             GROUP BY u.id, u.username"""
    result = db.query(sql, [user_id])
    return result[0] if result else None
