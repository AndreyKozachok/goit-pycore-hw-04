def add_contact(args, contacts): # Функція add_contact призначена для додавання нового контакту до словника контактів.
    try:
        if len(args) != 2:
            raise ValueError("Exactly 2 arguments (name and phone) are required.")
        name, phone = args # args, який є списком і містить ім'я та телефонний номер
        contacts[name] = phone #  який є словником, де зберігаються контакти
        return "Contact added."
    except ValueError as ve:
        return str(ve)
    except Exception as e:
        return f"Error occurred while adding contact: {type(e).__name__}, {e}"

def change_contacts(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Exactly 2 arguments (name and phone) are required.")
        name, phone = args
        if name not in contacts:
            return "Contacts does not exist"
        contacts[name] = phone
        return "Contacts updated."
    except ValueError as ve:
        return str(ve)


def show_phone(args, contacts):
    try:
        if len(args) != 1:
            raise ValueError("Exactly 1 argument (name) is required.")
        name = args[0]
        if name not in contacts:
            return "Contact does not exist"
        return contacts[name]
    except ValueError as ve:
        return str(ve)
    

def get_all_contatcs(contacts):
    if not contacts:
        return "Contacts are empty"
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output
        

    