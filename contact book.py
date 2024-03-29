def add_contact(contacts, name, number):
    contacts[name] = number
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")

def search_contact(contacts, name):
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(contacts, name, new_number):
    if name in contacts:
        contacts[name] = new_number
        print(f"Contact '{name}' updated successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    contacts = {}

    while True:
        print("\n---- Contact Book ----")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("\nEnter name: ")
            number = input("Enter number: ")
            add_contact(contacts, name, number)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            name = input("\nEnter name to search: ")
            search_contact(contacts, name)

        elif choice == "4":
            name = input("\nEnter name to update: ")
            new_number = input("Enter new number: ")
            update_contact(contacts, name, new_number)

        elif choice == "5":
            name = input("\nEnter name to delete: ")
            delete_contact(contacts, name)

        elif choice == "6":
            break

        else:
            print("Invalid choice! Please try again.")

    print("\nGoodbye!")

if __name__ == "__main__":
    main()
