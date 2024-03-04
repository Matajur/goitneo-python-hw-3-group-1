"""Module providing a console bot assistant with CLI"""

import pickle

from source.functions import get_command, parse_input
from source.classes import AddressBook


BACKUP = "source/backup.dat"


def loader() -> AddressBook:
    """
    Function to load saved contact book.

    :return: contact book
    """
    book = AddressBook()
    try:
        with open(BACKUP, "rb") as file:
            book.data = pickle.load(file)
    except FileNotFoundError:
        pass
    return book


def main() -> None:
    """
    Function that provides Command Line Interface.
    """
    print("Welcome to the assistant bot!")
    book = loader()
    if book.data:
        print("Contact book successfully loaded from backup.dat.")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            decision = input("Do you want to save changes? Y/N [Y]: ").lower()
            if decision in ("y", ""):
                saver(book)
                print("Changes saved, good bye!")
                break
            print("Good bye!")
            break

        print(get_command(command)(book, *args))


def saver(book: AddressBook) -> None:
    """
    Function to save contact book to file.

    :param book: contact book
    """
    if book.data:
        with open(BACKUP, "wb") as file:
            pickle.dump(book.data, file)


if __name__ == "__main__":
    main()
