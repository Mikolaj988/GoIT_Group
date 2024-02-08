import sys
from messages import MESSAGES
from addressbook import Contact
from notebook import Note
from serialization import to_json_note, from_json_note, to_json_addressbook, from_json_addressbook
from colorama import Fore, Style, init

init()


def main_menu_loop():
    main_manu_counter = 0

    while True:

        if not main_manu_counter == 1:
            print(Fore.GREEN + MESSAGES['maine_welcome'] + Style.RESET_ALL)
            main_manu_counter += 1

        print(Fore.YELLOW + MESSAGES['maine_menu'] + Style.RESET_ALL)

        user_input_main = input(Fore.GREEN + MESSAGES['input_command'] + Style.RESET_ALL).lower()

        match user_input_main:
            case 'notebook' | '1':
                notebook_loop()
            case 'addressbook' | '2':
                addressbook_loop()
            case 'help' | '3':
                print(Fore.BLUE + MESSAGES['main_help'] + Style.RESET_ALL)
            case 'exit' | '4':
                print(exit_program())
            case _:
                print(Fore.RED + MESSAGES['error_command'] + Style.RESET_ALL)


def notebook_loop():
    notebook_manu_counter = 0

    while True:

        if not notebook_manu_counter == 1:
            notebook = from_json_note('notebook.json')
            print(Fore.GREEN + MESSAGES['notebook_welcome'] + Style.RESET_ALL)
            notebook_manu_counter += 1
            if not notebook:
                print(Fore.BLUE + MESSAGES['notebook_empty'] + Style.RESET_ALL)
            else:
                print(Fore.BLUE + MESSAGES['load'] + str(len(notebook)) + Style.RESET_ALL)

        print(Fore.YELLOW + MESSAGES['notebook_menu'] + Style.RESET_ALL)
        notebook = from_json_note('notebook.json')
        user_input_notebook = input(Fore.GREEN + MESSAGES['input_command'] + Style.RESET_ALL).lower()

        match user_input_notebook:
            case 'add_note' | '1':
                title_add = input(Fore.GREEN + MESSAGES['title_add'] + Style.RESET_ALL)
                text_add = input(Fore.GREEN + MESSAGES['text_add'] + Style.RESET_ALL)
                tags_add = input(Fore.GREEN + MESSAGES['tags_add'] + Style.RESET_ALL).split()
                note = Note(title_add, text_add, tags_add)
                print(notebook.add_note(note))
                print(note)
                to_json_note(notebook, 'notebook.json')
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
            case 'rewrite_note' | '2':
                title_to_rewrite = input(Fore.GREEN + MESSAGES['title_to_rewrite'] + Style.RESET_ALL)
                if title_to_rewrite in notebook.data:
                    note = notebook.data[title_to_rewrite]
                    title_new = input(Fore.GREEN + MESSAGES['title_new'] + Style.RESET_ALL)
                    text_new = input(Fore.GREEN + MESSAGES['text_new'] + Style.RESET_ALL)
                    print(note.rewrite_note(title_new, text_new))
                    notebook.add_note(note)
                    to_json_note(notebook, 'notebook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + title_to_rewrite + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_note' | '3':
                title_to_delete = input(Fore.GREEN + MESSAGES['title_to_delete'] + Style.RESET_ALL)
                print(notebook.delete_note(title_to_delete))
                to_json_note(notebook, 'notebook.json')
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
            case 'search_note' | '4':
                title_search = input(Fore.GREEN + MESSAGES['title_search'] + Style.RESET_ALL)
                result = notebook.search_note(title_search)
                print(result)
            case 'add_tag' | '5':
                title_to_tag = input(Fore.GREEN + MESSAGES['title_to_tag'] + Style.RESET_ALL)
                if title_to_tag in notebook.data:
                    note = notebook.data[title_to_tag]
                    tag_new = input(Fore.GREEN + MESSAGES['tags_add'] + Style.RESET_ALL).split()
                    print(note.add_tag(tag_new))
                    notebook.add_note(note)
                    to_json_note(notebook, 'notebook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + title_to_tag + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_tag' | '6':
                title_to_untag = input(Fore.GREEN + MESSAGES['title_to_untag'] + Style.RESET_ALL)
                if title_to_untag in notebook.data:
                    note = notebook.data[title_to_untag]
                    tag_to_delete = input(Fore.GREEN + MESSAGES['tag_to_delete'] + Style.RESET_ALL)
                    print(note.delete_tag(tag_to_delete))
                    notebook.add_note(note)
                    to_json_note(notebook, 'notebook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + title_to_untag + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'search_tag' | '7':
                tag_search = input(Fore.GREEN + MESSAGES['tag_search'] + Style.RESET_ALL)
                result = notebook.search_tag(tag_search)
                print(result)
            case 'sort_tag' | '8':
                result = notebook.sort_tag()
                print(result)
            case 'show_all' | '9':
                print(notebook)
            case 'help' | '10':
                print(Fore.BLUE + MESSAGES['notebook_help'] + Style.RESET_ALL)
            case 'exit_notebook' | '11':
                to_json_note(notebook, 'notebook.json')
                print(Fore.BLUE + MESSAGES['exit_notebook'] + Style.RESET_ALL)
                break
            case 'exit_program' | '12':
                to_json_note(notebook, 'notebook.json')
                print(exit_program())
            case _:
                print(Fore.RED + MESSAGES['error_command'] + Style.RESET_ALL)


def addressbook_loop():
    address_book_menu_counter = 0

    while True:
        if not address_book_menu_counter == 1:
            addressbook = from_json_addressbook('addressbook.json')
            print(Fore.GREEN + MESSAGES['addressbook_welcome'] + Style.RESET_ALL)
            address_book_menu_counter += 1
            if not addressbook:
                print(Fore.BLUE + MESSAGES['addressbook_empty'] + Style.RESET_ALL)
            else:
                print(Fore.BLUE + MESSAGES['load'] + str(len(addressbook)) + Style.RESET_ALL)

        print(Fore.YELLOW + MESSAGES['addressbook_menu'] + Style.RESET_ALL)
        addressbook = from_json_addressbook('addressbook.json')
        user_input_addressbook = input(Fore.GREEN + MESSAGES['input_command'] + Style.RESET_ALL).lower()

        match user_input_addressbook:
            case 'add_contact' | '1':
                name_add = input(Fore.GREEN + MESSAGES['name_add'] + Style.RESET_ALL)
                phone_add = input(Fore.GREEN + MESSAGES['phone_add'] + Style.RESET_ALL)
                birthday_add = input(Fore.GREEN + MESSAGES['birthday_add'] + Style.RESET_ALL)
                email_add = input(Fore.GREEN + MESSAGES['email_add'] + Style.RESET_ALL)
                contact = Contact(name_add, phone_add, birthday_add, email_add)
                if contact.name is None:
                    continue
                print(addressbook.contact_add(contact))
                print(contact)
                to_json_addressbook(addressbook, 'addressbook.json')
            case 'name_to_rewrite' | '2':
                name_to_rewrite = input(Fore.GREEN + MESSAGES['name_to_rewrite'] + Style.RESET_ALL)
                if name_to_rewrite in addressbook.data:
                    contact = addressbook.data[name_to_rewrite]
                    new_name = input(Fore.GREEN + MESSAGES['name_add'] + Style.RESET_ALL)
                    print(contact.edit_name(name_to_rewrite, new_name))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                else:
                    print(Fore.RED + name_to_rewrite + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_contact' | '3':
                name_to_delete = input(Fore.GREEN + MESSAGES['contact_to_delete'] + Style.RESET_ALL)
                print(addressbook.contact_delete(name_to_delete))
                to_json_addressbook(addressbook, 'addressbook.json')
            case 'search_contact' | '4':
                pattern_search = input(Fore.GREEN + MESSAGES['pattern_search'] + Style.RESET_ALL)
                result = addressbook.search(pattern_search)
                print(result)
            case 'add_phone' | '5':
                name_to_add_phone = input(Fore.GREEN + MESSAGES['name_to_add_phone'] + Style.RESET_ALL)
                if name_to_add_phone in addressbook.data:
                    contact = addressbook.data[name_to_add_phone]
                    new_phone = input(Fore.GREEN + MESSAGES['phone_add'] + Style.RESET_ALL)
                    print(contact.add_phone(new_phone))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                else:
                    print(Fore.RED + name_to_add_phone + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_phone' | '6':
                name_to_delete_phone = input(Fore.GREEN + MESSAGES['name_to_delete_phone'] + Style.RESET_ALL)
                if name_to_delete_phone in addressbook.data:
                    contact = addressbook.data[name_to_delete_phone]
                    phone_to_delete = input(Fore.GREEN + MESSAGES['phone_to_delete'] + Style.RESET_ALL)
                    print(contact.delete_phone(phone_to_delete))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_delete_phone + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'edit_phone' | '7':
                name_to_edit_phone = input(Fore.GREEN + MESSAGES['name_to_edit_phone'] + Style.RESET_ALL)
                if name_to_edit_phone in addressbook.data:
                    contact = addressbook.data[name_to_edit_phone]
                    if not contact.phone:
                        print(Fore.RED + MESSAGES['error_phone'] + Style.RESET_ALL)
                        continue
                    old_phone = input(Fore.GREEN + MESSAGES['old_phone'] + Style.RESET_ALL)
                    new_phone = input(Fore.GREEN + MESSAGES['new_phone'] + Style.RESET_ALL)
                    print(contact.edit_phone(old_phone, new_phone))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_edit_phone + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'add_birthday' | '8':
                name_to_add_birthday = input(Fore.GREEN + MESSAGES['name_to_add_birthday'] + Style.RESET_ALL)
                if name_to_add_birthday in addressbook.data:
                    contact = addressbook.data[name_to_add_birthday]
                    new_birthday = input(Fore.GREEN + MESSAGES['birthday_add'] + Style.RESET_ALL)
                    print(contact.add_birthday(new_birthday))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_add_birthday + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_birthday' | '9':
                name_to_delete_birthday = input(Fore.GREEN + MESSAGES['name_to_delete_birthday'] + Style.RESET_ALL)
                if name_to_delete_birthday in addressbook.data:
                    contact = addressbook.data[name_to_delete_birthday]
                    birthday_to_delete = input(Fore.GREEN + MESSAGES['birthday_to_delete'] + Style.RESET_ALL)
                    print(contact.delete_birthday(birthday_to_delete))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_delete_birthday + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'edit_birthday' | '10':
                name_to_edit_birthday = input(Fore.GREEN + MESSAGES['name_to_edit_birthday'] + Style.RESET_ALL)
                if name_to_edit_birthday in addressbook.data:
                    contact = addressbook.data[name_to_edit_birthday]
                    new_birthday = input(Fore.GREEN + MESSAGES['birthday_add'] + Style.RESET_ALL)
                    print(contact.edit_birthday(new_birthday))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_edit_birthday + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'add_email' | '11':
                name_to_add_email = input(Fore.GREEN + MESSAGES['name_to_add_email'] + Style.RESET_ALL)
                if name_to_add_email in addressbook.data:
                    contact = addressbook.data[name_to_add_email]
                    new_email = input(Fore.GREEN + MESSAGES['email_add'] + Style.RESET_ALL)
                    print(contact.add_email(new_email))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_add_email + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_email' | '12':
                name_to_delete_email = input(Fore.GREEN + MESSAGES['name_to_delete_email'] + Style.RESET_ALL)
                if name_to_delete_email in addressbook.data:
                    contact = addressbook.data[name_to_delete_email]
                    email_to_delete = input(Fore.GREEN + MESSAGES['email_to_delete'] + Style.RESET_ALL)
                    print(contact.delete_email(email_to_delete))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_delete_email + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'edit_email' | '13':
                name_to_edit_email = input(Fore.GREEN + MESSAGES['name_to_edit_email'] + Style.RESET_ALL)
                if name_to_edit_email in addressbook.data:
                    contact = addressbook.data[name_to_edit_email]
                    new_email = input(Fore.GREEN + MESSAGES['email_add'] + Style.RESET_ALL)
                    print(contact.edit_email(new_email))
                    addressbook.contact_add(contact)
                    to_json_addressbook(addressbook, 'addressbook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + name_to_edit_email + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'display_all' | '14':
                print(addressbook)
            case 'help' | '15':
                print(Fore.BLUE + MESSAGES['addressbook_help'] + Style.RESET_ALL)
            case 'exit_address_book' | '16':
                to_json_addressbook(addressbook, 'addressbook.json')
                print(Fore.BLUE + MESSAGES['exit_addressbook'] + Style.RESET_ALL)
                break
            case 'exit_program' | '17':
                to_json_addressbook(addressbook, 'addressbook.json')
                print(exit_program())
            case _:
                print(Fore.RED + MESSAGES['error_command'] + Style.RESET_ALL)


def exit_program():
    return sys.exit(Fore.RED + MESSAGES['exit_program'] + Style.RESET_ALL)


if __name__ == '__main__':
    main_menu_loop()
