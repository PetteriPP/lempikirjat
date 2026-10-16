import random
import sqlite3
from werkzeug.security import generate_password_hash

USER_COUNT = 1000
REVIEW_COUNT = 100000
COMMENT_COUNT = 1000000


def create_users(con):
    password_hash = generate_password_hash("test-password")
    sql = "INSERT INTO users (id, username, password_hash) VALUES (?, ?, ?)"
    for user_id in range(1, USER_COUNT + 1):
        con.execute(sql, [user_id, "user" + str(user_id), password_hash])


def create_reviews(con):
    genre_ids = [row[0] for row in con.execute(
        "SELECT id FROM classes WHERE kind = ?", ["genre"])]
    theme_ids = [row[0] for row in con.execute(
        "SELECT id FROM classes WHERE kind = ?", ["theme"])]
    sql = """INSERT INTO reviews (id, title, author, description, rating, user_id)
             VALUES (?, ?, ?, ?, ?, ?)"""
    link_sql = "INSERT INTO review_classes (review_id, class_id) VALUES (?, ?)"
    for review_id in range(1, REVIEW_COUNT + 1):
        user_id = 1 if review_id % 5 == 0 else random.randint(1, USER_COUNT)
        title = "Testikirja " + str(review_id)
        author = "Kirjailija " + str(random.randint(1, 5000))
        description = ("Kirja-arvostelu " + str(review_id) + ".\n"
                       "Tämä teksti on suuren tietomäärän testaamista varten.")
        con.execute(sql, [review_id, title, author, description,
                          random.randint(1, 10), user_id])
        con.executemany(link_sql, [(review_id, random.choice(genre_ids)),
                                  (review_id, random.choice(theme_ids))])


def create_comments(con):
    sql = """INSERT INTO comments (review_id, user_id, content)
             VALUES (?, ?, ?)"""
    for comment_id in range(1, COMMENT_COUNT + 1):
        review_id = 1 if comment_id % 5 == 0 else random.randint(1, REVIEW_COUNT)
        user_id = random.randint(1, USER_COUNT)
        content = ("Testikommentti " + str(comment_id) + ".\n"
                   "Tämä kommentti kuuluu testiaineistoon.")
        con.execute(sql, [review_id, user_id, content])


def main():
    con = sqlite3.connect("database.db")
    try:
        con.execute("PRAGMA foreign_keys = ON")
        random.seed(42)
        create_users(con)
        create_reviews(con)
        create_comments(con)
        con.commit()
    finally:
        con.close()


if __name__ == "__main__":
    main()
