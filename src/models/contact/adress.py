import src.models.contact.field as Field


class Adress(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Adress should have at least 2 characters")
        super().__init__(value)
