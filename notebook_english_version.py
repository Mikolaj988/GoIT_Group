import json


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text


class Notepad:
    def __init__(self):
        self.notes = []

    def add_note(self, title, text):
        self.notes.append(Note(title, text))

    def find_note(self, title):
        for note in self.notes:
            if note.title == title:
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


def start_notepad():
    notepad = Notepad()
    while True:
        command = input(
            "Enter the command (add, find, edit, delete, save, load, display, quit): ")
        if command == "add":
            title = input("Enter a title for the note: ")
            text = input("Enter the note text: ")
            notepad.add_note(title, text)
        elif command == "find":
            title = input("Enter a title for the note: ")
            note = notepad.find_note(title)
            if note:
                print(f'Note found: {note.title} - {note.text}')
            else:
                print("Note not found")
        elif command == "edit":
            title = input("Enter a title for the note: ")
            note = notepad.find_note(title)
            if note:
                print(f'Current note text: {note.text}')
                new_text = input(
                    "Enter new note text or leave the field blank to keep the current text: ")
                if new_text:
                    notepad.edit_note(title, new_text)
            else:
                print("Note not found")
        elif command == "delete":
            title = input("Enter a title for the note: ")
            notepad.delete_note(title)
        elif command == "save":
            filename = input("Enter a file name: ")
            try:
                notepad.save_to_disk(filename)
            except FileNotFoundError:
                print(
                    "Error: Failed to save the file. Check the file name and path.")
        elif command == "load":
            filename = input("Enter a file name: ")
            try:
                notepad.load_from_disk(filename)
            except FileNotFoundError:
                print("Error: File not found. Check the file name and path.")
        elif command == "display":
            notepad.display_notes()
        elif command == "quit":
            break
        else:
            print(
                "Unknown indication. Enter one of the commands below:\nadd - Add a note\nfind - Find the note\nedit - Edit note\ndelete - Delete note\nsave - Save the note\nload - Download notes\ndisplay - Show all notes\nquit - Quit using the notebook"
            )


start_notepad()
