from src.commands.note_commands import NoteCommands
from src.models.notes.note_book import NoteBook
from src.storage.storage_manager import StorageManager
from src.utils.command_suggester import CommandSuggester
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from src.commands.contact_commands import ContactCommands
from src.models.contact.contact_book import ContactBook


class AssistantBot:
    def __init__(self):
        self.storage_manager = StorageManager()

        # Notes
        self.notes_storage = self.storage_manager.get_note_storage()
        self.notes_book = NoteBook(storage=self.notes_storage)

        self.notes_commands = NoteCommands(
            self.notes_book, self.notes_storage
        )

        # Contacts
        self.contact_storage = self.storage_manager.get_contact_storage()
        self.contacts_book = ContactBook(storage=self.contact_storage)

        self.contacts_commands = ContactCommands(
            self.contacts_book, self.contact_storage
        )

        self.command_suggester = CommandSuggester()

        self.style = Style.from_dict(
            {
                "prompt": "ansicyan bold",
            }
        )

        self.session = PromptSession(
            completer=self.command_suggester.completer,
            style=self.style,
            complete_while_typing=True,
        )

    def _parse_input(self, user_input):
        if not user_input.strip():
            return "", []

        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    def _show_welcome_message(self):
        print("Welcome to the assistant bot!")
        print("Type 'hello' for help or start typing a command to see suggestions.")

    def _suggest_command(self, user_input):
        suggested_command = self.command_suggester.suggest_command(user_input)

        if suggested_command:
            description = self.command_suggester.get_command_description(
                suggested_command
            )
            print(f"Did you mean '{suggested_command}' ({description})?")
            user_response = input("Use this command? (yes/no): ").strip().lower()

            if user_response in ["yes", "y"]:
                return suggested_command

        return None

    def run(self):
        self._show_welcome_message()

        while True:
            try:
                user_input = self.session.prompt("Command > ")

                command, args = self._parse_input(user_input)

                if not command:
                    print("Please enter a command.")
                    continue

                if command in ["close", "exit"]:
                    print("Good bye!")
                    break
                elif command == "hello":
                    print("How can I help you?")
                    print("Available commands:")
                    for cmd in self.command_suggester.available_commands:
                        desc = self.command_suggester.get_command_description(cmd)
                        print(f"  - {cmd}: {desc}")
                elif command == "add-contact":
                    print(self.contacts_commands.add_contact(args))
                elif command == "find-contact":
                    print(self.contacts_commands.find_contact(args))
                elif command == "edit-contact":
                    print(self.contacts_commands.edit_contact(args))
                elif command == "delete-contact":
                    print(self.contacts_commands.delete_contact(args))
                elif command == "add-birthday":
                    print(self.contacts_commands.add_birthday(args))
                elif command == "show-birthday":
                    print(self.contacts_commands.show_birthday(args))
                elif command == "upcoming-birthdays":
                    print(self.contacts_commands.upcoming_birthdays(args))
                elif command == "all-contacts":
                    print(self.contacts_commands.all_contacts(args))
                elif command == "add-note":
                    print(self.notes_commands.add_note(args))
                elif command == "delete-note":
                    print(self.notes_commands.delete_note(args))
                elif command == "find-note":
                    print(self.notes_commands.find_note(args))
                elif command == "edit-note":
                    print(self.notes_commands.edit_note(args))
                elif command == "add-tag":
                    print("Adding tag...")
                elif command == "remove-tag":
                    print("Removing tag...")
                elif command == "all-notes":
                    print(self.notes_commands.all_notes())
                else:
                    suggested_command = self._suggest_command(user_input)

                    if suggested_command:
                        print(f"Running '{suggested_command}'...")

                        if suggested_command in ["close", "exit"]:
                            print("Good bye!")
                            break
                        elif suggested_command == "hello":
                            print("How can I help you?")
                            print("Available commands:")
                            for cmd in self.command_suggester.available_commands:
                                desc = self.command_suggester.get_command_description(
                                    cmd
                                )
                                print(f"  - {cmd}: {desc}")
                        elif command == "add-contact":
                            print(self.contacts_commands.add_contact(args))
                        elif command == "find-contact":
                            print(self.contacts_commands.find_contact(args))
                        elif command == "edit-contact":
                            print(self.contacts_commands.edit_contact(args))
                        elif command == "delete-contact":
                            print(self.contacts_commands.delete_contact(args))
                        elif command == "add-birthday":
                            print(self.contacts_commands.add_birthday(args))
                        elif command == "show-birthday":
                            print(self.contacts_commands.show_birthday(args))
                        elif command == "upcoming-birthdays":
                            print(self.contacts_commands.upcoming_birthdays(args))
                        elif command == "all-contacts":
                            print(self.contacts_commands.all_contacts(args))
                        elif command == "add-note":
                            print(self.notes_commands.add_note(args))
                        elif command == "delete-note":
                            print(self.notes_commands.delete_note(args))
                        elif command == "find-note":
                            print(self.notes_commands.find_note(args))
                        elif command == "edit-note":
                            print(self.notes_commands.edit_note(args))
                        elif suggested_command == "add-tag":
                            print("Adding tag...")
                        elif suggested_command == "remove-tag":
                            print("Removing tag...")
                        elif suggested_command == "all-notes":
                            print(self.notes_commands.all_notes(args))
                    else:
                        print("Unknown command. Try typing 'hello' for help.")
            except KeyboardInterrupt:
                print("\nUse 'exit' or 'close' to exit the program.")
            except EOFError:
                print("\nGood bye!")
                break
