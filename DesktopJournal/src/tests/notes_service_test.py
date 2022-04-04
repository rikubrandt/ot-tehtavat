import unittest
from services.notes_service import NotesService
from init_database import init_db

class TestNotesService(unittest.TestCase):

    def setUp(self):
        init_db()
        self.notes_service = NotesService()


    def test_creating_new_note_id(self):
        new_note_id = self.notes_service.create_note("Test #test")
        self.assertEqual(new_note_id, 5)