from src.storage.storage import Storage


class StorageManager:
    def __init__(self):
        self.contact_storage = Storage("contacts")
        self.note_storage = Storage("notes")

    def get_contact_storage(self):
        return self.contact_storage

    def get_note_storage(self):
        return self.note_storage
