from src.models.contact.contact import Contact
from datetime import datetime


class ContactService:
    def __init__(self, address_book, storage):
        self.address_book = address_book
        self.storage = storage

    def add_contact(self, name, phone=None, email=None, birthday=None, address=None):
        if self.address_book.find(name):
            return f"Contact '{name}' already exists. Use edit_contact to modify it."

        contact = Contact(name)

        if phone:
            try:
                contact.add_phone(phone)
            except ValueError as e:
                return f"Invalid phone number: {e}"

        if email:
            try:
                contact.add_email(email)
            except ValueError as e:
                return f"Invalid email: {e}"

        if birthday:
            try:
                contact.add_birthday(birthday)
            except ValueError as e:
                return f"Invalid birthday format (use DD.MM.YYYY): {e}"

        if address:
            contact.add_address(address)

        self.address_book.add_record(contact)
        self.storage.add(contact)  # Persist
        return f"Contact '{name}' added successfully."

    def find_contact(self, name):
        return self.address_book.find(name)

    def edit_contact(self, name, field, new_value):
        contact = self.address_book.find(name)
        if not contact:
            return f"Contact '{name}' not found."

        old_contact = contact

        try:
            if field == "name":
                old_name = contact.get_name()
                contact.name.value = new_value
                self.address_book.delete(old_name)
                self.address_book.add_record(contact)

            elif field == "phone":
                if contact.phones:
                    contact.phones.pop(0)
                contact.add_phone(new_value)

            elif field == "email":
                contact.add_email(new_value)

            elif field == "birthday":
                contact.add_birthday(new_value)

            elif field == "address":
                contact.add_address(new_value)

            else:
                return (
                    "Unknown field '{field}'. "
                    "Available fields: name, phone, email, birthday, address."
                )

            self.storage.update(old_contact, contact)
            return f"{field.capitalize()} updated for contact '{name}'."

        except ValueError as e:
            return f"Error updating {field}: {e}"

    def delete_contact(self, name):
        contact = self.address_book.find(name)
        if contact:
            self.address_book.delete(name)
            self.storage.remove(contact)  # Also remove from storage
            return f"Contact '{name}' deleted successfully."
        else:
            return f"Contact '{name}' not found."

    def add_birthday(self, name, birthday):
        contact = self.address_book.find(name)
        if not contact:
            return f"Contact '{name}' not found."

        try:
            old_contact = contact
            contact.add_birthday(birthday)
            self.storage.update(old_contact, contact)
            return f"Birthday added/updated for contact '{name}'."
        except ValueError as e:
            return f"Invalid birthday format: {e}"

    def show_birthday(self, name):
        contact = self.address_book.find(name)
        if not contact:
            return f"Contact '{name}' not found."

        birthday = contact.get_birthday()
        if birthday:
            return f"{name}'s birthday: {birthday}"
        else:
            return f"No birthday set for contact '{name}'."

    def upcoming_birthdays(self, days=7):
        today = datetime.today()
        upcoming = []

        for name, contact in self.address_book.data.items():
            birthday_str = contact.get_birthday()
            if birthday_str:
                if not isinstance(birthday_str, str):
                    birthday_date = birthday_str
                else:
                    try:
                        birthday_date = datetime.strptime(
                            birthday_str, "%d.%m.%Y"
                        ).date()
                    except ValueError:
                        continue

                birthday_this_year = birthday_date.replace(year=today.year)
                delta = (birthday_this_year - today.date()).days
                if 0 <= delta <= days:
                    upcoming.append(f"{name}: {birthday_date.strftime('%d.%m.%Y')}")

        if not upcoming:
            return ["No upcoming birthdays."]
        return upcoming

    def get_all_contacts(self):
        return self.address_book.data
