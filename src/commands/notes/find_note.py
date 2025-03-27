from src.models.notes.note_book import NoteBook
from src.models.notes.note import Note


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note title, please."
        except KeyError as e:
            return str(e)

    return inner

@input_error
def find_note(args, note_book: NoteBook):
    title, *_ = args
    note = note_book.find_note(title)
    return f"{note}\n"
