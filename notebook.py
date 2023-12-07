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
            print(f'Tytuł notatki: {note.title}\n {note.text}\n')


def start_notepad():
    notepad = Notepad()
    while True:
        command = input(
            "Wprowadź polecenie (add, find, edit, delete, save, load, display, quit): ")
        if command == "add":
            title = input("Wprowadź tytuł notatki: ")
            text = input("Wprowadź tekst notatki: ")
            notepad.add_note(title, text)
        elif command == "find":
            title = input("Wprowadź tytuł notatki: ")
            note = notepad.find_note(title)
            if note:
                print(f'Znaleziono notatkę: {note.title} - {note.text}')
            else:
                print("Nie znaleziono notatki")
        elif command == "edit":
            title = input("Wprowadź tytuł notatki: ")
            note = notepad.find_note(title)
            if note:
                print(f'Aktualny tekst notatki: {note.text}')
                new_text = input(
                    "Wprowadź nowy tekst notatki lub pozostaw pole puste, aby zachować bieżący tekst: ")
                if new_text:
                    notepad.edit_note(title, new_text)
            else:
                print("Nie znaleziono notatki")
        elif command == "delete":
            title = input("Wprowadź tytuł notatki: ")
            notepad.delete_note(title)
        elif command == "save":
            filename = input("Wprowadź nazwę pliku: ")
            try:
                notepad.save_to_disk(filename)
            except FileNotFoundError:
                print(
                    "Błąd: Nie udało się zapisać pliku. Sprawdź nazwę pliku i ścieżkę.")
        elif command == "load":
            filename = input("Wprowadź nazwę pliku: ")
            try:
                notepad.load_from_disk(filename)
            except FileNotFoundError:
                print("Błąd: Nie znaleziono pliku. Sprawdź nazwę pliku i ścieżkę.")
        elif command == "display":
            notepad.display_notes()
        elif command == "quit":
            break
        else:
            print(
                "Nieznane wskazanie. Wprowadź jedno z poniższych poleceń:\nadd - Dodaj notatkę\nfind - Znajdź notatkę\nedit - Edytuj notatkę\ndelete - Usuń notatkę\nsave - Zapisz notatkę\nload - Pobierz notatki\ndisplay - Pokaż wszystkie notatki\nquit - Zakończ korzystanie z notatnika"
            )


start_notepad()
