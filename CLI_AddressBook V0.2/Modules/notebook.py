from collections import UserDict
from serialization import to_json_note, from_json_note


class Note:
    def __init__(self, title, text=None, tags=None):
        self._title = title
        self._tags = tags or []
        self._text = text

    def add_tag(self, tags):
        self._tags.append(tags)

    def delete_tag(self, tag):
        self._tags = [i for i in self._tags if str(i) != tag]
        if not self._tags:
            print(f'All tags hase ben deleted.')

    def rewrite_note(self, new_title=None, new_text=None):
        if new_title is not None:
            self._title = new_title
        if new_text is not None:
            self._text = new_text

    def __str__(self):
        return (f'Title: {self._title}\n'
                f'Tag: {", ".join(map(str, self._tags))}\n'
                f'Text: {self._text if self._text else ""}\n')


class NoteBook(UserDict):
    def __init__(self, records: dict = None):
        super().__init__(records or {})

    def search_tag(self, tag):
        ...

    def search_note(self, title):
        ...

    def sort_tag(self):
        pass

    def add_note(self, record: Note):
        if record._title is None:
            raise ValueError(f'Error: The contact cannot be created.\n')
        else:
            self.data[record._title] = record

    def delete_note(self, title):
        if title in self.data:
            del self.data[title]
            print(f"Note {title} exterminated successfully ;)\n")
        else:
            print(f"Note {title} not found in the address book.\n")

    def __str__(self):
        return "\n".join(str(note) for note in self.data.values())


# Создаем экземпляр NoteBook
notebook = NoteBook()

# Создаем экземпляр Note
note = Note("Example Note", "This is an example note.")

# Добавляем теги к заметке
note.add_tag(["tag1", "tag2"])

# Добавляем заметку в NoteBook
notebook.add_note(note)

# Выводим содержимое NoteBook
print("Initial NoteBook:")
print(notebook)

# Сохраняем NoteBook в файл JSON
filename = "notebook.json"
to_json_note(notebook, filename)
print(f'NoteBook saved to {filename}\n')

# Загружаем NoteBook из файла JSON
loaded_notebook = from_json_note(filename)

# Выводим содержимое загруженного NoteBook
print("Loaded NoteBook:")
print(loaded_notebook)

# Поиск заметки по тегу
tag_to_search = "tag1"
matching_notes = loaded_notebook.search_tag(tag_to_search)
print(f"Notes with tag '{tag_to_search}':")
print(matching_notes)

# Поиск заметки по заголовку
title_to_search = "Example"
matching_notes = loaded_notebook.search_note(title_to_search)
print(f"Notes with title '{title_to_search}':")
print(matching_notes)

# Удаление заметки
note_to_delete = "Example Note"
loaded_notebook.delete_note(note_to_delete)

# Выводим обновленное содержимое NoteBook
print("Updated NoteBook:")
print(loaded_notebook)

