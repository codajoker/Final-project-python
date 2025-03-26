import datetime
from src.models.contact.field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = list(map(int, value.split(".")))
            date_obj = date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date_obj)
