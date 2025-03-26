import re

from src.models.contact.field import Field


class Email(Field):
    def __init__(self, value):
        if not self._is_valid_email(value):
            raise ValueError("Invalid email format. Use example@domain.com")
        super().__init__(value)

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Перевірка email за допомогою регулярного виразу"""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def __repr__(self):
        return f"Email({self.value})"
