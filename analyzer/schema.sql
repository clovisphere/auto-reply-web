DROP TABLE IF EXISTS automated_reponses;

CREATE TABLE automated_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tag VARCHAR(20) UNIQUE NOT NULL,
    response TEXT NOT NULL
);
