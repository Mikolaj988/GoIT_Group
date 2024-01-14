import json
from notebook import Note, NoteBook
from addressbook import Contact, AddressBook


def to_json_note(notebook, filename):
    notepad_data = {
        note.title: {
            "title": note.title,
            "text": note.text,
            "tags": note.tags,
        }
        for note in notebook.data.values()
    }
    with open(filename, "w") as data_file:
        json.dump(notepad_data, data_file, indent=4)


def from_json_note(filename):
    with open(filename, "r") as data_file:
        data = json.load(data_file)
        notes_dict = {}

        for title, note_data in data.items():
            note = Note(
                title,
                note_data.get("text", ""),
                ', '.join(map(str, note_data.get('tags', []))),
            )
            notes_dict[title] = note

        return NoteBook(notes_dict)


def to_json_addressbook(addressbook, filename):
    addressbook_data = {
        contact.name: {
            "name": contact.name,
            "phone": contact.phone,
            "birthday": contact.birthday,
            "email": contact.email,
        }
        for contact in addressbook.data.values()
    }
    with open(filename, "w") as data_file:
        json.dump(addressbook_data, data_file, indent=4)


def from_json_addressbook(filename):
    with open(filename, "r") as data_file:
        data = json.load(data_file)
        contact_dict = {}

        for name, addressbook_data in data.items():
            contact = Contact(
                name,
                ', '.join(map(str, addressbook_data.get('phone', []))),
                addressbook_data.get("birthday"),
                addressbook_data.get("email")
            )
            contact_dict[name] = contact

        return AddressBook(contact_dict)
