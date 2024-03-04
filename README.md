# Homework #3

A virtual assistant with a command line interface (CLI)

## General acceptance criteria

* The repository `goitneo-python-hw-3-group-name` has been created.
* The homework contains a link to the GitHub repository and an attached repository file in `zip` format.
* The tasks are completed strictly per the technical description (recommendations for completion and grading criteria).
* The console has no errors or warnings when running the bot.
* The names of variables and functions are clear and descriptive.
* The code is formatted and complies with the PEP8 standard.

## Task #1

### Technical description:

Continue to develop the virtual assistant with a CLI interface from the homework 2 and combine it with the birthdays processing from the homework 1.

* Add a field for birthday - the `Birthday` class. This field is optional, but there can be only one.
* Let's add the functionality of working with `Birthday` to the `Record` class, particularly the `add_birthday` function, which adds a birthday to a contact.
* Let's add the checking functionality to correct the entered values for the `Phone` and `Birthday` fields.
* Let's add our function to the `AddressBook` class from the first homework assignment. This function is the `get_birthdays_per_week`, which returns a list of users who must be congratulated for the contacts in the address book the following week.

To implement the new functionality, also add handlers with the following commands:

* `add-birthday` — add a birthday to the contact in the format `DD.MM.YYYY`.
* `show-birthday` — show the contact's birthday.
* `birthdays` — returns a list of users who need to be congratulated on days in the next week

So, our bot should support the following list of commands:

1. `add` `[name]` `[phone]`: Add a new contact with a name and phone number.
2. `change` `[name]` `[new phone]`: Change the phone number for the specified contact.
3. `phone` `[name]`: Show the phone number for the specified contact.
4. `all`: Show all contacts in the address book.
5. `add-birthday` `[name]` [birth date]: Add a date of birth for the specified contact.
6. `show-birthday` `[name]`: Show the date of birth for the specified contact.
7. `birthdays`: Show birthdays that will take place within the next week.
8. `hello`: Receive a greeting from a bot.
9. `close` or `exit`: Close the app.

### Evaluation criteria:

1. Implement all the specified commands to the bot.
2. All data should be output in a clear and user-friendly format.
3. All errors, such as incorrect input or missing contact, should be adequately handled with an appropriate message to the user.
4. Data validation:
    * The date of birth should be in the format `DD.MM.YYYY`.
    * The phone number must consist of `10` digits.
5. The program should be closed correctly after executing the `close` or `exit` commands.

## Task 2

### Technical description:

Add the functionality of saving the address book to disk and restoring it from disk. To do this, you can choose any data serialization/deserialization protocol that suits you and implement methods that will allow you to save all data to a file and load it from a file. The main goal is to ensure that the application does not lose data after exiting the application and restores it from the file when it starts.
