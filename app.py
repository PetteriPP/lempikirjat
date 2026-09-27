import sqlite3
from flask import Flask
from flask import abort, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import db
import reviews
import validation

app = Flask(__name__)
app.secret_key = config.secret_key
app.jinja_env.globals["limits"] = {
    "title": validation.TITLE_MAX,
    "author": validation.AUTHOR_MAX,
    "description": validation.DESCRIPTION_MAX,
    "username": validation.USERNAME_MAX,
    "password": validation.PASSWORD_MAX,
    "query": validation.QUERY_MAX,
}


def require_login():
    if "user_id" not in session:
        abort(403, description="Kirjaudu sisään käyttääksesi tätä toimintoa.")


def get_review(review_id):
    review_id = validation.review_id(review_id)
    if review_id is None:
        abort(404, description="Arvostelua ei löytynyt.")
    review = reviews.show_review(review_id)
    if review is None:
        abort(404, description="Arvostelua ei löytynyt.")
    return review


def require_owner(review):
    if review["user_id"] != session["user_id"]:
        abort(403, description="Voit muokata ja poistaa vain omia arvostelujasi.")


@app.errorhandler(403)
@app.errorhandler(404)
def show_error(error):
    return render_template("error.html", error=error), error.code


@app.route("/")
def index():
    query = request.args.get("query", "").strip()
    if len(query) > validation.QUERY_MAX:
        flash(f"Hakusana saa sisältää enintään {validation.QUERY_MAX} merkkiä.")
        return render_template("index.html", reviews=[], query=query), 400
    if query:
        review_list = reviews.search_reviews(query)
    else:
        review_list = reviews.get_reviews()
    return render_template("index.html", reviews=review_list, query=query)


@app.route("/review/<int:review_id>")
def show_review(review_id):
    review = get_review(review_id)
    return render_template("show_review.html", review=review)


@app.route("/new_book_review")
def new_book_review():
    require_login()
    return render_template("new_book_review.html", review={})


@app.route("/create_book_review", methods=["POST"])
def create_book_review():
    require_login()
    review, errors = validation.review_form(request.form)
    if errors:
        for error in errors:
            flash(error)
        return render_template("new_book_review.html", review=review), 400
    reviews.add_review(review["title"].strip(), review["author"].strip(),
                       review["description"].strip(), int(review["rating"]),
                       session["user_id"])
    return redirect("/")


@app.route("/edit_review/<int:review_id>")
def edit_review(review_id):
    require_login()
    review = get_review(review_id)
    require_owner(review)
    return render_template("edit_review.html", review=review)


@app.route("/update_review", methods=["POST"])
def update_review():
    require_login()
    original = get_review(request.form.get("review_id"))
    require_owner(original)
    review, errors = validation.review_form(request.form)
    if errors:
        for error in errors:
            flash(error)
        review["id"] = original["id"]
        return render_template("edit_review.html", review=review), 400
    reviews.update_review(original["id"], review["title"].strip(),
                          review["author"].strip(), review["description"].strip(),
                          int(review["rating"]))
    return redirect("/review/" + str(original["id"]))


@app.route("/delete_review/<int:review_id>", methods=["GET", "POST"])
def delete_review(review_id):
    require_login()
    review = get_review(review_id)
    require_owner(review)
    if request.method == "GET":
        return render_template("delete_review.html", review=review)
    if "cancel" in request.form:
        return redirect("/review/" + str(review_id))
    if "delete" not in request.form:
        flash("Vahvista arvostelun poistaminen tai peruuta.")
        return render_template("delete_review.html", review=review), 400
    reviews.delete_review(review_id)
    flash("Kirja-arvostelu poistettu.")
    return redirect("/")


@app.route("/register")
def register():
    return render_template("register.html", username="")


@app.route("/create", methods=["POST"])
def create():
    username, password, errors = validation.registration(request.form)
    if errors:
        for error in errors:
            flash(error)
        return render_template("register.html", username=username), 400
    password_hash = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        flash("Käyttäjänimi on jo varattu. Valitse toinen käyttäjänimi.")
        return render_template("register.html", username=username), 400
    flash("Tunnus luotu. Voit nyt kirjautua sisään.")
    return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    valid_input = (0 < len(username) <= validation.USERNAME_MAX
                   and 0 < len(password) <= validation.PASSWORD_MAX
                   and bool(password.strip()))
    result = []
    if valid_input:
        sql = "SELECT id, password_hash FROM users WHERE username = ?"
        result = db.query(sql, [username])
    if not result or not check_password_hash(result[0]["password_hash"], password):
        flash("Väärä käyttäjänimi tai salasana.")
        return render_template("index.html", reviews=reviews.get_reviews(),
                               query="", username=username), 400
    session["user_id"] = result[0]["id"]
    session["username"] = username
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
