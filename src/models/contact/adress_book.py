from collections import UserDict
from datetime import date, datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data[name] if name in self.data.keys() else None

    def delete(self, name):
        self.data.pop(name)
