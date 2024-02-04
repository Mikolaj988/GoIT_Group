import sys
from messages import MESSAGES
from addressbook import Contact, AddressBook
from notebook import Note, NoteBook
from serialization import to_json_note, from_json_note, to_json_addressbook, from_json_addressbook
from colorama import Fore, Style, init


notebook = NoteBook()

notebook = from_json_note('notebook.json')

print(notebook)

title_to_untag = 'qwe'
note = notebook.data[title_to_untag]
print(note)
tag_to_delete = 'asd'
note.delete_tag(tag_to_delete)
print(note)