from collections import UserDict
from datetime import datetime, timedelta
import pickle
class Field:
    def wczytywacz(self, name):
        with open(name, "rb") as file:
            value = pickle.load(file)
            return value
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __repr__(self):
        return str(self.value)

class First_Name(Field):
    pass

class Last_Name(Field):
    pass

class E_Mail(Field):
    pass

class Phonee(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str) :
            raise ValueError("Numer telefonu musi być liczbą")
        self._value = new_value
class Birthday (Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, datetime):
            raise ValueError("Wartość musi być obiektem datetime")
        self._value = new_value

class Record:

    def __init__(self, first_name, last_name, e_mail=None, phonee=None,birthday=None):
        self.first_name = First_Name(first_name)
        self.last_name = Last_Name(last_name)
        self.e_mail = E_Mail(e_mail) if e_mail else None
        self.phonee = [Phonee(namber) for namber in phonee] if phonee else None
        self.birthday=Birthday(datetime.strptime(birthday, "%d.%m.%Y")) if birthday else None

    def Add_phone(self, phone):
        self.Phonese = [Phonee(phone)] if phone else None
    def remove_phone(self, phone):
        if self.Phonee in phone:
            self.Phonee.remove(phone)
    def show_phone(self,phone):
        if phone in self.Phonee:
            print(f"{phone}")
    def days_to_birthday(self):
        if self.birthday:
            urodziny=self.birthday.value
            dat = datetime.now()
            wiek = dat.year - urodziny.year
            nzw = urodziny + timedelta(wiek * 365.25)
            if dat<=nzw:
                dni = (nzw - dat).days
                return (f"Pozostało do następnych urodzin: {dni} dni i są to {wiek} urodziny")
        return f"Urodsziny Już się odbyły"

    def __repr__(self):
        if self.first_name.value and self.last_name.value:
            repr_string = f" Nazwisko: {self.last_name}"
            if self.e_mail:
                repr_string += f", E-mail: {self.e_mail}"
            if self.phonee:
                repr_string += f", Telefon: {', '.join(map(str, self.phonee))},"
            if self.birthday:
                repr_string += f" {self.days_to_birthday()} "
            return repr_string
        else:
            return f",Nazwisko:{self.last_name}\n"
    def wyszukiwacz(self):
        if key in self.last_name or (self.phonee and key in self.phonee):
            return repr_string
        else:
            return f"Kontakt nie znaleziony"
class Iterable():
    def __init__(self, stron=1):
        self.l_stron=0
        self.AdressBook={}
        self.strona=stron
    def __next__(self):
        if self.l_stron<len(self.AdressBook):
            self.l_stron+=1
            return self.adressBook
        raise StopIteration
class Inter:
    def __init__(self,stron=1):
        self.stron=stron
    def __iter__(self):
        return Iterable(self.stron)
i = Inter()
for char in i:
        print(char)
class AdressBook(UserDict,Iterable):
    def wczytywacz(self, data):
        with open(self.data, "rb") as file:
            value = pickle.load(file)
            return value
    def add_record(self, record: Record):
        key = record.first_name.value
        if key not in self.data:
            self.data[key] = []
        self.data[key].append(record)

    def zapisywacz(self, data):
        with open(self.data, "wb") as file:
            pickle.dump(data, file)


def main():
    record_1 = Record(
        first_name="Paweł",
        last_name="Pierwszy",
        e_mail="rrr.sssss@gmail.com",
        phonee=["+7376382327"],
        birthday="12.12.1994"
    )
    record_2 = Record(
        first_name="Adam",
        last_name="Zakolski"

    )

    address_book = AdressBook()
    address_book.add_record(record_1)
    address_book.add_record(record_2)

    print(address_book)

if __name__ == "__main__":
    main()
