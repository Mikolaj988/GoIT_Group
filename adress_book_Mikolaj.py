from collections import UserDict
from datetime import datetime, timedelta
import pickle
import re


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __repr__(self):
        return self.value


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not str(new_value).isdigit():
            raise ValueError("Numer telefonu musi być liczbą")
        self._value = new_value


class Mail(Field):
    pass


class Birthday(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, datetime):
            raise ValueError("Data urodzenia musi być typu datetime")
        self._value = new_value


class Record:
    def __init__(self, name, phone=None, mail=None, birthday=None):
        self.name = Name(name)
        self.phones = [Phone(phone)] if phone else []
        self.mails = [Mail(mail)] if mail else []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [
            phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_phone_number, new_phone_number):
        for phone in self.phones:
            if phone.value == old_phone_number:
                phone.value = new_phone_number

    def add_mail(self, mail_address):
        self.mails.append(Mail(mail_address))

    def remove_mail(self, mail_address):
        self.mails = [
            mail for mail in self.mails if mail.value != mail_address]

    def edit_mail(self, old_mail_address, new_mail_address):
        for mail in self.mails:
            if mail.value == old_mail_address:
                mail.value = new_mail_address

    def days_to_birthday(self):
        if self.birthday:
            now = datetime.now()
            next_birthday = datetime(
                now.year, self.birthday.value.month, self.birthday.value.day)
            if now > next_birthday:
                next_birthday = datetime(
                    now.year + 1, self.birthday.value.month, self.birthday.value.day)
            return (next_birthday - now).days
        else:
            return None

    def __str__(self):
        phones = "\n".join([str(phone.value) for phone in self.phones])
        mails = "\n".join([str(mail.value) for mail in self.mails])
        return f"Imię: {self.name.value}\nNumery telefoniczne:\n{phones}\nAdres mailowy: {mails}"


class AddressBook(UserDict):
    def __init__(self, page_size=1):
        super().__init__()
        self.page_size = page_size

    def add_record(self, name, record: Record):
        self.data[record.name.value] = record

    def __iter__(self):
        self.index = 0
        self.keys = list(self.data.keys())
        return self

    def __next__(self):
        if self.index < len(self.keys):
            result = [self.data[self.keys[i]] for i in range(
                self.index, min(self.index + self.page_size, len(self.keys)))]
            self.index += self.page_size
            return result
        else:
            raise StopIteration

    def __str__(self):
        records = "\n\n".join([str(record) for record in self.data.values()])
        return f"\n{records}"

    def save_to_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.data, file)
        except Exception as e:
            print(f"Błąd podczas zapisywania do pliku: {e}")

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = pickle.load(file)
        except Exception as e:
            print(f"Błąd ładowania z pliku: {e}")

    def search(self, query):
        if len(query) < 3:
            print("Zapytanie musi mieć co najmniej trzy znaki")
            return []
        results = []
        for record in self.data.values():
            if re.search(query, record.name.value, re.I):
                results.append(record)
            else:
                for phone in record.phones:
                    if re.search(query, str(phone.value), re.I):
                        results.append(record)
                        break
        return results


if __name__ == "__main__":
    address_book = AddressBook(page_size=2)

    record_1 = Record('Olek', mail="olek@example.com",
                      birthday=datetime(1990, 5, 15))
    address_book.add_record(record_1.name.value, record_1)

    record_2 = Record('Tomek', mail="tomek@example.com")
    record_2.add_phone('73473645')
    address_book.add_record(record_2.name.value, record_2)

    record_3 = Record('Ania', mail="ania@example.com",
                      birthday=datetime(1992, 8, 30))
    record_3.add_phone('123456789')
    address_book.add_record(record_3.name.value, record_3)

    record_4 = Record('Piotr', mail="piotr@example.com",
                      birthday=datetime(1988, 9, 15))
    record_4.add_phone('987654321')
    address_book.add_record(record_4.name.value, record_4)

    record_5 = Record('Kasia', mail="kasia@example.com",
                      birthday=datetime(1993, 12, 20))
    record_5.add_phone('741852963')
    address_book.add_record(record_5.name.value, record_5)

    record_5.name.value = "Tereza"

    # for records in address_book:
    #     for record in records:
    #         print(record)
    #         print(f"Urodziny przez {record.days_to_birthday()} dni")

    # print(record_5.birthday.value)
    # print(record_5.phones[0])

    address_book.save_to_file('address_book.pkl')

    address_book.load_from_file('address_book.pkl')

    # Sprawdzanie, czy dane zostały poprawnie załadowane
    # print(address_book)

    print("Wyszukiwanie po imieniu 'Tomek':")
    for record in address_book.search('Tom'):
        print(record)

    print("Wyszukiwanie według numeru '987654321':")
    for record in address_book.search('987'):
        print(record)

    print("Wyszukiwanie po imieniu Tomek, wprowadzając tylko dwie litery 'To':")
    for record in address_book.search('To'):
        print(record)
