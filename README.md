# Aysusdito | Django

"Aysusdito" a parody of an old consumer-to-consumer website called "Ayosdito"

My channel:
[Leepogi](https://www.youtube.com/watch?v=oHg5SJYRHA0)

## Getting Started (Run the Project)

Prerequisites:
- Python 3.9+
- pip

Setup (Windows PowerShell):
1. Create and activate a virtual environment:
	- `py -3 -m venv .venv`
	- `.\.venv\Scripts\Activate.ps1`
2. Install dependencies:
	- `pip install -r requirements.txt`
3. Apply migrations:
	- `python manage.py migrate`
4. Load seed data:
	- `python manage.py seed_data`
5. Run the server:
	- `python manage.py runserver`

Setup (macOS/Linux):
1. Create and activate a virtual environment:
	- `python3 -m venv .venv`
	- `source .venv/bin/activate`
2. Install dependencies:
	- `pip install -r requirements.txt`
3. Apply migrations:
	- `python manage.py migrate`
4. Load seed data:
	- `python manage.py seed_data`
5. Run the server:
	- `python manage.py runserver`

Then open `http://127.0.0.1:8000/` in your browser.

## Author
This website is managed by Lee Pogi.

[Leepogi](https://www.youtube.com/watch?v=oHg5SJYRHA0)

## Admin Account:

Username: leepogi

Email: leepogi@gmail.com

Password: leepogi

## Existing Users(For Demonstration)

Username: hevabi

Password: downtown123

Username: rickowens

Password: downtown123

## Seed Data

This project includes a fixture at `fixtures/seed.json` and media files under `media/`.
Running `python manage.py seed_data` loads the demo items and users.

## Troubleshooting

- If the virtual environment does not activate in PowerShell, try opening a new PowerShell window or use Command Prompt.
- Make sure you are using Python 3.9+ and that your virtual environment is active before running migrations.




## This Project Is Made For The Sole Purpose of Fulfilling Academic Activities/Requirements Only.