import json
from notebook import Note, NoteBook


def to_json_note(notebook, filename):
    notepad_data = {
        note._title: {
            "title": note._title,
            "text": note._text,
            "tags": note._tags,
        }
        for note in notebook.data.values()
    }
    with open(filename, 'w') as data_file:
        json.dump(notepad_data, data_file, indent=4)


def from_json_note(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        notes_dict = {}

        for title, note_data in data.items():
            note = Note(
                title,
                note_data.get('text', ''),
                note_data.get('tags', [])
            )
            notes_dict[title] = note

        return NoteBook(notes_dict)
