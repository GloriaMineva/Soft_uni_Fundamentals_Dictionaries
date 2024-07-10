phonebook = {}
while True:
    contact = input()
    if '-' in contact:
        contact = contact.split('-')
        name, phone = contact
        phonebook[name] = phone
    else:
        contacts_to_search = int(contact)
        break
for i in range(contacts_to_search):
    searched_name = input()
    if searched_name in phonebook:
        print(f'{searched_name} -> {phonebook[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
