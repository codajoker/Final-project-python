from src.models.notes.field import Field


class Title(Field):
    def __init__(self, value):
        if len(value) < 2 or len(value) > 63:
            raise TypeError("Note title should have from 2 to 63 characters.")
        super().__init__(value)
