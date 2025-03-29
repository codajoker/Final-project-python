from src.models.notes.field import Field


class Tag(Field):
    def __init__(self, value):
        if len(value) < 3 or len(value) > 31:
            raise TypeError("Tag should have from 3 to 31 characters.")
        super().__init__(value)
