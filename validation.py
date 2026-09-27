"""Validate user input before storing it in the database."""

TITLE_MAX = 200
AUTHOR_MAX = 200
DESCRIPTION_MAX = 5000
USERNAME_MAX = 30
PASSWORD_MAX = 128
QUERY_MAX = 200
MAX_ID = 2**63 - 1


def review_form(form):
    review = {
        "title": form.get("book_name", ""),
        "author": form.get("author_name", ""),
        "description": form.get("description", ""),
        "rating": form.get("rating", ""),
    }
    errors = []
    for field, label, maximum in [
        ("title", "Kirjan nimi", TITLE_MAX),
        ("author", "Kirjailijan nimi", AUTHOR_MAX),
        ("description", "Arvostelu", DESCRIPTION_MAX),
    ]:
        value = review[field]
        if not value.strip():
            errors.append(f"{label} on pakollinen.")
        elif len(value) > maximum:
            errors.append(f"{label} saa sisältää enintään {maximum} merkkiä.")
    rating = review["rating"]
    if rating not in [str(number) for number in range(1, 11)]:
        errors.append("Arvosanan pitää olla kokonaisluku väliltä 1–10.")
    return review, errors


def registration(form):
    username = form.get("username", "").strip()
    password = form.get("password1", "")
    confirmation = form.get("password2", "")
    errors = []
    if not username or len(username) > USERNAME_MAX:
        errors.append(f"Käyttäjänimen pituuden pitää olla 1–{USERNAME_MAX} merkkiä.")
    if not password.strip() or len(password) > PASSWORD_MAX:
        errors.append(f"Salasanan pituuden pitää olla 1–{PASSWORD_MAX} merkkiä "
                      "eikä se saa sisältää vain välilyöntejä.")
    if password != confirmation:
        errors.append("Salasanat eivät ole samat.")
    return username, password, errors


def review_id(value):
    try:
        number = int(value)
    except (TypeError, ValueError):
        return None
    return number if 1 <= number <= MAX_ID else None
