from MovieNotes import Note
from MovieNotes import MovieNotes


def main():
    mynotes = Note.Note(1, 2, 4.5)
    mynotes = MovieNotes.MovieNotes("file.csv", mynotes)

    mynotes.add_note_to_csv(Note.Note(1, 3, 3.5))
    mynotes.add_note_to_csv(Note.Note(1, 4, 4.5))
    mynotes.add_note_to_csv(Note.Note(1, 2, 2.5))
    mynotes.add_note_to_csv(Note.Note(1, 5, 2.5))
    mynotes.add_note_to_csv(Note.Note(1, 6, 1.5))
    mynotes.add_note_to_csv(Note.Note(1, 7, 1.5))

    mynotes.remove_note_from_csv(Note.Note(1, 2, 4.5))
    mynotes.remove_note_from_csv(Note.Note(1, 4, 4.5))

    print(mynotes.film_with_max_rating)
    print(mynotes.film_with_min_rating)

    # mynotes.read_notes_from_csv()
    mynotes.print_to_console()



if __name__ == '__main__':
    main()

