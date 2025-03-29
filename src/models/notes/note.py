from src.models.notes.text import Text
from src.models.notes.title import Title


class Note:
    def __init__(self, title, text):
        self.title = Title(title)
        self.text = Text(text)

    def __eq__(self, other):
        if not isinstance(other, Note):
            return False
        return self.title.value == other.title.value

    def __repr__(self):
        return f"Note({self.title.value}, {self.text.value})"

    def __str__(self):
        return f"{self.title.value}: {self.text.value}"
