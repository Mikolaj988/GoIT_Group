from collections import UserDict
import curses


# stdscr = curses.initscr()
# curses.start_color()
# curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)


class Note:
    def __init__(self, title, text=None, tags=None):
        self._title = title
        self._tags = tags or []
        self._text = text

    def add_tag(self, tag):
        self._tags.append(tag)

    def delete_tag(self, tag):
        self._tags = [i for i in self._tags if str(i) != tag]
        if not self._tags:
            print(f'All tags have been deleted.')
            # stdscr.addstr(f'All tags have been deleted.', curses.color_pair(1))
            # stdscr.refresh()

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
        matching_records = [
            record for record in self.data.values() if any(tag.lower() in t.lower() for t in record._tags)
        ]
        if not matching_records:
            return "No records to display.\n"
        else:
            return self.__str__(matching_records)

    def search_note(self, title):
        matching_records = [
            note for note in self.data.values() if title.lower() in note._title.lower()
        ]
        if not matching_records:
            return "No records to display.\n"
        return self.__str__(matching_records)

    def sort_tag(self):
        for records in self.data.values():
            records._tags.sort()

        sorted_records = sorted(self.data.values(), key=lambda record: record._tags)
        return self.__str__(sorted_records)

    def add_note(self, record: Note):
        if record._title is None:
            raise ValueError(f'Error: Note cannot be created.\n')
        else:
            self.data[record._title] = record

    def delete_note(self, title):
        if title in self.data:
            del self.data[title]
            print(f"Note {title} deleted successfully\n")
        else:
            print(f"Note {title} not found in the address book.\n")

    def __str__(self, records=None):
        if records is None:
            return "\n".join(str(record) for record in self.data.values())
        else:
            return "\n".join(str(record) for record in records)


# curses.endwin()