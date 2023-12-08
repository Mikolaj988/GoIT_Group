import json
from classes import Record, Phone
from notebook import NoteCollection, Note


# Kule dla wyciągania numerów z listy [...] w string.
def extract_phone(phone_list):
    return ', '.join(str(Phone(number)) for number in phone_list)


def to_json_book(address_book, filename):
    data_to_write = {
        name: {
            'name': str(record.name),
            'phone': list(map(str, record.phone)),
            'email': str(record.birthday),
            'birthday': str(record.birthday) if record.birthday else None
        } for name, record in address_book.data.items()
    }
    with open(filename, 'w') as data_file:
        json.dump(data_to_write, data_file, indent=2)


def from_json_book(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        records = {}

        for name, record_data in data.items():
            phone_list = record_data.get('phone', [])
            phone_string = extract_phone(phone_list)
            record = Record(
                name,
                phone_string,
                record_data.get('emaile'),
                record_data.get('birthday'),
            )
            records[name] = record
    return records


def to_json_note(note, filename):
    data_to_write = [
        {
            'tag': note.tag,
            'note': note.note,
            'tryger': list(note.tryger)
        } for note in note.notes
    ]
    with open(filename, 'w') as data_file:
        json.dump(data_to_write, data_file, indent=2)


def from_json_note(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        notes = []
        for note_data in data:
            note = Note(note_data['tag'], note_data['note'])
            note.tryger = set(note_data['tryger'])
            notes.append(note)
        notepad = NoteCollection()
        notepad.notes = notes
        return notepad
