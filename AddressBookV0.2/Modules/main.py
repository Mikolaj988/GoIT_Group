import sys
from messages import MESSAGES
from addressbook import Contact, AddressBook
from notebook import Note, NoteBook
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
                print(main_help())
            case 'exit' | '4':
                exit_program()
            case _:
                print(Fore.RED + MESSAGES['error_command'] + Style.RESET_ALL)


def notebook_loop():
    notebook_manu_counter = 0
    notebook = NoteBook()

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

        user_input_notebook = input(Fore.GREEN + MESSAGES['input_command'] + Style.RESET_ALL).lower()

        match user_input_notebook:
            case 'add_note' | '1':
                title_add = input(Fore.GREEN + MESSAGES['title_add'] + Style.RESET_ALL)
                text_add = input(Fore.GREEN + MESSAGES['text_add'] + Style.RESET_ALL)
                # tags_add = input(Fore.GREEN + MESSAGES['tags_add'] + Style.RESET_ALL).split()
                # dodaje listę. problem z __init__!?
                note = Note(title_add, text_add)
                notebook.add_note(note)
                print(note)
                to_json_note(notebook, 'notebook.json')
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
            case 'rewrite_note' | '2':
                title_to_rewrite = input(Fore.GREEN + MESSAGES['title_to_rewrite'] + Style.RESET_ALL)
                if title_to_rewrite in notebook.data:
                    note = notebook.data[title_to_rewrite]
                    title_new = input(Fore.GREEN + MESSAGES['title_new'] + Style.RESET_ALL)
                    text_new = input(Fore.GREEN + MESSAGES['text_new'] + Style.RESET_ALL)
                    note.rewrite_note(title_new, text_new)
                    to_json_note(notebook, 'notebook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + title_to_rewrite + MESSAGES['error_not_found'] + Style.RESET_ALL)
            case 'delete_note' | '3':
                title_to_delete = input(Fore.GREEN + MESSAGES['title_to_delete'] + Style.RESET_ALL)
                notebook.delete_note(title_to_delete)
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
                    note.add_tag(tag_new)
                    to_json_note(notebook, 'notebook.json')
                    print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + title_to_tag + MESSAGES['error_not_found'] + Style.RESET_ALL)

            # case 'delete_tag' | '6':
            #     title_to_untag = input(Fore.GREEN + MESSAGES['title_to_untag'] + Style.RESET_ALL)
            #     tag_to_delete = input(Fore.GREEN + MESSAGES['tag_to_delete'] + Style.RESET_ALL)
            #     notebook.delete_tag(title_to_untag, tag_to_delete)
            #     print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)

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
                print(notebook_help())
            case 'exit_notebook' | '11':
                to_json_note(notebook, 'notebook.json')
                exit_notebook()
                break
            case 'exit_program' | '12':
                to_json_note(notebook, 'notebook.json')
                exit_program()
            case _:
                print(Fore.RED + MESSAGES['error_command'] + Style.RESET_ALL)


def addressbook_loop():
    address_book_menu_counter = 0
    addressbook = AddressBook()

    while True:
        if not address_book_menu_counter == 1:
            addressbook = from_json_addressbook('address_book.json')
            print(Fore.GREEN + MESSAGES['addressbook_welcome'] + Style.RESET_ALL)
            address_book_menu_counter += 1
            if not addressbook:
                print(Fore.BLUE + MESSAGES['addressbook_empty'] + Style.RESET_ALL)
            else:
                print(Fore.BLUE + MESSAGES['load'] + str(len(addressbook)) + Style.RESET_ALL)

        print(Fore.YELLOW + MESSAGES['addressbook_menu'] + Style.RESET_ALL)

        user_input_addressbook = input(Fore.GREEN + MESSAGES['input_command'] + Style.RESET_ALL).lower()

        match user_input_addressbook:
            case 'add_contact' | '1':
                name_add = input(Fore.GREEN + MESSAGES['name_add'] + Style.RESET_ALL)
                phone_add = input(Fore.GREEN + MESSAGES['phone_add'] + Style.RESET_ALL)
                birthday_add = input(Fore.GREEN + MESSAGES['birthday_add'] + Style.RESET_ALL)
                email_add = input(Fore.GREEN + MESSAGES['email_add'] + Style.RESET_ALL)
                contact = Contact(name_add, phone_add, birthday_add, email_add)
                addressbook.contact_add(contact)
                print(contact)
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
            case 'edit_contact' | '2':
                name_to_rewrite = input(Fore.GREEN + MESSAGES['name_to_rewrite'] + Style.RESET_ALL)
                new_name = input(Fore.GREEN + MESSAGES['name_add'] + Style.RESET_ALL)
                addressbook.edit_contact(name_to_rewrite, new_name)
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
            case 'delete_contact' | '3':
                name_to_delete = input(Fore.GREEN + MESSAGES['contact_to_delete'] + Style.RESET_ALL)
                addressbook.contact_delete(name_to_delete)
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
            case 'search_contact' | '4':
                pattern_search = input(Fore.GREEN + MESSAGES['pattern_search'] + Style.RESET_ALL)
                result = addressbook.search(pattern_search)
                print(result)
            case 'add_phone' | '5':
                name_to_add_phone = input(Fore.GREEN + MESSAGES['name_to_add_phone'] + Style.RESET_ALL)
                new_phone = input(Fore.GREEN + MESSAGES['phone_add'] + Style.RESET_ALL)
                addressbook.add_phone(name_to_add_phone, new_phone)
                print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'delete_phone' | '6':
        #         name_to_delete_phone = input(Fore.GREEN + MESSAGES['name_to_delete_phone'] + Style.RESET_ALL)
        #         phone_to_delete = input(Fore.GREEN + MESSAGES['phone_to_delete'] + Style.RESET_ALL)
        #         address_book.delete_phone(name_to_delete_phone, phone_to_delete)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'edit_phone' | '7':
        #         name_to_edit_phone = input(Fore.GREEN + MESSAGES['name_to_edit_phone'] + Style.RESET_ALL)
        #         old_phone = input(Fore.GREEN + MESSAGES['old_phone'] + Style.RESET_ALL)
        #         new_phone = input(Fore.GREEN + MESSAGES['new_phone'] + Style.RESET_ALL)
        #         address_book.edit_phone(name_to_edit_phone, old_phone, new_phone)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'add_birthday' | '8':
        #         name_to_add_birthday = input(Fore.GREEN + MESSAGES['name_to_add_birthday'] + Style.RESET_ALL)
        #         new_birthday = input(Fore.GREEN + MESSAGES['new_birthday'] + Style.RESET_ALL)
        #         address_book.add_birthday(name_to_add_birthday, new_birthday)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'delete_birthday' | '9':
        #         name_to_delete_birthday = input(Fore.GREEN + MESSAGES['name_to_delete_birthday'] + Style.RESET_ALL)
        #         birthday_to_delete = input(Fore.GREEN + MESSAGES['birthday_to_delete'] + Style.RESET_ALL)
        #         address_book.delete_birthday(name_to_delete_birthday, birthday_to_delete)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'edit_birthday' | '10':
        #         name_to_edit_birthday = input(Fore.GREEN + MESSAGES['name_to_edit_birthday'] + Style.RESET_ALL)
        #         new_birthday = input(Fore.GREEN + MESSAGES['new_birthday'] + Style.RESET_ALL)
        #         address_book.edit_birthday(name_to_edit_birthday, new_birthday)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'add_email' | '11':
        #         name_to_add_email = input(Fore.GREEN + MESSAGES['name_to_add_email'] + Style.RESET_ALL)
        #         new_email = input(Fore.GREEN + MESSAGES['new_email'] + Style.RESET_ALL)
        #         address_book.add_email(name_to_add_email, new_email)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'delete_email' | '12':
        #         name_to_delete_email = input(Fore.GREEN + MESSAGES['name_to_delete_email'] + Style.RESET_ALL)
        #         email_to_delete = input(Fore.GREEN + MESSAGES['email_to_delete'] + Style.RESET_ALL)
        #         address_book.delete_email(name_to_delete_email, email_to_delete)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'edit_email' | '13':
        #         name_to_edit_email = input(Fore.GREEN + MESSAGES['name_to_edit_email'] + Style.RESET_ALL)
        #         new_email = input(Fore.GREEN + MESSAGES['new_email'] + Style.RESET_ALL)
        #         address_book.edit_email(name_to_edit_email, new_email)
        #         print(Fore.BLUE + MESSAGES['success'] + Style.RESET_ALL)
        #     case 'days_to_birthday' | '14':
        #         name_to_check_birthday = input(Fore.GREEN + MESSAGES['name_to_check_birthday'] + Style.RESET_ALL)
        #         result = address_book.days_to_birthday(name_to_check_birthday)
        #         print(result)
        #     case 'display_all' | '15':
        #         print(address_book)
        #     case 'help' | '16':
        #         print(address_book_help())
        #     case 'exit_address_book' | '17':
        #         to_json_address_book(address_book, 'address_book.json')
        #         exit_address_book()
        #         break
        #     case 'exit_program' | '18':
        #         to_json_address_book(address_book, 'address_book.json')
        #         exit_program()
        #     case _:
        #         print(Fore.RED + MESSAGES['command_error'] + Style.RESET_ALL)


def main_help():
    return Fore.BLUE + MESSAGES['main_help'] + Style.RESET_ALL


def notebook_help():
    return Fore.BLUE + MESSAGES['notebook_help'] + Style.RESET_ALL


def exit_program():
    return sys.exit(Fore.RED + MESSAGES['exit_program'] + Style.RESET_ALL)


def exit_notebook():
    return Fore.BLUE + MESSAGES['exit_notebook'] + Style.RESET_ALL


def exit_addressbook():
    pass


if __name__ == '__main__':
    main_menu_loop()
