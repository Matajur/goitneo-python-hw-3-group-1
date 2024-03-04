"""Module providing the classes to manage the contacts in a contact book"""

from collections import UserDict
from datetime import datetime


class BirthdayFormatError(Exception):
    """
    Incorrect birthday format error.
    """


class BirthdayValidationError(Exception):
    """
    Incorrect birthday date error.
    """


class NameValidationError(Exception):
    """
    Incorrect name format error.
    """


class PhoneIndexError(Exception):
    """
    Incorrect phone index error.
    """


class PhoneValidationError(Exception):
    """
    Incorrect phone number format error.
    """


class RecordValidationError(Exception):
    """
    Error of creating an entry with an existing name in the contact book.
    """


class Field:
    """
    A base class for record fields.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Birthday(Field):
    """
    A class for storing a birthday. Has format validation (DD.MM.YYYY).
    """

    @property
    def value(self):
        """
        A method that validates name.
        """
        return self._value

    @value.setter
    def value(self, birthday):
        """
        A method that validates name.
        """
        try:
            birth = datetime.strptime(birthday, "%d.%m.%Y").date()
        except ValueError as exc:
            raise BirthdayFormatError() from exc
        if not 0 < (datetime.today().date() - birth).days < 100 * 365.4:
            raise BirthdayValidationError()
        self._value = datetime.strptime(birthday, "%d.%m.%Y").date()

    def __str__(self):
        return str(self.value.strftime("%d.%m.%Y"))


class Name(Field):
    """
    A class for storing a contact name. Required field, min 3 characters.
    """

    @property
    def value(self):
        """
        A method that validates name.
        """
        return self._value

    @value.setter
    def value(self, name):
        """
        A method that validates name.
        """
        if len(str(name)) < 3:
            raise NameValidationError()
        self._value = name


class Phone(Field):
    """
    A class for storing a phone number. Has format validation (10 digits).
    """

    @property
    def value(self):
        """
        A method that validates phone number.
        """
        return self._value

    @value.setter
    def value(self, phone):
        """
        A method that validates phone number.
        """
        if not str(phone).isdecimal() or len(str(phone)) != 10:
            raise PhoneValidationError()
        self._value = phone


class Record:
    """
    A class for storing information about a contact, including name and contacts list.
    """

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        """
        A method that adds a birthday to the record.
        """
        self.birthday = Birthday(birthday)

    def add_phone(self, phone: str):
        """
        A method that adds a new phone number to the record.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
        A method that removes a phone number from the record.
        """
        index = self.find_phone(phone)
        self.phones.pop(index)

    def edit_phone(self, phones: list):
        """
        A method that edits a phone number in the record.
        """
        index = self.find_phone(phones[0])
        self.phones[index] = Phone(phones[1])

    def find_phone(self, phone: str):
        """
        A method that finds an index of the phone number in the record.
        """
        index = 0
        for item in self.phones:
            if item.value == phone:
                return index
            index += 1
        raise PhoneIndexError()

    def __str__(self) -> str:
        numbers = '; '.join(p.value for p in self.phones) if self.phones else None
        return f"Contact name: {self.name.value}, phones: {numbers}, birthday: {self.birthday}"


class AddressBook(UserDict):
    """
    A class for storing and managing records.
    """

    def add_record(self, record: Record) -> None:
        """
        A method that adds a record to the address book.
        """
        if str(record.name) in self.data.keys():
            raise RecordValidationError()
        self.data[str(record.name)] = record

    def find(self, name: str) -> Record:
        """
        A method that finds a record in the address book.
        """
        return self.data[name]

    def delete(self, name: str) -> None:
        """
        A method that removes a record from the address book.
        """
        self.data.pop(name)
