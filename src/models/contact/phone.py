import src.models.contact.field as Field


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() and not len(value) == 10:
            raise TypeError("Pnone number should have only 10 digits")
        super().__init__(value)

    def __repr__(self):
        return f"Phone({self.value})"
