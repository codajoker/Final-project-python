from src.services.contact_service import ContactService


def add_contact(args, contact_book):
    if len(args) < 1:
        return "Usage: add-contact [name] [phone (optional)] [email (optional)] [birthday (optional)] [address (optional)] [comments (optional)]"
    
    name = args[0]
    phone = args[1] if len(args) > 1 else None
    email = args[2] if len(args) > 2 else None
    birthday = args[3] if len(args) > 3 else None
    address = args[4] if len(args) > 4 else None
    comments = args[5] if len(args) > 5 else None
    
    contact_service = ContactService(contact_book)
    return contact_service.add_contact(name, phone, email, birthday, address, comments)


def find_contact(args, contact_book):
    if len(args) < 1:
        return "Usage: find-contact [name]"
    
    name = args[0]
    contact_service = ContactService(contact_book)
    contact = contact_service.find_contact(name)
    
    if contact:
        return str(contact)
    else:
        return f"Contact '{name}' not found."


def edit_contact(args, contact_book):
    if len(args) < 3:
        return "Usage: edit-contact [name] [field] [new_value]"
    
    name = args[0]
    field = args[1].lower()
    new_value = args[2]
    
    contact_service = ContactService(contact_book)
    return contact_service.edit_contact(name, field, new_value)


def delete_contact(args, contact_book):
    if len(args) < 1:
        return "Usage: delete-contact [name]"
    
    name = args[0]
    contact_service = ContactService(contact_book)
    return contact_service.delete_contact(name)


def add_birthday(args, contact_book):
    if len(args) < 2:
        return "Usage: add-birthday [name] [birthday (DD.MM.YYYY)]"
    
    name = args[0]
    birthday = args[1]
    
    contact_service = ContactService(contact_book)
    return contact_service.add_birthday(name, birthday)


def show_birthday(args, contact_book):
    if len(args) < 1:
        return "Usage: show-birthday [name]"
    
    name = args[0]
    contact_service = ContactService(contact_book)
    return contact_service.show_birthday(name)


def upcoming_birthdays(args, contact_book):
    days = 7 
    
    if args and args[0].isdigit():
        days = int(args[0])
    
    contact_service = ContactService(contact_book)
    upcoming = contact_service.upcoming_birthdays(days)
    
    if upcoming:
        return "Upcoming birthdays:\n" + "\n".join(upcoming)
    else:
        return f"No upcoming birthdays in the next {days} days."


def all_contacts(args, contact_book):
    contact_service = ContactService(contact_book)
    contacts = contact_service.get_all_contacts()
    
    if not contacts:
        return "No contacts found."
    
    result = "All contacts:\n"
    for name, contact in contacts.items():
        result += f"{name}: {contact}\n"
    
    return result
