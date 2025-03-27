from src.models.contact.field import Field


class Comments(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Comments should have at least 2 characters")
        super().__init__(value)
