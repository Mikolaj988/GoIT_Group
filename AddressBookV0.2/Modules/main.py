from addressbook import Contact, AddressBook
from notebook import Note, NoteBook
from serialization import to_json_note, from_json_note

# NoteBook
# # Create a NoteBook
# notebook = NoteBook()
#
#
# # Create a Note
# note1 = Note("Example Note 1", "This is an example note.")
# note2 = Note("Example Note 2", "This is an example note.")
#
#
# # Adding tags to a note
# note1.add_tag("banana")
# note2.add_tag("salami")
# note2.add_tag("apple")
#
#
# # Save NoteBook to JSON file
# notebook.add_note(note1)
# notebook.add_note(note2)
# filename = "notebook.json"
# to_json_note(notebook, filename)
#
#
# # Loading NoteBook from JSON file
# loaded_notebook = from_json_note(filename)
#
#
# # Displaying the contents of the downloaded NoteBook
# print(f"Loaded NoteBook:\n{loaded_notebook}")
#
#
# # Search for a note by tag
# tag_to_search = "apple"
# matching_notes = loaded_notebook.search_tag(tag_to_search)
# print(f"Notes with tag '{tag_to_search}':\n{matching_notes}")
#
# tag_to_search = "banana"
# matching_notes = loaded_notebook.search_tag(tag_to_search)
# print(f"Notes with tag '{tag_to_search}':\n{matching_notes}")
#
#
# # Search note by title
# title_to_search = "Example"
# matching_notes = loaded_notebook.search_note(title_to_search)
# print(f"Notes with title '{title_to_search}':\n{matching_notes}")
#
# title_to_search = "Notes"
# matching_notes = loaded_notebook.search_note(title_to_search)
# print(f"Notes with title '{title_to_search}':\n{matching_notes}")
#
#
# # Sorting by tag
# note_sorted_by_tag = loaded_notebook.sort_tag()
# print(f"Sorted by Tag:\n{note_sorted_by_tag}")
#
#
# # Deleting a note
# note_to_delete = "Example Note 3"
# loaded_notebook.delete_note(note_to_delete)
#
# note_to_delete = "Example Note 1"
# loaded_notebook.delete_note(note_to_delete)
#
#
# # Displaying updated NoteBook contents
# print(f"Updated NoteBook:\n{loaded_notebook}")

# AddressBook
# Create a Contact
# contact1 = Contact("John Doe")
# print(contact1)
#
# contact1.add_birthday("12.01.1990")
# print(contact1)

# # Add phone number
# contact1.add_phone("9876543210")
# print(contact1)  # ['1234567890', '9876543210']
#
# # Delete phone number
# contact1.delete_phone("1234567890")
# print(contact1)  # ['9876543210']
#
# # Edit phone number
# contact1.edit_phone("9876543210", "5555555555")
# print(contact1)  # ['5555555555']
#
# # Add more birthday
# contact1.add_birthday("01.01.1990")
# # Contact already haw birth date
#
# # Edite birthday
# contact1.edit_birthday("03.03.1980")
#
# # Wrong birthday edition
# contact1.edit_birthday("04.31.1975")
# print(contact1)
#
# # Delete Birthday
# contact1.delete_birthday("04.10.1975")
# contact1.delete_birthday("01.01.1990")
#
# # Add more email
# contact1.add_email("john2@example.com")
# # Contact already haw Email
# print(contact1)
#
# # Edite email
# contact1.edit_email("john.doe@example.com")
#
# # Delete email
# contact1.delete_email("john@example.com")
# contact1.delete_email("john.doe@example.com")
# print(contact1)

# Załóżmy, że masz już utworzoną klasę AddressBook i Contact.

# Tworzenie obiektu Contact
new_contact = Contact("John Doe", phone="1234567890", birthday="01.01.1990", email="john@example.com")

# Utworzenie książki adresowej
address_book = AddressBook()

# Dodanie nowego kontaktu do książki adresowej
address_book.rec_add(new_contact)

# Wyświetlenie zawartości książki adresowej
print(address_book)