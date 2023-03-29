-- SQLite
CREATE TABLE users (
    user_id INTEGER NOT NULL PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE;
    hash TEXT NOT NULL,
    birthdate TEXT NOT NULL,
    sign TEXT NOT NULL
);