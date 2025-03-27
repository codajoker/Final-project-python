from src.models.notes.field import Field


class Text(Field):
    def __init__(self, value):
        if len(value) < 2 or len(value) > 255:
            raise TypeError("Note text should have from 10 to 500 characters")
        super().__init__(value)
