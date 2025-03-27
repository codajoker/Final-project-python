from src.models.notes.note_book import NoteBook
from src.models.notes.note import Note


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note name and text, please."
        except KeyError as e:
            return str(e)
        except TypeError as e:
            return str(e)

    return inner

@input_error
def add_note(args, note_book: NoteBook):
    name, *rest = args
    note = Note(name, ' '.join(rest))
    note_book.add_note(note)
    return "Note was added."