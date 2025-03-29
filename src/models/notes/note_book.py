from collections import UserList
from src.models.notes.title import Title
from src.models.notes.text import Text
from src.utils.find_elements import find_element


class NoteBook(UserList):
    def __init__(self, storage=None):
        super().__init__()
        if storage is not None:
            self.load_from_storage(storage)

    def load_from_storage(self, storage):
        self.data.clear()
        for stored_note in storage.get_all():
            self.add_note(stored_note)

    def _find_element(self, title):
        return find_element(self.data, lambda x: x.title.value == title)

    def add_note(self, note):
        self.data.append(note)

    def delete_note(self, title):
        self.data = list(filter(lambda x: x.title.value != title, self.data))

    def find_note(self, title):
        return self._find_element(title)

    def __str__(self):
        return "\n".join(
            f"{idx + 1}. {str(note)}" for idx, note in enumerate(self.data)
        )
