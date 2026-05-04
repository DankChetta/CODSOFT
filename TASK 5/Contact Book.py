contact = {}
def add_contact(name, number):
    contact[name] = number
    print("Contact added successfully")

def view_contacts():
    if not contact:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, number in contact.items():
            print(f"Name: {name}, Number: {number}")

def search_contact(name):
    if name in contact:
        print(f"Name: {name}, Number: {contact[name]}")
    else:
        print("Contact not found.")

def update_contact(name, number):
    if name in contact:
        contact[name] = number
        print("Contact updated successfully")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contact:
        del contact[name]
        print("Contact deleted successfully")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        if len(number) != 10 or not number.isdigit():
            print("Invalid number. Please enter a 10-digit number.")
        else:
            add_contact(name, number)
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == 4:
        name = input("Enter contact name to update: ")
        number = input("Enter new contact number: ")
        if len(number) != 10 or not number.isdigit():
            print("Invalid number. Please enter a 10-digit number.")
        else:
            update_contact(name, number)
    elif choice == 5:
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")