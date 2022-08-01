import csv

from MovieNotes import Note

class MovieNotes:
    def __init__(self, csv_file_name, note: Note.Note = None):
        self.__notes = []
        self.__add_note(note)
        self.__csv_file_name = csv_file_name

    # @classmethod
    # def from_notes(cls, csv_file_name, notes):
    #     cl = cls(csv_file_name=csv_file_name)
    #     cl.__notes = notes
    #     return cl

    def read_notes_from_csv(self):
        with open(self.__csv_file_name) as stream:
            reader = csv.reader(stream)
            for row in reader:
                if row:
                    note = Note.Note(*row)
                    self.__notes.append(note)

    def __dump_to_file(self):
        with open(self.__csv_file_name, "w") as stream:
            writer = csv.writer(stream)
            writer.writerows(self.__notes)

    def __add_note(self, note):
        if note is not None:
            self.__notes.append(note)

    def __remove_note(self, note):
        if note is not None:
            self.__notes.remove(note)

    def add_note_to_csv(self, note: Note.Note = None):
        self.__add_note(note)
        self.__dump_to_file()

    def remove_note_from_csv(self, note: Note.Note = None):
        self.__remove_note(note)
        self.__dump_to_file()

    def print_to_console(self):
        for n in self.__notes:
            print(n)

    @property
    def film_with_max_rating(self):
        return max(rate.rating for rate in self.__notes)

    @property
    def film_with_min_rating(self):
        return min(rate.rating for rate in self.__notes)

    # @property
    # def film_with_avg_rating(self):
    #     return return mean(rate.rating for rate in self.__notes__)
