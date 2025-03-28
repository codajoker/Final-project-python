import pickle
import os
from src.storage.storage_interface import StorageInterface
from src.config.constants import CONTACTS_FILE, NOTES_FILE
from builtins import open


class Storage(StorageInterface):
    FILE_PATHS = {
        "contacts": CONTACTS_FILE,
        "notes": NOTES_FILE,
    }

    def __init__(self, file_type):
        self.file_path = self._get_file_path(file_type)
        self.data = None

    # def __del__(self):
    #     self.save_data()

    def _get_file_path(self, file_type):
        if file_type not in self.FILE_PATHS:
            raise ValueError("Invalid file type. Use 'contacts' or 'notes'.")
        return self.FILE_PATHS[file_type]

    def load_data(self):
        if self.data is None:
            try:
                if os.path.exists(self.file_path):
                    with open(self.file_path, "rb") as file:
                        self.data = pickle.load(file)
                else:
                    self.data = []
            except (pickle.UnpicklingError, EOFError):
                print(f"Warning: {self.file_path} is corrupted. Loading empty dataset.")
                self.data = []
            except Exception as e:
                print(f"Error loading {self.file_path}: {e}")
                self.data = []
        return self.data

    def save_data(self):
        if self.data is not None:
            try:
                with open(self.file_path, "wb") as file:
                    pickle.dump(self.data, file)
            except Exception as e:
                print(f"Error saving data to {self.file_path}: {e}")

    def add(self, item):
        self.load_data().append(item)
        self.save_data()

    def update(self, old_item, new_item):
        self.data = [new_item if obj == old_item else obj for obj in self.load_data()]
        self.save_data()

    def remove(self, item):
        self.data = [obj for obj in self.load_data() if obj != item]
        self.save_data()

    def get_all(self):
        yield from self.load_data()
