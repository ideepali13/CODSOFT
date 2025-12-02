import json
import os

# Define the file path for persistent storage
CONTACT_FILE_PATH = "contact_book.json"

def load_contacts():
    """Loads contacts from the JSON file, or returns an empty list if the file doesn't exist."""
    if os.path.exists(CONTACT_FILE_PATH):
        try:
            with open(CONTACT_FILE_PATH, 'r') as file:
                # Load existing contacts or default to an empty list if the file is empty
                return json.load(file) or []
        except json.JSONDecodeError:
            # Handle case where file is empty or corrupted
            print("Warning: Contact file corrupted or empty. Starting with a fresh list.")
            return []
    return []

def save_contacts(contacts):
    """Saves the current list of contacts to the JSON file."""
    with open(CONTACT_FILE_PATH, 'w') as file:
        json.dump(contacts, file, indent=4)

def display_contact_list(contacts):
    """Displays a list of all saved contacts with their index, name, and phone number."""
    if not contacts:
        print("\nYour Contact Book is empty.")
        return False

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. Name: {contact['name']:<20} | Phone: {contact['phone']}")
    print("--------------------")
    return True

def add_contact(contacts):
    """Allows users to add new contacts with their details."""
    print("\n--- Add New Contact ---")
    name = input("Enter Name (required): ").strip()
    phone = input("Enter Phone Number (required): ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    if name and phone:
        new_contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        contacts.append(new_contact)
        save_contacts(contacts)
        print(f"\nContact '{name}' added successfully.")
    else:
        print("\nName and Phone Number are required. Contact not added.")

def search_contact(contacts):
    """Searches for contacts by name or phone number and displays full details."""
    if not contacts:
        print("\nContact Book is empty. Nothing to search.")
        return

    query = input("\nEnter Name or Phone Number to search: ").strip().lower()
    found_contacts = []

    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            found_contacts.append(contact)

    if not found_contacts:
        print(f"\nNo contacts found matching '{query}'.")
        return

    print(f"\n--- Search Results for '{query}' ---")
    for contact in found_contacts:
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email'] or 'N/A'}")
        print(f"Address: {contact['address'] or 'N/A'}")
    print("--------------------------------------")


def update_contact(contacts):
    """Enables users to update contact details."""
    if not display_contact_list(contacts):
        return

    try:
        index_to_update = int(input("Enter the number of the contact to update: ")) - 1
        if 0 <= index_to_update < len(contacts):
            contact = contacts[index_to_update]
            print(f"\nUpdating contact: {contact['name']}")
            print("Press Enter to keep the current value.")

            contact['name'] = input(f"New Name ({contact['name']}): ").strip() or contact['name']
            contact['phone'] = input(f"New Phone ({contact['phone']}): ").strip() or contact['phone']
            contact['email'] = input(f"New Email ({contact['email']}): ").strip() or contact['email']
            contact['address'] = input(f"New Address ({contact['address']}): ").strip() or contact['address']

            save_contacts(contacts)
            print(f"\nContact '{contact['name']}' updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact(contacts):
    """Provides an option to delete a contact."""
    if not display_contact_list(contacts):
        return

    try:
        index_to_delete = int(input("Enter the number of the contact to DELETE: ")) - 1
        if 0 <= index_to_delete < len(contacts):
            deleted_contact = contacts.pop(index_to_delete)
            save_contacts(contacts)
            print(f"\nContact '{deleted_contact['name']}' deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def contact_book_app():
    """Main application loop."""
    contacts = load_contacts()

    while True:
        print("\n" + "="*40)
        print("    **Contact Book Manager**")
        print("="*40)
        print("1. Add New Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("="*40)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            display_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nContacts saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_book_app()