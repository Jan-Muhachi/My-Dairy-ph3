# My Diary.

This Python project implements a simple personal diary application using a SQLite database. Users can create accounts, write diary entries, and view or delete their entries.

## Features:

• User accounts with usernames and passwords (unique usernames enforced).

• Creation, viewing, searching by title, and deletion of diary entries.

• Timestamped diary entries (creation date).

• Personalized greetings based on the time of day.

## Technology:

• Python 3

• SQLAlchemy (for database interaction)

• SQLite (for data storage)


## How to Use:

Install Dependencies: You'll need to have sqlalchemy installed. You can install it using pip:

```Bash
pip install sqlalchemy
```
```Bash
pipenv install
```
```Bash
pipenv shell
```

Run the Application: Open a terminal in the project directory and run:

```Bash
python cli.py
```


## User Interface:

The application provides a text-based interface for user interaction. You'll be presented with a menu of options:

• Create an account (allows you to sign up for a new account)

• Login (lets you log in with an existing username and password)

• Exit (terminates the program)

#### Once logged in, you can access additional functionalities:

• Create a diary entry

• View all diary entries

• Find a diary entry by title

• Delete a diary entry

• Logout

## Security:

This is a basic implementation and currently stores passwords in plain text. This application will not allow the user to access the account without putting in the correct password. 

### Further Development:

• Implement data validation for user input.

• Add features like image or file attachment to diary entries.

• Implement functionalities for exporting or backing up diary entries.
