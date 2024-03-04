"""Module providing a function to display a list of colleagues with upcoming birthdays"""

import calendar
from collections import defaultdict
from datetime import datetime, timedelta

from source.classes import AddressBook, Record

TODAY = datetime.now().date()
TIME_SPAN = 7  # days


def get_birthdays_per_week(book: AddressBook[Record, ...], *_) -> str:
    """
    Function to create a list of recods from contact book with upcoming birthdays.

    :param users_list: a list of dictionaries with users and their birthdays
    :return: a string of weekdays and people who have upcoming birthdays on these days
    """
    birthdays = defaultdict(list)

    for user in book.values():
        # remove users with an inappropriate age
        if user.birthday.value:
            birthday = user.birthday.value
            try:
                next_birthday = birthday.replace(year=TODAY.year)
            except ValueError:  # when birthday on February 29
                next_birthday = birthday.replace(year=TODAY.year, month=3, day=1)

            if TODAY.month == 12 and birthday.month == 1:  # for New Year's Eve
                next_birthday = next_birthday.replace(year=TODAY.year + 1)

            if next_birthday.weekday() == 5:
                next_birthday += timedelta(days=2)
            elif next_birthday.weekday() == 6:
                next_birthday += timedelta(days=1)

            if 0 <= (next_birthday - TODAY).days < TIME_SPAN:
                birthdays[next_birthday.weekday()].append(user.name.value)

    # sort defaultdict by numbers of weekdays
    birthdays = dict(sorted(birthdays.items()))
    if not birthdays:
        return "No upcoming birthdays"

    result = ""
    # check if there are birthdays this week
    this_week = dict(filter(lambda day: day[0] >= TODAY.weekday(), birthdays.items()))
    if this_week:
        result += "Birthdays this week:"
        for day, value in this_week.items():
            result += f"\n{calendar.day_name[day]}: {', '.join(value)}"

    # check if there are birthdays next week
    next_week = dict(filter(lambda day: day[0] < TODAY.weekday(), birthdays.items()))
    if next_week:
        result += "\nBirthdays next week:"
        for day, value in next_week.items():
            result += f"\n{calendar.day_name[day]}: {', '.join(value)}"

    return result.strip("\n")
