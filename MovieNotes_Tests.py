import unittest
import MovieNotes.MovieNotes
import MovieNotes.Note

class MyTestCase(unittest.TestCase):
    def test_add_note_to_csv(self):
        res = MovieNotes.MovieNotes.add_note_to_csv()
        self.assertNotEqual(res, "")


if __name__ == '__main__':
    unittest.main()
