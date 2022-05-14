import unittest
from services.notes_service import NotesService
from init_database import init_test_db


class TestNotes(unittest.TestCase):

    def setUp(self):
        init_test_db()
        self.notes_service = NotesService()

    def test_get_notes(self):
        notes = self.notes_service.get_notes()
        self.assertEqual(len(notes), 4)
        num = 1
        for note in notes:
            self.assertEqual(note["text"], "This is a note"+str(num))
            num += 1

    def test_get_tags(self):
        tags = self.notes_service.get_tags()
        self.assertEqual(tags[0]["name"], "idea")
        self.assertEqual(tags[1]["name"], "question")
        self.assertEqual(tags[2]["name"], "answer")

    def test_search_by_tag(self):
        notes = self.notes_service.search_by_tag("#question")
        self.assertEqual(notes[0]["text"], "This is a note3")

    def test_get_notes_by_keyword(self):
        notes = self.notes_service.search_by_keyword("1")
        self.assertEqual(notes[0]["text"], "This is a note1")

    def test_delete_note(self):
        self.notes_service.delete_note(1)
        notes = self.notes_service.get_notes()
        self.assertEqual(len(notes), 3)
        num = 2
        for note in notes:
            self.assertEqual(note["text"], "This is a note"+str(num))
            num += 1

    def test_creating_new_note_id(self):
        new_note_id = self.notes_service.create_note("Test #test")
        self.assertEqual(new_note_id, 5)
