from collections import UserList
from src.utils.find_elements import find_element


class NoteBook(UserList):
    def add_note(self, note):
        element = find_element(self.data, lambda x: x.title.value == note.title.value)
        if not element:
            self.data.append(note)
        else:
            raise KeyError("Note with such title already exists.")

    def delete_note(self, title):
        element = find_element(self.data, lambda x: x.title.value == title)
        if element:
            self.data = list(filter(lambda x: x.title.value != title, self.data))
        else:
            raise KeyError("Note with such title doesn't exist.")