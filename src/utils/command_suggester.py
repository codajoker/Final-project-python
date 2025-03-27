from difflib import get_close_matches
from prompt_toolkit.completion import Completer, Completion


class CommandCompleter(Completer):
    def __init__(self, command_suggester):
        self.command_suggester = command_suggester
        
    def get_completions(self, document, complete_event):
        word = document.get_word_before_cursor()
        if not word:
            for command in self.command_suggester.available_commands:
                description = self.command_suggester.get_command_description(command)
                yield Completion(
                    command, 
                    start_position=-len(word),
                    display=command,
                    display_meta=description
                )
        else:
            for command in self.command_suggester.available_commands:
                if command.startswith(word.lower()):
                    description = self.command_suggester.get_command_description(command)
                    yield Completion(
                        command, 
                        start_position=-len(word),
                        display=command,
                        display_meta=description
                    )


class CommandSuggester:
    def __init__(self):
        self.available_commands = [
            "hello", "close", "exit", "add-contact", "find-contact", 
            "edit-contact", "delete-contact", "add-birthday", "show-birthday", 
            "upcoming-birthdays", "all-contacts", "add-note", "delete-note", 
            "find-note", "edit-note", "add-tag", "remove-tag", "all-notes"
        ]
        
        self.command_descriptions = {
            "hello": "greet the assistant",
            "close": "close the program",
            "exit": "exit the program",
            "add-contact": "add a new contact",
            "find-contact": "find a contact",
            "edit-contact": "edit an existing contact",
            "delete-contact": "delete a contact",
            "add-birthday": "add a birthday to a contact",
            "show-birthday": "show a contact's birthday",
            "upcoming-birthdays": "show upcoming birthdays",
            "all-contacts": "show all contacts",
            "add-note": "add a new note",
            "delete-note": "delete a note",
            "find-note": "find a note",
            "edit-note": "edit a note",
            "add-tag": "add a tag to a note",
            "remove-tag": "remove a tag from a note",
            "all-notes": "show all notes"
        }
        
        self.command_keywords = {}
        for cmd in self.available_commands:
            self.command_keywords[cmd] = [cmd]
        
        self.completer = CommandCompleter(self)
    
    def suggest_command(self, user_input):
        user_input = user_input.lower().strip()
        matches = get_close_matches(user_input, self.available_commands, n=1, cutoff=0.5)
        return matches[0] if matches else None
    
    def get_command_description(self, command):
        return self.command_descriptions.get(command, "unknown command")
