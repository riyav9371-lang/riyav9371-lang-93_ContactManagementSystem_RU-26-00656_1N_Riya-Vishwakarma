contacts = []


def is_valid_phone(phone):
    return len(phone) == 10 and phone.isdigit()


def phone_exists(phone):
    for contact in contacts:
        if contact["phone"] == phone:
            return True
    return False


def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()

    if not is_valid_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if phone_exists(phone):
        print("Contact with this number already exists.")
        return

    email = input("Enter Email (press enter to skip): ").strip()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact)
    print("=========================Contact added successfully!============================")
    print(f"Contact added: {name} | {phone}")


def display_contacts():
    if not contacts:
        print("No contacts to display.")
        return

    print(f"\n--- Total Contacts: {len(contacts)} ---")
    for contact in contacts:
        if contact["email"]:
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
        else:
            print(f"{contact['name']} | {contact['phone']}")


def search_contact():
    search_name = input("Enter name to search: ").strip()
    found = False

    for contact in contacts:
        if search_name.lower() in contact["name"].lower():
            if contact["email"]:
                print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
            else:
                print(f"{contact['name']} | {contact['phone']}")
            found = True

    if not found:
        print(f"No contact found with name '{search_name}'.")


def update_contact():
    name_to_update = input("Enter contact name to update: ").strip()
    target_contact = None

    for contact in contacts:
        if contact["name"].lower() == name_to_update.lower():
            target_contact = contact
            break

    if not target_contact:
        print(f"Contact '{name_to_update}' not found.")
        return

    new_phone = input("Enter new phone: ").strip()

    if not is_valid_phone(new_phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    if new_phone != target_contact["phone"] and phone_exists(new_phone):
        print("Contact with this number already exists.")
        return

    target_contact["phone"] = new_phone
    print(f"Phone updated: {new_phone}")


def delete_contact():
    name_to_delete = input("Enter contact name to delete: ").strip()
    target_contact = None

    for contact in contacts:
        if contact["name"].lower() == name_to_delete.lower():
            target_contact = contact
            break

    if not target_contact:
        print(f"Contact '{name_to_delete}' not found.")
        return

    original_name = target_contact["name"]
    contacts.remove(target_contact)
    print(f"Contact '{original_name}' deleted. Total contacts: {len(contacts)}")


def main():
    while True:
        print("\n===== CONTACT MANAGEMENT SYSTEM =====")
        print("1. Add Contact")
        print("2. Display All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select between 1 and 6.")


if __name__ == "__main__":
    main()