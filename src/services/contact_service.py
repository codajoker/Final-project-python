from datetime import date, datetime
from src.models.contact.contact import Contact
from src.models.contact.contact_book import СontactBook


class ContactService:
    def __init__(self, address_book):
        self.address_book = address_book
    
    def add_contact(self, name, phone=None, email=None, birthday=None, address=None, comments=None):
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
                contact.email = email
            except ValueError as e:
                return f"Invalid email: {e}"
        
        if birthday:
            try:
                contact.add_birthday(birthday)
            except ValueError as e:
                return f"Invalid birthday format (use DD.MM.YYYY): {e}"
        
        if address:
            contact.add_adress(address)
        
        if comments:
            contact.add_comments(comments)
        
        self.address_book.add_record(contact)
        
        return f"Contact '{name}' added successfully."
    
    def find_contact(self, name):
        contact = self.address_book.find(name)
        
        if contact:
            return contact
        else:
            return None
    
    def edit_contact(self, name, field, new_value):
        contact = self.address_book.find(name)
        if not contact:
            return f"Contact '{name}' not found."
        
        try:
            if field == "name":
                old_name = contact.get_name()
                contact.name.value = new_value
                self.address_book.delete(old_name)
                self.address_book.add_record(contact)
                return f"Contact name updated from '{old_name}' to '{new_value}'."
            
            elif field == "phone":
                if contact.phones:
                    contact.phones.pop(0)
                contact.add_phone(new_value)
                return f"Phone number updated for contact '{name}'."
            
            elif field == "email":
                contact.add_email(new_value)
                return f"Email updated for contact '{name}'."
            
            elif field == "birthday":
                contact.add_birthday(new_value)
                return f"Birthday updated for contact '{name}'."
            
            elif field == "address":
                contact.add_adress(new_value)
                return f"Address updated for contact '{name}'."
            
            elif field == "comments":
                contact.add_comments(new_value)
                return f"Comments updated for contact '{name}'."
            
            else:
                return f"Unknown field '{field}'. Available fields: name, phone, email, birthday, address, comments."
        
        except ValueError as e:
            return f"Error updating {field}: {e}"
    
    def delete_contact(self, name):
        if self.address_book.find(name):
            self.address_book.delete(name)
            return f"Contact '{name}' deleted successfully."
        else:
            return f"Contact '{name}' not found."
    
    def add_birthday(self, name, birthday):
        contact = self.address_book.find(name)
        if not contact:
            return f"Contact '{name}' not found."
        
        try:
            contact.add_birthday(birthday)
            return f"Birthday added to contact '{name}'."
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
        upcoming = []
        
        for name, contact in self.address_book.data.items():
            if contact.birthday:
                upcoming.append(f"{name}: {contact.get_birthday()}")
        
        return upcoming
    
    def get_all_contacts(self):
        return self.address_book.data
