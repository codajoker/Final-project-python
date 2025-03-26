from collections import UserList

from src.utils.find_elements import find_element

class NoteBook(UserList):
    def add_note(self, note):
        element = find_element(self.data, lambda x: x.name == note.name)
        if not element:
            self.data.append(note)
        else:
            raise KeyError("Note with such name already exists.")

    def delete_note(self, name):
        element = find_element(self.data, lambda x: x.name == name)
        if element:
            self.data.pop(element)
        else:
            raise KeyError("Note with such name was not found.")