import src.models.contact.field as Field


class Name(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Name should have at least 2 characters")
        super().__init__(value)
