from src.models.notes.tag import Tag
from src.models.notes.text import Text
from src.models.notes.title import Title
from src.utils.find_elements import find_element


class Note:
    def __init__(self, title, text):
        self.title = Title(title)
        self.text = Text(text)
        self.tags = []

    def _find_tag(self, tag):
        return find_element(self.tags, lambda x: x.value == tag)

    def add_tag(self, tag):
        if not self._find_tag(tag):
            self.tags.append(Tag(tag))
            return f"Tag {tag} was added to {self.title.value} note."
        else:
            return f"Tag {tag} already exists in {self.title.value} note."
        
    def remove_tag(self, tag):
        if self._find_tag(tag):
            self.tags = list(filter(lambda x: x.value != tag, self.tags))
            return f"Tag {tag} was removed from {self.title.value} note."
        else:
            return f"Tag {tag} doesn't exist in {self.title.value} note."

    def __repr__(self):
        return f"Note({self.title.value}, {self.text.value})"

    def __str__(self):
        tags = "No tags were added"
        if len(self.tags):
            tags = ", ".join(list(map(lambda x: x.value, self.tags)))
        return f"Title: {self.title.value}\n    Tags: {tags}\n    Text: {self.text.value}"

