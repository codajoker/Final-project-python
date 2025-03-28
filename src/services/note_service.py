from src.models.notes.title import Title
from src.models.notes.text import Text
from src.models.notes.note import Note


class NoteService:
    def __init__(self, note_book, storage):
        self.note_book = note_book
        self.storage = storage

    def add_note(self, title, text):
        if self.note_book.find_note(title):
            return f"Note '{title}' already exists. Use 'edit-note' to modify it."
        
        note = Note(title, text)

        self.note_book.add_note(note)
        self.storage.add(note)
        return f"Note '{title}' was added successfully."
    
    def find_note(self, title):
        return self.note_book.find_note(title)
    
    def edit_note(self, title, field, new_value):
        note = self.note_book.find_note(title)
        if not note:
            return f"Note '{title}' was not found."

        old_note = note

        try:
            if field == "title":
                current_title = note.title.value
                note.title = Title(new_value)
                self.note_book.delete_note(current_title)
                self.note_book.add_note(note)

            elif field == "text":
                note.text.value = Text(new_value)
                self.note_book.delete_note(title)
                self.note_book.add_note(note)

            else:
                return f"Unknown field '{field}'. Available fields: title, text."

            self.storage.update(old_note, note)
            return f"{field.capitalize()} was updated for contact '{title}'."

        except ValueError as e:
            return f"Error updating {field}: {e}"
    
    def delete_note(self, title):
        note = self.note_book.find_note(title)
        if note:
            self.note_book.delete_note(title)
            self.storage.remove(title)
            return f"Contact '{title}' was deleted successfully."
        else:
            return f"Contact '{title}' was not found."
        
    def get_all_notes(self):
        return self.note_book.data
