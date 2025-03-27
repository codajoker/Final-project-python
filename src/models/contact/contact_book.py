from collections import UserDict


class ContactBook(UserDict):
    def __init__(self, storage=None):
        super().__init__()
        if storage is not None:
            self.load_from_storage(storage)

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data.keys() else None

    def delete(self, name):
        self.data.pop(name)

    def load_from_storage(self, storage):
        self.data.clear()
        for stored_contact in storage.get_all():
            self.add_record(stored_contact)
