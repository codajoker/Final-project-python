import pickle
import os
from src.storage.storage_interface import StorageInterface


class Storage(StorageInterface):
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "rb") as file:
                try:
                    return pickle.load(file)
                except EOFError:
                    return []
        return []

    def save_data(self):
        with open(self.file_path, "wb") as file:
            pickle.dump(self.data, file)

    def add(self, item):
        self.data.append(item)
        self.save_data()

    def remove(self, item):
        self.data = [obj for obj in self.data if obj != item]
        self.save_data()

    def get_all(self):
        for item in self.data:
            yield item
