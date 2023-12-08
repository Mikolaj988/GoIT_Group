class Note:
    def __init__(self,tag,note):
        self.tag=tag
        self.note=note
        self.tryger=set()
    def add_tag(self,tags):
        sels.tryger.add(tags)
    def __repr__(self):
        return f("Note: {tag}\n,Treść: {note}\n, \nTags: {', '.join(self.tryger)} ")
class NoteCollection:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def search_notes_by_tag(self, tag):
        return [note for note in self.notes if tag in note.tags]

    def sort_notes_by_tag(self, tag):
        return sorted(self.notes, key=lambda note: tag in note.tags)

    def __repr__(self):
        return '\n\n'.join(map(str, self.notes))