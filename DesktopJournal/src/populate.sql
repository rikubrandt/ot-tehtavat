
INSERT INTO tags (name) VALUES ("idea");
INSERT INTO tags (name) VALUES ("question");
INSERT INTO tags (name) VALUES ("answer");

INSERT INTO notes(text, time) VALUES ("This is a note", DateTime("now"));
INSERT INTO notes(text, time) VALUES ("This is a note2", DateTime("now"));
INSERT INTO notes(text, time) VALUES ("This is a note3", DateTime("now"));
INSERT INTO notes(text, time) VALUES ("This is a note4", DateTime("now"));

INSERT INTO note_tags(note_id, tag_id) VALUES(4, 1);
INSERT INTO note_tags(note_id, tag_id) VALUES(3, 1);
INSERT INTO note_tags(note_id, tag_id) VALUES(2, 1);
INSERT INTO note_tags(note_id, tag_id) VALUES(1, 1);
INSERT INTO note_tags(note_id, tag_id) VALUES(3, 2);
