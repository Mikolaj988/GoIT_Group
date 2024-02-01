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

        user_input_main = input(Fore.GREEN + MESSAGES['input'] + Style.RESET_ALL).lower()

        if user_input_main in COMMAND_LIST_MAIN.keys():
            print(f'{Fore.GREEN}Execute {user_input_main}.{Style.RESET_ALL}')
            print(COMMAND_LIST_MAIN[user_input_main]())
        else:
            print(Fore.RED + MESSAGES['command_error'] + Style.RESET_ALL)


def notebook_loop():
    notebook_manu_counter = 0
    notebook = NoteBook()

    while True:

        if not notebook_manu_counter == 1:
            notebook = from_json_note('notebook.json')
            print(Fore.GREEN + MESSAGES['notebook_welcome'] + Style.RESET_ALL)
            notebook_manu_counter += 1

        print(Fore.YELLOW + MESSAGES['notebook_menu'] + Style.RESET_ALL)

        user_input_notebook = input(Fore.GREEN + MESSAGES['input'] + Style.RESET_ALL).lower()

        if user_input_notebook in COMMAND_LIST_NOTEBOOK.keys():
            if user_input_notebook in ['exit_notebook', '11'] or user_input_notebook in ['exit_program', '12']:
                to_json_note(notebook, 'notebook.json')
                if user_input_notebook in ['exit_notebook', '11']:
                    exit_notebook()
                    break
                elif user_input_notebook in ['exit_program', '12']:
                    exit_program()
            else:
                print(f'{Fore.GREEN}Execute {user_input_notebook}.{Style.RESET_ALL}')
                print(COMMAND_LIST_NOTEBOOK[user_input_notebook](???))
        else:
            print(Fore.RED + MESSAGES['command_error'] + Style.RESET_ALL)


def addressbook_loop():
    pass


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


COMMAND_LIST_MAIN = {
    'notebook': notebook_loop,
    '1': notebook_loop,
    'addressbook': addressbook_loop,
    '2': addressbook_loop,
    'help': main_help,
    '3': main_help,
    'exit': exit_program,
    '4': exit_program,
}

COMMAND_LIST_NOTEBOOK = {
    'add_note': NoteBook.add_note,
    '1': NoteBook.add_note,
    'rewrite_note': Note.rewrite_note,
    '2': Note.rewrite_note,
    'delete_note': NoteBook.delete_note,
    '3': NoteBook.delete_note,
    'search_note': NoteBook.search_note,
    '4': NoteBook.search_note,
    'add_tag': Note.add_tag,
    '5': Note.add_tag,
    'delete_tag': Note.delete_tag,
    '6': Note.delete_tag,
    'search_tag': NoteBook.search_tag,
    '7': NoteBook.search_tag,
    'sort_tag': NoteBook.sort_tag,
    '8': NoteBook.sort_tag,
    'show_all': NoteBook.show_all,
    '9': NoteBook.show_all,
    'help': notebook_help,
    '10': notebook_help,
    'exit_notebook': exit_notebook,
    '11': exit_notebook,
    'exit_program': exit_program,
    '12': exit_program,
}

if __name__ == '__main__':
    main_menu_loop()
