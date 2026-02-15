def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, users_dict):
    if len(args) == 2:
        name, phone = args[0], args[1]
        users_dict[name] = phone
        return "Contact added."
    else:
        return "Give me name and phone"

def change_contact(args, users_dict):
    if len(args) == 2:
        name, new_phone = args[0], args[1]
        if name in users_dict:
            users_dict[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found"
    else:
        return "Give me name and phone"
def show_phone(args, users_dict):
    if len(args) !=1:
        return "Give me name"
    else:
        name = args[0]
        if name in users_dict:
            return users_dict[name]
        else:
            return "Contact not found"
def show_all(users_dict):
    if not users_dict:
        return "No contacts"
    else:
        all_users_visibility = []
        for name, phone in users_dict.items():
            joint_str = f"{name}: {phone}"
            all_users_visibility.append(joint_str)
    return "\n".join(all_users_visibility)
                  

def main():
    print("Welcome to the assistant bot!")
    users_dict = {}
    while True:
        user_input = input("Enter a command: ")
        if not user_input.split(): 
            continue
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "add":
            result_add_contact = add_contact(args, users_dict)
            print(result_add_contact)
        elif command == "change":
            result_change_cont = change_contact(args, users_dict)
            print(result_change_cont)
        elif command == "phone":
            result_show_ph = show_phone(args, users_dict)
            print(result_show_ph)
        elif command == "all":
            result_show_all = show_all(users_dict)
            print(result_show_all)

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()