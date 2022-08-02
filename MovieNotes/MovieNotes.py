"""
Create micro library that allows users to work with notes about ukrainian films. Note should contain film_name, note, rating (rating - is 1 - 5 rating of the film) Micro lib should contain the next funcitonality:
Read notes from .csv file
Add note to .csv file
Remove note from .csv file
Print notes to console
Get films with the highest rating
Get films with the lowest rating
Get average rating among all films
"""

import csv
from statistics import mean

from MovieNotes import Note


class MovieNotes:
    def __init__(self, csv_file_name, note: Note.Note = None):
        self.__notes = []
        self.__add_note(note)
        self.__csv_file_name = csv_file_name

    @classmethod
    def from_notes(cls, csv_file_name, notes):
        cl = cls(csv_file_name=csv_file_name)
        cl.__notes = notes
        return cl

    def read_notes_from_csv(self):
        with open(self.__csv_file_name) as stream:
            reader = csv.reader(stream)
            for row in reader:
                if row:
                    note = Note.Note(*row)
                    self.__notes.append(note)

    def __dump_to_file(self):
        with open(self.__csv_file_name, "w", newline='') as stream:
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
        maxrate = max(rate.rating for rate in self.__notes)
        return [n for n in self.__notes if n.rating == maxrate]

    @property
    def film_with_min_rating(self):
        minrate = min(rate.rating for rate in self.__notes)
        return [n for n in self.__notes if n.rating == minrate]

    @property
    def film_avg_rating(self):
        return mean(rate.rating for rate in self.__notes)
