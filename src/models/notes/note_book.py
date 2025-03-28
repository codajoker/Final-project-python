from collections import UserList
from src.models.notes.title import Title
from src.models.notes.text import Text
from src.utils.find_elements import find_element


class NoteBook(UserList):
    def _find_element(self, title):
        return find_element(self.data, lambda x: x.title.value == title)

    def add_note(self, note):
        element = self._find_element(note.title.value)
        if not element:
            self.data.append(note)
        else:
            raise KeyError("Note with such title already exists.")

    def delete_note(self, title):
        element = self._find_element(title)
        if element:
            self.data = list(filter(lambda x: x.title.value != title, self.data))
        else:
            raise KeyError("Note with such title doesn't exist.")
        
    def find_note(self, title):
        element = self._find_element(title)
        if element:
            return str(element)
        else:
            raise KeyError("Note with such title doesn't exist.")
        
    def edit_note(self, title, field, new_value):
        element = self._find_element(title)
        if element:
            if field == 'title':
                element.title = Title(new_value)
            else:
                element.text = Text(new_value)
        else:
            raise KeyError("Note with such title doesn't exist.")
        
    def __str__(self):
        return "\n".join(f"{idx + 1}. {str(note)}" for idx, note in enumerate(self.data))
