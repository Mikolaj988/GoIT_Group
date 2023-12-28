from collections import UserDict


class Note:
    def __init__(self, title, tag=None, text=None):
        self._title = title
        self._tag = tag
        self._text = text

    def add_tag(self, tag):
        pass

    def delete_tag(self, tag):
        pass

    def edit_note(self, title, text=None):
        pass

    def __str__(self):
        return (f'Title: {self._title}'
                f'Tag: {", ".join(map(str, self._tag))}'
                f'Text: {self._text}')


class NoteBook(UserDict):
    def __init__(self, records={}):
        super().__init__(records)

    def search_tag(self):
        pass

    def search_note(self):
        pass

    def sort_tag(self):
        pass

    def add_note(self):
        pass

    def delete_note(self):
        pass

    def __str__(self, note=None):
        pass

