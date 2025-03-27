import re
from src.models.contact.field import Field


class Phone(Field):
    def __init__(self, value):
        cleaned_value = self._clean_phone_number(value)
        
        if not self._is_valid_phone(cleaned_value):
            raise ValueError("Invalid phone number format. Use +XXXXXXXXXXXX or XXXXXXXXXX format")
        
        super().__init__(cleaned_value)

    @staticmethod
    def _clean_phone_number(phone):
        if phone.startswith('+'):
            return '+' + re.sub(r'\D', '', phone[1:])
        return re.sub(r'\D', '', phone)
    
    @staticmethod
    def _is_valid_phone(phone):
        if phone.startswith('+'):
            return len(phone) >= 8 and len(phone) <= 15 and phone[1:].isdigit()
        
        return len(phone) >= 7 and len(phone) <= 13 and phone.isdigit()

    def __repr__(self):
        return f"Phone({self.value})"
        
    def __str__(self):
        return self.value
