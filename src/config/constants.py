import os

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.dat")
NOTES_FILE = os.path.join(DATA_DIR, "notes.dat")
