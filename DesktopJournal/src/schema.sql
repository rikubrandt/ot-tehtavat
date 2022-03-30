DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS note_tags;




CREATE TABLE notes(
    id SERIAL PRIMARY KEY,
    text TEXT,
    time TIMESTAMP,
    visible BOOLEAN DEFAULT TRUE
);

CREATE TABLE tags(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE note_tags(
    note_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (note_id, tag_id)
);