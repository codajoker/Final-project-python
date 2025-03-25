from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def add(self, item):
        pass

    @abstractmethod
    def update(self, old_item, new_item):
        pass

    @abstractmethod
    def remove(self, item):
        pass

    @abstractmethod
    def get_all(self):
        pass
