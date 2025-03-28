from src.services.note_service import NoteService


class NoteCommands:
    def __init__(self, note_book, note_storage):
        self.service = NoteService(note_book, note_storage)

    def add_note(self, args):
        if len(args) < 2:
            return (
                "Usage: add-note [title] [text]"
            )

        title, *rest = args
        return self.service.add_note(title, ' '.join(rest))
    
    def find_note(self, args):
        if len(args) < 1:
            return "Usage: find-note [title]"

        if len(args[0]) < 2 or len(args[0]) > 63:
            return "Note title should have from 2 to 63 characters."

        title = args[0]
        note = self.service.find_note(title)

        return str(note) if note else f"Note '{title}' was not found."
    
    def edit_note(self, args):
        if len(args) < 3:
            return "Usage: edit-note [title] [field] [new_value]"

        title, field, *rest = args
        new_value = rest[0] if field.lower() == 'title' else ' '.join(rest)
        return self.service.edit_note(title, field, new_value)

    def delete_note(self, args):
        if len(args) < 1:
            return "Usage: delete-note [title]"
        
        if len(args[0]) < 2 or len(args[0]) > 63:
            return "Note title should have from 2 to 63 characters."

        title = args[0]
        return self.service.delete_note(title)
    
    def all_notes(self):
        notes = self.service.get_all_notes()
        if not len(notes):
            return "No notes found."

        result = "All notes:\n"
        for note in notes:
            result += f"{note}\n"
        return result
