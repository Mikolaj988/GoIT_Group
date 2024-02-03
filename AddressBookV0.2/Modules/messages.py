MESSAGES = {
    'maine_welcome': f'Hello, welcome to the personal assistant program.\n'
                     f'You have a NoteBook and a AddressBok at your disposal.\n'
                     f'What would you prefer to start with?',

    'notebook_welcome': f'Welcome to yours NoteBook.\n'
                        f'You can create and delete notes, add tags, and delete them.\n'
                        f'Additionally, you can sort your tags.\n'
                        f'Following commands are at your disposal:',

    'addressbook_welcome': f'Welcome to yours AddressBook.\n'
                           f'You can create and delete addressbook, add phone numbers.\n'
                           f'Also add additional information like\n'
                           f'emails and birthday date and delete them.\n'
                           f'Following commands are at your disposal:',

    'maine_menu': f'1. NoteBook\n'
                  f'2. AddressBook\n'
                  f'3. Help\n'
                  f'4. Exit',

    'notebook_menu': f'1. Add_Note\n'
                     f'2. Rewrite_Note\n'
                     f'3. Delete_Note\n'
                     f'4. Search_Note\n'
                     f'5. Add_tag\n'
                     f'6. Delete_Tag\n'
                     f'7. Search_Tag\n'
                     f'8. Sort_Tag\n'
                     f'9. Show_All\n'
                     f'10. Help\n'
                     f'11. Exit_NoteBook\n'
                     f'12. Exit_Program',

    'addressbook_menu': f'1. Add_Contact\n'
                        f'2. Edit_Contact\n'
                        f'3. Delete_Contact\n'
                        f'4. Search_Contact\n'
                        f'5. Add_Phone\n'
                        f'6. Delete_Phone\n'
                        f'7. Edit_Phone\n'
                        f'8. Add_Birthday\n'
                        f'9. Delete_Birthday\n'
                        f'10. Edit_Birthday\n'
                        f'11. Add_Email\n'
                        f'12. Delete_Email\n'
                        f'13. Edit_Email\n'
                        f'14. Display_All\n'
                        f'15. Help\n'
                        f'16. Exit_Address_Book\n'
                        f'17. Exit_Program',

    'main_help': f'Welcome to the Personal Assistant Program Help:\n'
                 f'1. NoteBook - Manage your notes.\n'
                 f'2. AddressBook - Manage your contacts and addresses.\n'
                 f'3. Help - Display this help message.\n'
                 f'4. Exit - Exit the program.\n'
                 f'To proceed, make your choice from the following commands.',

    'notebook_help': f'Welcome to the Notebook Help:\n'
                     f'1. Add_Note: Add a new note.\n'
                     f'2. Rewrite_Note: Rewrite the content of a note.\n'
                     f'3. Delete_Note: Delete a note.\n'
                     f'4. Search_Note: Search for a note by title.\n'
                     f'5. Add_Tag: Add a tag to a note.\n'
                     f'6. Delete_Tag: Delete a tag from a note.\n'
                     f'7. Search_Tag: Search for notes with a specific tag.\n'
                     f'8. Sort_Tag: Sort notes based on tags.\n'
                     f'9. Show_All: Display all notes.\n'
                     f'10. Help: Show this help message.\n'
                     f'11. Exit_Notebook: Exit the notebook.\n'
                     f'To proceed, make your choice from the following commands.',

    'addressbook_help': f'Welcome to the Address Book Help:\n'
                        f'1. Add_Contact: Add a new contact.\n'
                        f'2. Edit_Contact: Edit an existing contact.\n'
                        f'3. Delete_Contact: Delete a contact.\n'
                        f'4. Search_Contact: Search for a contact by name, phone, birthday, or email.\n'
                        f'5. Add_Phone: Add a phone number to a contact.\n'
                        f'6. Delete_Phone: Delete a phone number from a contact.\n'
                        f'7. Edit_Phone: Edit a phone number in a contact.\n'
                        f'8. Add_Birthday: Add a birthday to a contact.\n'
                        f'9. Delete_Birthday: Delete a birthday from a contact.\n'
                        f'10. Edit_Birthday: Edit a birthday in a contact.\n'
                        f'11. Add_Email: Add an email to a contact.\n'
                        f'12. Delete_Email: Delete an email from a contact.\n'
                        f'13. Edit_Email: Edit an email in a contact.\n'
                        f'14. Days_To_Birthday: Display days left to the next birthday for a contact.\n'
                        f'15. Display_All: Display all contacts.\n'
                        f'16. Help: Show this help message.\n'
                        f'17. Exit_Address_Book: Exit the address book.\n'
                        f'To proceed, make your choice from the following commands.',

    'notebook_empty': f'Correctly you have no notes.',
    'addressbook_empty': f'Correctly you have no contacts.',

    'success': f'Operation completed successful.',

    'error_command': f'Unknown command. Try again.',
    'error_not_found': f'Cannot be found.',
    'error': f'Something went wrong.\n'
             f'Please contact our support team for assistance.',

    'input_command': f'Please enter a number or command.\n'
                     f'>>> ',

    'title_add': f'Enter note title.\n'
                 f'>>> ',
    'text_add': f'Enter note text.\n'
                f'>>> ',
    'tags_add': f'Enter note tags. Use space as separator.\n'
                f'>>> ',
    'name_add': f'Enter contact name.'
                f'>>> ',
    'phone_add': f'Enter contact phone number.'
                 f'>>> ',
    'birthday_add': f'Enter contact birth date. DD.MM.YYYY'
                    f'>>> ',
    'email_add': f'Enter contact email.'
                 f'>>>',

    'title_new': f'Enter new note title.\n'
                 f'>>> ',
    'text_new': f'Enter new note text.\n'
                f'>>> ',

    'title_to_rewrite': f'Enter note title you wish to rewrite.\n'
                        f'>>> ',
    'name_to_rewrite': f'Enter name you wish to rewrite.\n'
                        f'>>> ',

    'title_to_delete': f'Enter note title to delete note.\n'
                       f'>>> ',
    'contact_to_delete': f'Enter contact name to delete contact.\n'
                         f'>>> ',

    'title_search': f'Enter note title to search.\n'
                    f'>>> ',
    'tag_search': f'Enter tag to search.\n'
                  f'>>> ',
    'pattern_search': f'Enter pattern to search.\n'
                      f'>>> ',

    'title_to_tag': f'Enter note title to add tag.\n'
                    f'>>> ',
    'name_to_add_phone': f'Enter the contact name for whom you want to add a phone number.\n'
                         f'>>> ',

    'title_to_untag': f'Enter note title to delete tag.\n'
                      f'>>> ',

    'tag_to_delete': f'Enter tag to delete.\n'
                     f'>>> ',

    'exit_program': f'Exiting the program.\n'
                    f'Have a nice day.',
    'exit_notebook': f'Exiting Notebook.',
    'exit_addressbook': f'Exiting Addressbook.',

    'save': f'Your notes have been saved.',
    'load': f'Your notes have been loaded.\n'
            f'Notes at your disposal: ',
}
