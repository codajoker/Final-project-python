from collections import UserDict
from datetime import date
import re
from src.utils.find_elements import find_element

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
class Name(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Name should have at least 2 characters")
        super().__init__(value)
class Adress(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Adress should have at least 2 characters")
        super().__init__(value)
class Comments(Field):
    def __init__(self, value):
        if len(value) < 2:
            raise TypeError("Comments should have at least 2 characters")
        super().__init__(value)
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() and not len(value) == 10:
            raise TypeError("Pnone number should have only 10 digits")
        super().__init__(value)
    def __repr__(self):
        return f"Phone({self.value})"
class Email(Field):
    def __init__(self, value):
        if not self._is_valid_email(value):
            raise ValueError("Invalid email format. Use example@domain.com")
        super().__init__(value)
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Перевірка email за допомогою регулярного виразу"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def __repr__(self):
        return f"Email({self.value})"
class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = list(map(int, value.split('.')))
            date_obj = date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(date_obj)

class Record:
    def __init__(self, name, phones=[], email="" , birthday = None,adress="",comments=""):
        self.name = Name(name)
        self.phones = phones
        self.birthday = birthday
        self.email = email
        self.adress = adress
        self.comments = comments

    def add_birthday(self, birthdate):
        self.birthday = Birthday(birthdate)

    def get_name(self):
        return self.name.value

    def get_birthday(self):
        return self.birthday.value if self.birthday else None

    def add_phone(self, phone):
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))
        else:
            raise KeyError("Phone already exists.")
    def add_email(self, email):
        if not self.find_email(email):
            self.phones.append(Email(email))
        else:
            raise KeyError("Phone already exists.")


    def find_phone(self, phone):
        return find_element(self.phones, lambda x: x.value == phone)
    def find_email(self, email):
        return find_element(self.email, lambda x: x.value == email)
    
    def __repr__(self):
        return f"Record({self.name.value}, {self.phones}, {self.birthday} , {self.email}, {self.adress}, {self.comments})"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones) , self.birthday, self.email, self.adress, self.comments}"