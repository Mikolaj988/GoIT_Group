import json
from address_book_aleksandra import Record, Phone


# Kule dla wyciągania numerów z listy [...] w string.
def extract_phone(phone_list):
    return ', '.join(str(Phone(number)) for number in phone_list)


def to_json(address_book, filename):
    data_to_write = {
        name: {
            'name': str(record.name),
            'phone': list(map(str, record.phone)),
            'emaile': str(record.birthday),
            'birthday': str(record.birthday) if record.birthday else None
        } for name, record in address_book.data.items()
    }
    with open(filename, 'w') as data_file:
        json.dump(data_to_write, data_file, indent=2)


def from_json(filename):
    with open(filename, 'r') as data_file:
        data = json.load(data_file)
        records = {}

        for name, record_data in data.items():
            phone_list = record_data.get('phone', [])
            phone_string = extract_phone(phone_list)
            record = Record(
                name,
                phone_string,
                record_data.get('emaile'),
                record_data.get('birthday'),
            )
            records[name] = record
    return records

if __name__ == "__main__":
