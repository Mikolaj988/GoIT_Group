from notebook import Note, NoteBook
from serialization import to_json_note, from_json_note


# Создаем экземпляр NoteBook
notebook = NoteBook()


# Создаем экземпляр Note
note1 = Note("Example Note 1", "This is an example note.")
note2 = Note("Example Note 2", "This is an example note.")


# Добавляем теги к заметке
note1.add_tag("banana")
note2.add_tag("salami")
note2.add_tag("apple")


# Сохраняем NoteBook в файл JSON
notebook.add_note(note1)
notebook.add_note(note2)
filename = "notebook.json"
to_json_note(notebook, filename)


# Загружаем NoteBook из файла JSON
loaded_notebook = from_json_note(filename)


# Выводим содержимое загруженного NoteBook
print(f"Loaded NoteBook:\n{loaded_notebook}")


# Поиск заметки по тегу
tag_to_search = "apple"
matching_notes = loaded_notebook.search_tag(tag_to_search)
print(f"Notes with tag '{tag_to_search}':\n{matching_notes}")

tag_to_search = "banana"
matching_notes = loaded_notebook.search_tag(tag_to_search)
print(f"Notes with tag '{tag_to_search}':\n{matching_notes}")


# # Поиск заметки по заголовку
title_to_search = "Example"
matching_notes = loaded_notebook.search_note(title_to_search)
print(f"Notes with title '{title_to_search}':\n{matching_notes}")

title_to_search = "Notes"
matching_notes = loaded_notebook.search_note(title_to_search)
print(f"Notes with title '{title_to_search}':\n{matching_notes}")


# Сортировка по тагу
note_sorted_by_tag = loaded_notebook.sort_tag()
print(f"Sorted by Tag:\n{note_sorted_by_tag}")


# Удаление заметки
note_to_delete = "Example Note 3"
loaded_notebook.delete_note(note_to_delete)

note_to_delete = "Example Note 1"
loaded_notebook.delete_note(note_to_delete)


# Выводим обновленное содержимое NoteBook
print(f"Updated NoteBook:\n{loaded_notebook}")
