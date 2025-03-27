from src.models.notes.note_book import NoteBook
from src.commands.notes.delete_note import delete_note
from src.commands.notes.add_note import add_note
from src.storage.storage_manager import StorageManager
from src.utils.command_suggester import CommandSuggester
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style


class AssistantBot:
    def __init__(self):
        self.storage_manager = StorageManager()
        # self.contacts_book
        self.notes_book = self.storage_manager.get_note_storage()
        # self.notes_book = NoteBook()
        self.command_suggester = CommandSuggester()
        
        self.style = Style.from_dict({
            'prompt': 'ansicyan bold',
        })
        
        self.session = PromptSession(
            completer=self.command_suggester.completer,
            style=self.style,
            complete_while_typing=True
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
            description = self.command_suggester.get_command_description(suggested_command)
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
                    print("Adding contact...")
                elif command == "find-contact":
                    print("Finding contact...")
                elif command == "edit-contact":
                    print("Editing contact...")
                elif command == "delete-contact":
                    print("Deleting contact...")
                elif command == "add-birthday":
                    print("Adding birthday...")
                elif command == "show-birthday":
                    print("Showing birthday...")
                elif command == "upcoming-birthdays":
                    print("Showing upcoming birthdays...")
                elif command == "all-contacts":
                    print("Showing all contacts...")
                elif command == "add-note":
                    print("Adding note...")
                    print(add_note(args, self.notes_book))
                elif command == "delete-note":
                    print("Deleting note...")
                    print(delete_note(args, self.notes_book))
                elif command == "find-note":
                    print("Finding note...")
                elif command == "edit-note":
                    print("Editing note...")
                elif command == "add-tag":
                    print("Adding tag...")
                elif command == "remove-tag":
                    print("Removing tag...")
                elif command == "all-notes":
                    print("Showing all notes...")
                    print(self.notes_book.data)
                else:
                    suggested_command = self._suggest_command(user_input)
                    
                    if suggested_command:
                        print(f"Running '{suggested_command}'...")
                        print(f"Command '{suggested_command}' executed.")
                    else:
                        print("Unknown command. Try typing 'hello' for help.")
            except KeyboardInterrupt:
                print("\nUse 'exit' or 'close' to exit the program.")
            except EOFError:
                print("\nGood bye!")
                break
