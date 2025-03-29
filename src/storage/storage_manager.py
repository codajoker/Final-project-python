from src.storage.storage import Storage


class StorageManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(StorageManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if self.__initialized:
            return
        self.contact_storage = Storage("contacts")
        self.note_storage = Storage("notes")
        self.__initialized = True

    def get_contact_storage(self):
        return self.contact_storage

    def get_note_storage(self):
        return self.note_storage

    def save_all(self):
        self.contact_storage.save_data()
        self.note_storage.save_data()
