class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tryger = set()

    def add_tag(self, tags):
        self.tryger.add(tags)

    def __repr__(self):
        return f"Note: {self.title}\n, Tags: {', '.join(self.tryger)}\n, Content: {self.text}\n, "


class NoteCollection:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes_by_tag(self, tag):
        return [note for note in self.notes if tag in note.tryger]

    def sort_notes_by_tag(self, tag):
        return sorted(self.notes, key=lambda note: tag in note.tryger)

    def __repr__(self):
        return '\n\n'.join(map(str, self.notes))
