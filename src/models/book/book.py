from src.models.notes.note_book import NoteBook
from src.models.contact.contact_book import ContactBook


class Book:
    def __init__(self):
        self.notes = NoteBook()
        self.contacts = ContactBook()

    def __str__(self):
        return f"Notes: {self.notes}"
