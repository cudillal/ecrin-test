# ECRIN Technical test - User To-do list
## Requirements
- Python 3.10 (tested with 3.10.11)
- Django 5.0.1
- Django REST framework 3.14.0
## Installation
Install the required packages previously mentioned. A `requirements.txt` file is provided for convenience.

## Usage

Run `python manage.py runserver` in the `todo_site` directory to start the server. Follow the server link that should appear in the terminal.

Users can create an account, log in, log out, add new tasks, edit existing tasks, and delete their tasks.

### REST API links
- `/api/users` to view your user info.
- `/api/tasks` to view and edit your task list.
