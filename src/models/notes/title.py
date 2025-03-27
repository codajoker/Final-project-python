from src.models.notes.field import Field


class Title(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Note title should have at least 2 characters")
        super().__init__(value)