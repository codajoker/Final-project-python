from collections import UserDict
from datetime import date
import re
from src.utils.find_elements import find_element
from src.models.contact.name import Name
from src.models.contact.phone import Phone
from src.models.contact.email import Email
from src.models.contact.birthday import Birthday
from src.models.contact.adress import Adress
from src.models.contact.comments import Comments


class Contact:
    def __init__(
        self, name, phones=[], email="", birthday=None, adress="", comments=""
    ):
        self.name = Name(name)
        self.phones = phones
        self.birthday = birthday
        self.email = email
        self.adress = adress
        self.comments = comments

    def add_birthday(self, birthdate):
        self.birthday = Birthday(birthdate)

    def add_adress(self, adress):
        self.adress = Adress(adress)

    def add_comments(self, comments):
        self.comments = Comments(comments)

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
