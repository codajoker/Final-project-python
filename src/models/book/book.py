from src.models.notes.note_book import NoteBook


class Book:
    def __init__(self):
        self.notes = NoteBook()
        self.contacts = AddressBook()

    def __str__(self):
        return f"Notes: {self.notes}"
