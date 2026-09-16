import db

def add_review(title, author, description, rating, user_id ):
    sql = "INSERT INTO reviews (title, author, description, rating, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, author, description, rating, user_id])