import re
from collections import UserDict
from datetime import datetime


class Contact:
    def __init__(self, name, phone=None, birthday=None, email=None):
        try:
            if not Contact.validation_name(name):
                raise ValueError(f'Error: Invalid Name format for {name}')
        except ValueError as e:
            print(e)
            self.name = None
        else:
            self.name = name
            self.phone = phone or []
            self.birthday = birthday
            self.email = email

    @staticmethod
    def validation_name(name):
        return bool(re.match(
            r'^[A-Za-z]+\s[A-Za-z]+$',
            name))

    @staticmethod
    def validation_phone(phone):
        return bool(re.match(
            r'\d{10}',
            phone))

    @staticmethod
    def validation_birthday(birthday):
        return bool(re.match(
            r'^(0[1-9]|[12][0-9]|3[01])\.'
            r'(0[1-9]|1[0-2])\.'
            r'(19[4-9][0-9]|200[0-9]|201[0-9]|202[0-4])$',
            birthday))

    @staticmethod
    def validation_email(email):
        return bool(re.match(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            email))

    def add_phone(self, phone):
        try:
            if not Contact.validation_phone(phone):
                raise ValueError(f'Error: Invalid phone number format for {phone}\n')
        except ValueError as e:
            print(e)
        else:
            self.phone.append(phone)

    def delete_phone(self, phone):
        self.phone = [i for i in self.phone if str(i) != phone]

    def edit_phone(self, old_phone, new_phone):
        try:
            if not Contact.validation_phone(new_phone):
                raise ValueError(f'Error: Invalid phone number format for {new_phone}\n')
        except ValueError as e:
            print(e)
        else:
            for key, elem in enumerate(self.phone):
                if str(elem) == old_phone:
                    self.phone[key] = new_phone
                    break

    def add_birthday(self, birthday):
        try:
            if not Contact.validation_birthday(birthday):
                raise ValueError(f'Error: Invalid birthday format for {birthday}\n')
        except ValueError as e:
            print(e)
        else:
            self.birthday = birthday

    def delete_birthday(self, birthday):
        pass

    def edit_birthday(self, old_birthday, new_birthday):
        pass

    def add_email(self, email):
        try:
            if not Contact.validation_email(email):
                raise ValueError(f'Error: Invalid email format for {email}\n')
        except ValueError as e:
            print(e)
        else:
            self.email = email

    def delete_email(self, email):
        pass

    def edit_email(self, old_email, new_email):
        pass


    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Phone: {", ".join(map(str, self.phone))}\n'
                f'Birthday: {self.birthday}\n'
                f'Days to next Birthday left: {''}\n')

class AddressBook:
    pass
