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

        self.notes_storage = self.storage_manager.get_note_storage()
        self.contact_storage = self.storage_manager.get_contact_storage()

        self.notes_book = NoteBook(storage=self.notes_storage)
        self.notes_commands = NoteCommands(self.notes_book, self.notes_storage)

        self.contacts_book = ContactBook(storage=self.contact_storage)
        self.contacts_commands = ContactCommands(
            self.contacts_book, self.contact_storage
        )

        self.command_suggester = CommandSuggester()
        self.style = Style.from_dict({"prompt": "ansicyan bold"})
        self.session = PromptSession(
            completer=self.command_suggester.completer,
            style=self.style,
            complete_while_typing=True,
        )

        self.command_handlers = {
            # Show help
            "help": self._cmd_hello,
            "hello": self._cmd_hello,
            # Contact commands
            "all-contacts": self.contacts_commands.all_contacts,
            "add-contact": self.contacts_commands.add_contact,
            "edit-contact": self.contacts_commands.edit_contact,
            "delete-contact": self.contacts_commands.delete_contact,
            "find-contact": self.contacts_commands.find_contact,
            "add-birthday": self.contacts_commands.add_birthday,
            "show-birthday": self.contacts_commands.show_birthday,
            "upcoming-birthdays": self.contacts_commands.upcoming_birthdays,
            # Note commands
            "all-notes": self.notes_commands.all_notes,
            "add-note": self.notes_commands.add_note,
            "edit-note": self.notes_commands.edit_note,
            "delete-note": self.notes_commands.delete_note,
            "find-note": self.notes_commands.find_note,
            "add-tag": lambda args: "Adding tag... (Not implemented)",
            "remove-tag": lambda args: "Removing tag... (Not implemented)",
            # "hello", "close", "exit" handled separately for clarity
        }

    @staticmethod
    def _parse_input(user_input: str):
        if not user_input.strip():
            return "", []
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    @staticmethod
    def _show_welcome_message():
        print("Welcome to the assistant bot!")
        print("Type 'hello' for help or start typing a command to see suggestions.")

    def _cmd_hello(self, args=None):
        print("How can I help you? Here are the commands:")
        for command in sorted(self.command_suggester.available_commands):
            description = self.command_suggester.get_command_description(command)
            print(f"  - {command}: {description}")

    def _suggest_command(self, user_input: str):
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

    def _execute_command(self, command: str, args: list[str]):
        if command in ["close", "exit"]:
            print("Good bye!")
            return True

        try:
            if command in self.command_handlers:
                result = self.command_handlers[command](args)
                if result:
                    print(result)
                return False

            suggested = self._suggest_command(" ".join([command] + args))
            if suggested:
                return self._execute_command(suggested, args)
            else:
                print("Unknown command. Try typing 'help' for help.")
            return False

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False

    def shutdown(self):
        self.storage_manager.save_all()

    def run(self):
        self._show_welcome_message()

        while True:
            try:
                user_input = self.session.prompt("Command > ")
                if not user_input:
                    print("Please enter a command.")
                    continue

                command, args = self._parse_input(user_input)
                should_exit = self._execute_command(command, args)
                if should_exit:
                    break

            except KeyboardInterrupt:
                print("\nUse 'exit' or 'close' to exit the program.")
            except EOFError:
                print("\nGood bye!")
                self.shutdown()
                break
