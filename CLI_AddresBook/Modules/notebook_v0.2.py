class Notepad:
    def __init__(self, title, text=None, tags=None):
        self.title = title
        self.text = text
        self.tags = tags

    def add_tag(self, tag):
        pass

    def edit_tag(self):
        pass

    def delete_tag(self):
        pass

    def search_tag(self):
        pass

    def sort_tag(self):
        pass

    def add_note(self):
        pass

    def edit_note(self):
        pass

    def delete_note(self):
        pass

    def search_note(self):
        pass

    def __str__(self):
        return (
            f"Note: {self.title}\n"
            f"Tags: {', '.join(self.tags)}\n"
            f"Content: {self.text}\n"
        )
