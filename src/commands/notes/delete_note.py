from src.models.notes.note_book import NoteBook
from src.utils.find_elements import find_element


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note name, please."
        except KeyError:
            return "Such note doesn't exist."

    return inner

@input_error
def delete_note(args, note_book: NoteBook):
    name, *_ = args
    note = find_element(note_book, lambda x: x.name == name)
    note_book.delete_note(note)
    message = "Note deleted."
    return message
    # message = "Such note doesn't exist."