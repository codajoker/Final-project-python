import re

from src.models.contact.field import Field


class Email(Field):
    def __init__(self, value):
        normalized_value = value.lower().strip()
        
        if not self._is_valid_email(normalized_value):
            raise ValueError("Invalid email format. Use example@domain.com format")
        
        super().__init__(normalized_value)

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def __repr__(self):
        return f"Email({self.value})"
        
    def __str__(self):
        return self.value
