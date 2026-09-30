import db

def get_classes():
    sql = "SELECT id, kind, name FROM classes ORDER BY kind, name"
    return db.query(sql)


def get_review_classes(review_id):
    sql = """SELECT classes.id, classes.kind, classes.name
             FROM classes
             JOIN review_classes ON review_classes.class_id = classes.id
             WHERE review_classes.review_id = ?
             ORDER BY classes.kind, classes.name"""
    return db.query(sql, [review_id])


def add_review(title, author, description, rating, user_id, class_ids):
    con = db.get_connection()
    try:
        sql = """INSERT INTO reviews (title, author, description, rating, user_id)
                 VALUES (?, ?, ?, ?, ?)"""
        result = con.execute(sql, [title, author, description, rating, user_id])
        review_id = result.lastrowid
        sql = "INSERT INTO review_classes (review_id, class_id) VALUES (?, ?)"
        con.executemany(sql, [(review_id, class_id) for class_id in class_ids])
        con.commit()
        return review_id
    finally:
        con.close()

def get_reviews():
    sql = "SELECT id, title FROM reviews"
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
    result = db.query(sql, [review_id])
    return result[0] if result else None

def update_review(review_id, title, author, description, rating, class_ids):
    sql = """ UPDATE reviews SET title = ?,
                                 author = ?,
                                 description = ?,
                                 rating = ?
                            WHERE id = ?"""
    con = db.get_connection()
    try:
        con.execute(sql, [title, author, description, rating, review_id])
        con.execute("DELETE FROM review_classes WHERE review_id = ?", [review_id])
        sql = "INSERT INTO review_classes (review_id, class_id) VALUES (?, ?)"
        con.executemany(sql, [(review_id, class_id) for class_id in class_ids])
        con.commit()
    finally:
        con.close()

def delete_review(review_id):
    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])

def search_reviews(query):
    sql = """SELECT id, title
             FROM reviews
             WHERE title LIKE ?
             OR author LIKE ?
             OR description LIKE ?
             OR rating LIKE ?
             ORDER BY id DESC"""
    search = "%" + query + "%"
    return db.query(sql, [search, search, search, query])


def get_user_reviews(user_id):
    sql = """SELECT id, title
             FROM reviews
             WHERE user_id = ?
             ORDER BY id DESC"""
    return db.query(sql, [user_id])
