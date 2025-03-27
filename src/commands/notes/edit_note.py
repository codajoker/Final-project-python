from src.models.notes.note_book import NoteBook
from src.models.notes.note import Note


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note title and new text, please."
        except KeyError as e:
            return str(e)
        except TypeError as e:
            return str(e)

    return inner

@input_error
def edit_note(args, note_book: NoteBook):
    title, new_text, *_ = args
    note_book.edit_note(title, new_text)
    return "Note was changed."
