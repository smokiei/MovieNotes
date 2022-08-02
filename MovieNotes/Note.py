"""
Class for note repr
"""
# limits for rate of a film
ratemax = 5
ratemin = 1

exception_text = f"rating must be float in range {ratemin} - {ratemax}"


class Note:

    def __init__(self, film_name, note, rating):

        self._film_name = film_name
        self._note = note
        self.rating = rating

    @property
    def film_name(self):
        return self._film_name

    @property
    def note(self):
        return self._note

    @property
    def rating(self):
        return self._rating

    @film_name.setter
    def film_name(self, val):
        self._film_name = val

    @note.setter
    def note(self, val):
        self._note = val

    @rating.setter
    def rating(self, val):
        try:
            self._rating = float(val)
        except:
            raise ValueError(exception_text)

        if self._rating > ratemax or self._rating < ratemin:
            raise ValueError(exception_text)

    def __eq__(self, other):
        if self.film_name == other.film_name and \
           self.note == other.note and \
           self.rating == other.rating:
             return True
        else:
             return False

    def __str__(self):
        return f"{self.film_name}, {self.note}, {self.rating}"

    def __iter__(self):
        return iter([self.film_name, self.note, self.rating])
