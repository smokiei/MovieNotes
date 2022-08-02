import unittest
import MovieNotes.MovieNotes as MovieNotes
import MovieNotes.Note as Note

class MyTestCase(unittest.TestCase):
    def test_add_note_to_csv(self):
        mynote = Note.Note("прятки", "best of the best movie", 5)
        mynotes = MovieNotes.MovieNotes("file.csv", mynote)

        mynotes.add_note_to_csv(Note.Note("Кино1", "норм", 3.5))
        mynotes.add_note_to_csv(Note.Note("Кіборги", "нормa", 4.5))
        mynotes.add_note_to_csv(Note.Note("Микита Кожум'яка", "нормa1", 2.5))
        mynotes.add_note_to_csv(Note.Note("Синевир ", "норм2", 2.5))
        mynotes.add_note_to_csv(Note.Note("Одного разу в Україні ", "норм3", 1.5))
        mynotes.add_note_to_csv(Note.Note("Гайдамака ", "норм4", 1.5))

        mynotes.remove_note_from_csv(Note.Note("прятки", "best of the best movie", 5))
        mynotes.remove_note_from_csv(Note.Note("Кіборги", "нормa", 4.5))
        res = mynotes.film_avg_rating
        self.assertEqual(res, 2.3)

    def test_add_note_to_csv_with_error(self):
        with self.assertRaises(ValueError):
            Note.Note("прятки", "best of the best movie", 5.5)


if __name__ == '__main__':
    unittest.main()
