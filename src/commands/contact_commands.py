from src.services.contact_service import ContactService


class ContactCommands:
    def __init__(self, contact_book, contact_storage):
        self.service = ContactService(contact_book, contact_storage)

    def add_contact(self, args):
        if len(args) < 1:
            return (
                "Usage: add-contact [name] "
                "[phone (optional)] "
                "[email (optional)] "
                "[birthday (optional)] "
                "[address (optional)]"
            )

        name = args[0]
        phone = args[1] if len(args) > 1 else None
        email = args[2] if len(args) > 2 else None
        birthday = args[3] if len(args) > 3 else None
        address = args[4] if len(args) > 4 else None

        return self.service.add_contact(name, phone, email, birthday, address)

    def find_contact(self, args):
        if len(args) < 1:
            return "Usage: find-contact [name]"

        name = args[0]
        contact = self.service.find_contact(name)

        return str(contact) if contact else f"Contact '{name}' not found."

    def edit_contact(self, args):
        if len(args) < 3:
            return "Usage: edit-contact [name] [field] [new_value]"

        name = args[0]
        field = args[1].lower()
        new_value = args[2]

        return self.service.edit_contact(name, field, new_value)

    def delete_contact(self, args):
        if len(args) < 1:
            return "Usage: delete-contact [name]"

        name = args[0]
        return self.service.delete_contact(name)

    def add_birthday(self, args):
        if len(args) < 2:
            return "Usage: add-birthday [name] [birthday (DD.MM.YYYY)]"

        name = args[0]
        birthday = args[1]

        return self.service.add_birthday(name, birthday)

    def show_birthday(self, args):
        if len(args) < 1:
            return "Usage: show-birthday [name]"

        name = args[0]
        return self.service.show_birthday(name)

    def upcoming_birthdays(self, args):
        days = 7
        if args and args[0].isdigit():
            days = int(args[0])

        upcoming = self.service.upcoming_birthdays(days)
        if upcoming:
            # If the service returns ["No upcoming birthdays."] or a list of actual birthdays
            if len(upcoming) == 1 and "No upcoming" in upcoming[0]:
                return upcoming[0]
            else:
                return "Upcoming birthdays:\n" + "\n".join(upcoming)
        else:
            return f"No upcoming birthdays in the next {days} days."

    def all_contacts(self, args):
        contacts = self.service.get_all_contacts()
        if not contacts:
            return "No contacts found."

        result = "All contacts:\n"
        for name, contact in contacts.items():
            result += f"{name}: {contact}\n"
        return result
