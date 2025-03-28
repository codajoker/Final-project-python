from src.models.notes.note_book import NoteBook
from src.models.notes.note import Note


def input_error(func):
    def inner(*args, **kwargs):
        try:
            if len(args[0]) < 3:
                raise ValueError
            return func(*args, **kwargs)
        except ValueError:
            return "Give me note title, field name and new value, please."
        except KeyError as e:
            return str(e)
        except TypeError as e:
            return str(e)

    return inner

@input_error
def edit_note(args, note_book: NoteBook):
    title, field, *rest = args
    new_value = rest[0] if field == 'title' else ' '.join(rest)
    note_book.edit_note(title, field, new_value)
    return "Note was changed."
