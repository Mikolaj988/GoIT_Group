from collections import UserDict
from datetime import datetime
import re


class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):
        allowed_chars = set("0123456789+-()/. ")
        if not all(char in allowed_chars for char in self.value):
            raise ValueError("Invalid phone number format")

        digits = [char for char in self.value if char.isdigit()]
        if len(digits) != 9:
            raise ValueError("Phone number must have exactly 9 digits")


class Email(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_email()

    def validate_email(self):
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_pattern, self.value):
            raise ValueError("Invalid e-mail format")


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_birthday()

    def validate_birthday(self):
        try:
            datetime.strptime(str(self.value), '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid birthday format")


class Record:
    FIELD_CLASSES = {
        "phones": Phone,
        "emails": Email,
        "birthday": Birthday,
    }

    def __init__(self, name, birthday=None):
        if not name:
            raise ValueError("Name is required.")
        self.name = Name(name)
        self.fields = {"phones": [], "emails": [], "birthday": []}
        if birthday:
            self.add_field("birthday", birthday)

    def add_field(self, field_type, value):
        if field_type in self.fields and field_type in self.FIELD_CLASSES:
            field_class = self.FIELD_CLASSES[field_type]
            try:
                self.fields[field_type].append(field_class(value))
            except ValueError as e:
                print(f"Error adding field: {field_type}: {e}")

    def remove_field(self, field_type, value):
        if field_type in self.fields:
            self.fields[field_type] = [
                f for f in self.fields[field_type] if f.value != value]

    def edit_field(self, field_type, old_value, new_value):
        if field_type in self.fields:
            for field in self.fields[field_type]:
                if field.value == old_value:
                    field.value = new_value
                    break

    def days_to_birthday(self):
        if "birthday" in self.fields:
            today = datetime.now()

            if isinstance(self.fields["birthday"][0].value, str):
                birthday_date = datetime.strptime(
                    self.fields["birthday"][0].value, '%Y-%m-%d')
            else:
                birthday_date = self.fields["birthday"][0].value

            next_birthday = datetime(
                today.year + 1, birthday_date.month, birthday_date.day)
            days_left = (next_birthday - today).days
            return days_left if days_left > 0 else 365 + days_left


class AddressBook(UserDict):
    def add_record(self, record):
        unique_key = record.name.value
        self.data[unique_key] = record

    def search_records(self, criteria):
        matching_records = []
        for record in self.data.values():
            matches_criteria = any(
                (field == 'name' and getattr(record.name, 'value', None) and criteria[field].lower() in record.name.value.lower()) or
                (field in record.fields and (
                    (isinstance(record.fields[field], list) and any(criteria[field].lower() in f.value.lower() for f in record.fields[field] if hasattr(f, 'value'))) or
                    (not isinstance(
                        record.fields[field], list) and criteria[field].lower() in record.fields[field][0].value.lower())
                ))
                for field in criteria.keys()
            )
            if matches_criteria:
                matching_records.append(record)
        return matching_records

    def search(self, query):
        criteria = {
            "name": query,
            "phones": query,
            "emails": query,
            "birthday": query,
        }
        return self.search_records(criteria)

    def upcoming_birthdays(self, days):
        today = datetime.now()
        upcoming_birthdays_list = []

        for record in self.data.values():
            if "birthday" in record.fields:
                # Sprawdzamy dni do urodzin
                days_to_birthday = record.days_to_birthday()

                if 0 <= days_to_birthday <= days:
                    upcoming_birthdays_list.append(record)

        return upcoming_birthdays_list
