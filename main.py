
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
def main():
    # contacts = AddressBook()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            pass
            # print(add_contact(args, contacts))
        elif command == "change":
            pass
            # print(change_contact(args, contacts))
        elif command == "phone":
            pass
            # print(get_phone(args, contacts))
        elif command == "add-birthday":
            pass
            # print(add_birthday(args, contacts))
        elif command == "show-birthday":
            pass
            # print(show_birthday(args, contacts))
        elif command == "birthdays":
            pass
            # print(birthdays(contacts))
        elif command == "all":
            pass
            # print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()