import db

def add_review(title, author, description, rating, user_id ):
    sql = "INSERT INTO reviews (title, author, description, rating, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, author, description, rating, user_id])

def get_reviews():
    sql = "SELECT * FROM reviews"
    return db.query(sql)

def show_review(review_id):
    sql = """SELECT 
                    reviews.id,
                    reviews.title,
                    reviews.author,
                    reviews.description,
                    reviews.rating,
                    users.id user_id,
                    users.username
            FROM reviews, users
            WHERE reviews.user_id = users.id AND
                reviews.id = ?""" 
    return db.query(sql, [review_id])[0]

def update_review(review_id, title, author, description, rating):
    sql = """ UPDATE reviews SET title = ?,
                                 author = ?,
                                 description = ?,
                                 rating = ?
                            WHERE id = ?"""
    db.execute(sql, [title, author, description, rating, review_id])

def delete_review(review_id):
    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])