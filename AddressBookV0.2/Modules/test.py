import sys
from messages import MESSAGES
from addressbook import Contact, AddressBook
from notebook import Note, NoteBook
from serialization import to_json_note, from_json_note, to_json_addressbook, from_json_addressbook
from colorama import Fore, Style, init


# Tworzenie instancji Notatnika
notebook = NoteBook()

# Dodawanie notatek
note1 = Note("Shopping List", "Buy groceries", ["shopping", "food"])
note2 = Note("Meeting Notes", "Discuss project updates", ["meeting", "work"])

notebook.add_note(note1)
notebook.add_note(note2)

# Wyświetlanie zawartości notatnika
print("### Zawartość notatnika ###")
print(notebook)

# Wyszukiwanie notatek po tagu
print("\n### Wyszukiwanie po tagu 'shopping' ###")
print(notebook.search_tag("shopping"))

# Wyszukiwanie notatek po tytule
print("\n### Wyszukiwanie po tytule 'Shopping List' ###")
print(notebook.search_note("Shopping List"))

# Sortowanie notatek po tagach
print("\n### Sortowanie notatek po tagach ###")
print(notebook.sort_tag())

# Usuwanie notatki
print("\n### Usuwanie notatki 'Shopping List' ###")
notebook.delete_note("Shopping List")
print("### Aktualna zawartość notatnika ###")
print(notebook)