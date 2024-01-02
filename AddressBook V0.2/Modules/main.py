from notebook import Note, NoteBook
from serialization import to_json_note, from_json_note


# Create a NoteBook
notebook = NoteBook()


# Create a Note
note1 = Note("Example Note 1", "This is an example note.")
note2 = Note("Example Note 2", "This is an example note.")


# Adding tags to a note
note1.add_tag("banana")
note2.add_tag("salami")
note2.add_tag("apple")


# Save NoteBook to JSON file
notebook.add_note(note1)
notebook.add_note(note2)
filename = "notebook.json"
to_json_note(notebook, filename)


# Loading NoteBook from JSON file
loaded_notebook = from_json_note(filename)


# Displaying the contents of the downloaded NoteBook
print(f"Loaded NoteBook:\n{loaded_notebook}")


# Search for a note by tag
tag_to_search = "apple"
matching_notes = loaded_notebook.search_tag(tag_to_search)
print(f"Notes with tag '{tag_to_search}':\n{matching_notes}")

tag_to_search = "banana"
matching_notes = loaded_notebook.search_tag(tag_to_search)
print(f"Notes with tag '{tag_to_search}':\n{matching_notes}")


# Search note by title
title_to_search = "Example"
matching_notes = loaded_notebook.search_note(title_to_search)
print(f"Notes with title '{title_to_search}':\n{matching_notes}")

title_to_search = "Notes"
matching_notes = loaded_notebook.search_note(title_to_search)
print(f"Notes with title '{title_to_search}':\n{matching_notes}")


# Sorting by tag
note_sorted_by_tag = loaded_notebook.sort_tag()
print(f"Sorted by Tag:\n{note_sorted_by_tag}")


# Deleting a note
note_to_delete = "Example Note 3"
loaded_notebook.delete_note(note_to_delete)

note_to_delete = "Example Note 1"
loaded_notebook.delete_note(note_to_delete)


# Displaying updated NoteBook contents
print(f"Updated NoteBook:\n{loaded_notebook}")
