from collections import UserDict
from datetime import datetime


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
    pass


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
            self.fields[field_type].append(field_class(value))

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

            # Modyfikacja: Sprawdzamy typ daty urodzenia
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


if __name__ == "__main__":
    address_book = AddressBook()

    record1 = Record(name="Jan Kowalski", birthday="1990-05-15")
    record1.add_field("phones", "123-456-780")
    record1.add_field("emails", "jan.kowalski@gmail.com")

    record2 = Record(name="Zofia Nowak", birthday="1985-01-02")
    record2.add_field("phones", "987-654-320")
    record2.add_field("emails", "zofia.nowak@gmail.com")

    address_book.add_record(record1)
    address_book.add_record(record2)

    search_query = "jan"
    my_data = address_book.search(search_query)

    print(f"\nSearch results for:\"{search_query}\":")
    for result in my_data:
        print(f"Name: {result.name.value}")
        print(f"Birthday: {result.fields['birthday'][0].value}")

        for phone in result.fields['phones']:
            print(f"Phone: {phone.value}")

        for email in result.fields['emails']:
            print(f"Email: {email.value}")

        days_to_birthday = result.days_to_birthday()
        if days_to_birthday is not None:
            print(f"Days to Birthday: {days_to_birthday}")

        print("-" * 20)

        upcoming_birthdays_list = address_book.upcoming_birthdays(days=30)
        print("\nContacts with upcoming birthdays (within 30 days):")
        for record in upcoming_birthdays_list:
            print(
                f"Name: {record.name.value}, Birthday: {record.fields['birthday'][0].value}")
