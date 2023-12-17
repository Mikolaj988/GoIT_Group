import json
class Notepad:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def find_note(self, title):
        for note in self.notes:
            if note.tag == title:
                return note
        return None

    def edit_note(self, title, new_text):
        note = self.find_note(title)
        if note:
            note.text = new_text

    def delete_note(self, title):
        note = self.find_note(title)
        if note:
            self.notes.remove(note)

    def save_to_disk(self, filename):
        with open(filename, 'w') as f:
            json.dump([note.__dict__ for note in self.notes], f)

    def load_from_disk(self, filename):
        with open(filename, 'r') as f:
            self.notes.extend([Note(**note) for note in json.load(f)])

    def display_notes(self):
        for note in self.notes:
            print(f'Title of the note: {note.title}\n {note.text}\n')

    def sort_notes_by_tag(self, tag):
        return sorted(self.notes, key=lambda note: tag in note.tag)


class Note:
    def __init__(self, tag, note):
        self.tag = tag
        self.note = note
        self.tryger = set()

    def add_tag(self, tags):
        self.tryger.add(tags)

    def __repr__(self):
        return f"Note: {self.tag}\nTreść: {self.note}\n\nTags: {', '.join(self.tryger)} "


