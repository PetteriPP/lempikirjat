CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    description TEXT,
    rating INTEGER,
    user_id INTEGER REFERENCES users
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY,
    kind TEXT NOT NULL CHECK (kind IN ('genre', 'theme')),
    name TEXT NOT NULL,
    UNIQUE (kind, name)
);

CREATE TABLE IF NOT EXISTS review_classes (
    review_id INTEGER NOT NULL REFERENCES reviews (id) ON DELETE CASCADE,
    class_id INTEGER NOT NULL REFERENCES classes (id),
    PRIMARY KEY (review_id, class_id)
);
