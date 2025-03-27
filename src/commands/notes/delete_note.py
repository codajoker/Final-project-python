from src.models.notes.note_book import NoteBook
from src.utils.find_elements import find_element


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note name, please."
        except KeyError as e:
            return str(e)
    return inner

@input_error
def delete_note(args, note_book: NoteBook):
    title, *_ = args
    note_book.delete_note(title)
    return "Note was deleted."
