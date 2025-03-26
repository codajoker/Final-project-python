from src.models.notes.note_book import NoteBook
from src.models.notes.note import Note


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note name and text, please."
        except KeyError:
            return "Such note already exists."

    return inner

@input_error
def add_note(args, note_book: NoteBook):
    name, text, *_ = args
    note = Note(name, text)
    note_book.add_note(note)
    message = "Note added."
    return message
    # note = note_book.find(name)
    # message = "Note updated."