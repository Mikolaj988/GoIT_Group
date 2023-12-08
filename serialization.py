import json
from notebook import Note, NoteCollection
from classes import Record, AddressBook, Birthday
from datetime import datetime


def extract_phone(phone_list):
    return ', '.join(phone_list)


def format_birthday(birthday):
    return str(birthday.value) if birthday else None


def to_json_address_book(filename, address_book):
    data = {
        name: {
            'name': record.name.value,
            'phone': [phone.value for phone in record.fields.get('phones', [])],
            'email': [email.value for email in record.fields.get('emails', [])],
            'birthday': format_birthday(record.fields.get('birthday', [None])[0]),
        }
        for name, record in address_book.data.items()
    }
    with open(filename, 'w') as data_file:
        json.dump(data, data_file, indent=2)


def from_json_address_book(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        records = {}

        for name, record_data in data.items():
            phone_list = record_data.get('phone', [])
            phone_string = extract_phone(phone_list)

            email_list = record_data.get('email', [])
            email_string = ', '.join(email_list)

            birthday = record_data.get('birthday', None)

            record = Record(
                name,
                birthday,
            )

            record.add_field("phones", phone_string)
            record.add_field("emails", email_string)

            records[name] = record

        return AddressBook(records)


def to_json_note(note, filename):
    notepad_data = {
        "notes": [
            {
                "title": note.title,
                "text": note.text,
                "tags": list(note.tags)
            }
            for note in note.notes
        ]
    }
    with open(filename, 'w') as data_file:
        json.dump(notepad_data, data_file, indent=2)


def from_json_note(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        notes = []
        for note_data in data.get('notes', []):
            note = Note(note_data.get('title', ''), note_data.get('text', ''))
            note.tags = set(note_data.get('tags', []))
            notes.append(note)
        note = NoteCollection()
        note.notes = notes
        return note


# Tworzenie książki adresowej i dodawanie rekordów
address_book = AddressBook()
record1 = Record("John Doe", "1990-01-01")
record1.add_field("phones", "123456789")
record1.add_field("phones", "987654321")
record2 = Record("Jane Doe", "1995-02-15")
record2.add_field("emails", "jane@example.com")

address_book.add_record(record1)
address_book.add_record(record2)

# Zapis książki adresowej do pliku JSON
to_json_address_book("Data.json", address_book)

# Odczyt książki adresowej z pliku JSON
loaded_address_book = from_json_address_book("Data.json")

# Wyświetlenie wczytanej książki adresowej
print(loaded_address_book)


