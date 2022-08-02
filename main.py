from MovieNotes import Note
from MovieNotes import MovieNotes


def main():
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

    notesnotes = MovieNotes.MovieNotes.from_notes("f.csv", mynotes.film_with_max_rating)
    notesnotes.print_to_console()

    newnotesnotes = MovieNotes.MovieNotes.from_notes("f1.csv", mynotes.film_with_min_rating)
    newnotesnotes.print_to_console()
    newnotesnotes.add_note_to_csv()

    print(mynotes.film_avg_rating)

    # mynotes.read_notes_from_csv()
    # mynotes.print_to_console()


if __name__ == '__main__':
    main()

