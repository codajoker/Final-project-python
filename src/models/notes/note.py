class Note:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __repr__(self):
        return f"Note({self.name}, {self.text})"

    def __str__(self):
        return f"{self.name}: {self.text}"