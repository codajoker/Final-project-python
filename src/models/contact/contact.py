from collections import UserDict
from datetime import date
import re
from src.utils.find_elements import find_element
from src.models.contact.name import Name
from src.models.contact.phone import Phone
from src.models.contact.email import Email
from src.models.contact.birthday import Birthday
from src.models.contact.adress import Adress


class Contact:
    def __init__(
        self,
        name,
        phones=[],
        email="",
        birthday=None,
        address="",
    ):
        self.name = Name(name)
        self.phones = phones
        self.birthday = birthday
        self.email = email
        self.address = address

    def add_birthday(self, birthdate):
        self.birthday = Birthday(birthdate)

    def add_address(self, address):
        self.address = Adress(address)

    def get_name(self):
        return self.name.value

    def get_birthday(self):
        return self.birthday.value if self.birthday else None

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            if not self.find_phone(phone_obj.value):
                self.phones.append(phone_obj)
            else:
                raise ValueError("This phone number already exists for this contact")
        except ValueError as e:
            raise ValueError(str(e))

    def add_email(self, email):
        try:
            email_obj = Email(email)
            self.email = email_obj
        except ValueError as e:
            raise ValueError(str(e))

    def find_phone(self, phone):
        return find_element(self.phones, lambda x: x.value == phone)

    def find_email(self, email):
        return find_element(self.email, lambda x: x.value == email)

    def __repr__(self):
        return f"Record({self.name.value}, {self.phones}, {self.birthday} , {self.email}, {self.address})"

    def __str__(self):
        birthday_str = (
            self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "N/A"
        )
        email_str = str(self.email) if self.email else "N/A"
        address_str = str(self.address) if self.address else "N/A"
        phones_str = "; ".join(p.value for p in self.phones) if self.phones else "N/A"
        return f"Contact name: {self.name.value}, phones: {phones_str}, birthday: {birthday_str}, email: {email_str}, address: {address_str}"
