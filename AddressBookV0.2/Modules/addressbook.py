import re
from collections import UserDict
from datetime import datetime


class Contact:
    def __init__(self, name, phone=None, birthday=None, email=None):
        try:
            if not Contact.validation_name(name):
                raise ValueError(f'Error: INVALID Name format for {name}')
        except ValueError as e:
            print(e)
            self.name = None
        else:
            self.name = name
            self.phone = [phone] or []
            self.birthday = birthday
            self.email = email
            print(f'Contact {self.name} was CREATED.\n')

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
                raise ValueError(f'Error: INVALID phone number format for {phone}\n')
        except ValueError as e:
            print(e)
        else:
            self.phone.append(phone)
            print(f'Phone {phone} was ADD to contact {self.name}\n')

    def delete_phone(self, phone):
        self.phone = [i for i in self.phone if str(i) != phone]
        print(f'Phone {phone} was DELETE from contact {self.name}\n')

    def edit_phone(self, old_phone, new_phone):
        try:
            if not Contact.validation_phone(new_phone):
                raise ValueError(f'Error: INVALID phone number format for {new_phone}\n')
        except ValueError as e:
            print(e)
        else:
            for key, elem in enumerate(self.phone):
                if str(elem) == old_phone:
                    self.phone[key] = new_phone
                    print(f'Phone number "{old_phone}" has been successfully CHANGED to "{new_phone}"\n')
                    break

    def add_birthday(self, birthday):
        try:
            if not Contact.validation_birthday(birthday):
                raise ValueError(f'Error: INVALID birthday format for {birthday}\n')
        except ValueError as e:
            print(e)
        else:
            if self.birthday:
                print(f'Contact already haw birth date\n')
            else:
                self.birthday = birthday
                print(f'Birthday {birthday} has been successfully ADDED to contact {self.name}\n')

    def delete_birthday(self, birthday):
        try:
            if not Contact.validation_birthday(birthday):
                raise ValueError(f'INVALID birthday format for {birthday}\n')
        except ValueError as e:
            print(e)
        else:
            if self.birthday == birthday:
                self.birthday = None
                print(f'Birthday {birthday} was DELETED from contact {self.name}\n')
            else:
                print(f'Error: Provided birthday does NOT MATCH the contact\'s birthday\n')

    def edit_birthday(self, new_birthday):
        try:
            if not Contact.validation_birthday(new_birthday):
                raise ValueError(f'Error: INVALID birthday format for {new_birthday}\n')
        except ValueError as e:
            print(e)
        else:
            old_birthday = self.birthday
            self.birthday = new_birthday
            print(f'Birthday "{old_birthday}" has been successfully CHANGED to "{new_birthday}"\n')

    def add_email(self, email):
        try:
            if not Contact.validation_email(email):
                raise ValueError(f'Error: INVALID email format for {email}\n')
        except ValueError as e:
            print(e)
        else:
            if self.email:
                print(f'Contact already haw Email\n')
            else:
                self.email = email
                print(f'Email {email} has been successfully ADDED to contact {self.name}\n')

    def delete_email(self, email):
        try:
            if not Contact.validation_email(email):
                raise ValueError(f'INVALID email format for {email}\n')
        except ValueError as e:
            print(e)
        else:
            if self.email == email:
                self.email = None
                print(f'Email {email} was DELETED from contact {self.name}\n')
            else:
                print(f'Error: Provided Email does NOT MATCH the contact\'s Email\n')

    def edit_email(self, new_email):
        try:
            if not Contact.validation_email(new_email):
                raise ValueError(f'Error: INVALID birthday format for {new_email}\n')
        except ValueError as e:
            print(e)
        else:
            old_email = self.email
            self.email = new_email
            print(f'Birthday "{old_email}" has been successfully CHANGED to "{new_email}"\n')

    def days_to_birthday(self):
        if not self.birthday:
            return None
        else:
            today = datetime.now().date()
            day, month, year = map(int, re.findall(r'\d+', str(self.birthday)))
            next_birthday = datetime(today.year, month, day).date()

            if today > next_birthday:
                next_birthday = datetime(today.year + 1, month, day).date()

            return (next_birthday - today).days

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Phone: {", ".join(map(str, self.phone))}\n'
                f'Birthday: {self.birthday}\n'
                f'Email: {self.email}\n'
                f'Days to next Birthday left: {self.days_to_birthday()}\n')


class AddressBook:
    pass
