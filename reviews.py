import db
import pagination

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
    sql = """INSERT INTO reviews (title, author, description, rating, user_id)
             VALUES (?, ?, ?, ?, ?)"""
    params = [title, author, description, rating, user_id]
    link_sql = "INSERT INTO review_classes (review_id, class_id) VALUES (?, ?)"
    return db.insert_with_links(sql, params, link_sql, class_ids)

def get_reviews(page=1):
    sql = """SELECT id, title FROM reviews
             ORDER BY id DESC
             LIMIT ? OFFSET ?"""
    return db.query(sql, [pagination.PAGE_SIZE, (page - 1) * pagination.PAGE_SIZE])


def count_reviews(query=""):
    if not query:
        return db.query("SELECT COUNT(*) FROM reviews")[0][0]
    sql = """SELECT COUNT(*) FROM reviews
             WHERE title LIKE ?
             OR author LIKE ?
             OR description LIKE ?
             OR rating LIKE ?"""
    search = "%" + query + "%"
    return db.query(sql, [search, search, search, query])[0][0]

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
    commands = [
        (sql, [title, author, description, rating, review_id]),
        ("DELETE FROM review_classes WHERE review_id = ?", [review_id]),
    ]
    sql = "INSERT INTO review_classes (review_id, class_id) VALUES (?, ?)"
    for class_id in class_ids:
        commands.append((sql, [review_id, class_id]))
    db.execute_transaction(commands)

def delete_review(review_id):
    sql = "DELETE FROM reviews WHERE id = ?"
    db.execute(sql, [review_id])

def search_reviews(query, page=1):
    sql = """SELECT id, title
             FROM reviews
             WHERE title LIKE ?
             OR author LIKE ?
             OR description LIKE ?
             OR rating LIKE ?
             ORDER BY id DESC
             LIMIT ? OFFSET ?"""
    search = "%" + query + "%"
    params = [search, search, search, query,
              pagination.PAGE_SIZE, (page - 1) * pagination.PAGE_SIZE]
    return db.query(sql, params)


def get_user_reviews(user_id, page=1):
    sql = """SELECT id, title
             FROM reviews
             WHERE user_id = ?
             ORDER BY id DESC
             LIMIT ? OFFSET ?"""
    params = [user_id, pagination.PAGE_SIZE, (page - 1) * pagination.PAGE_SIZE]
    return db.query(sql, params)
