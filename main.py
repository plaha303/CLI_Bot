CONTACTS = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please enter name and phone number separated by a space."
        except IndexError:
            return "Invalid input. Please enter a command."
        except TypeError:
            return func()
    return wrapper


@input_error
def hello():
    return "How can I help you?"


@input_error
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    CONTACTS[name] = phone
    return "Contact added successfully."


@input_error
def change_phone():
    name = input("Enter the name: ")
    phone = input("Enter the new phone number: ")
    CONTACTS[name] = phone
    return "Phone number updated successfully."


@input_error
def get_phone():
    name = input("Enter the name: ")
    return CONTACTS[name]


@input_error
def show_all():
    if not CONTACTS:
        return "No contacts found."
    contacts_list = "\n".join(f"{name}: {phone}" for name, phone in CONTACTS.items())
    return contacts_list


def helper():
    commands = {
        hello: "hello -> displays a welcome message.",
        add_contact: "add -> adds a new contact.",
        change_phone: "change -> changes the phone number of an existing contact.",
        get_phone: "phone -> displays the phone number of a contact.",
        show_all: "show all -> displays all contacts and their phone numbers.",
        helper: "help -> displays the list of available commands.",
        exit: "exit, close, good bye -> exits the program."
    }
    help_text = "Available commands:\n"
    for command, description in commands.items():
        help_text += f"{description}\n"
    return help_text


def main():
    print("Welcome!")
    commands = {
        "hello": hello,
        "add": add_contact,
        "change": change_phone,
        "phone": get_phone,
        "show all": show_all,
        "help": helper,
        "exit": exit,
        "good bye": exit,
        "close": exit
    }

    while True:
        command = input("Enter a command: ").lower()

        if command in commands:
            if command == "exit":
                print("Good bye!")
                break
            elif command == "help":
                print(commands[command]())
            else:
                func = commands[command]
                print(func())
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
