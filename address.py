from validator import validate_user_data
from contact import Contact
import os
import json

class AddressBook:
    """
    A class to manage a collection of contacts in an address book using JSON storage.
    """
    
    def __init__(self, name):
        """
        Initializes an empty address book with a name and JSON file.
        """
        self.address_book_name = name
        self.contacts = []
        self.file_path = f'data/json/{self.address_book_name}.json'

        if not os.path.exists(os.path.dirname(self.file_path)):
            os.makedirs(os.path.dirname(self.file_path))

        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)
        
        self.load_contacts()

    def add_contact(self, contact_o):
        """
        Adds a contact if it doesn't already exist.
        """
        if self.contact_exists(contact_o.fname, contact_o.lname):
            print("Duplicate contact exists. Cannot add.")
            return

        self.contacts.append(contact_o)
        self.save_contacts()
        print("Contact added successfully.")

    def print_address(self):
        """Prints all contacts in the address book."""
        for contact in self.contacts:
            print(contact)

    def sort_name(self):
        """Sorts contacts alphabetically by first name."""
        self.contacts.sort(key=lambda contact: contact.fname)
        print("Contacts sorted alphabetically:")
        self.print_address()

    def sorting(self, key):
        """Sorts contacts by a specified key."""
        self.contacts.sort(key=lambda con: getattr(con, key, ""))
        return self.contacts

    def loc_sort(self, location):
        """Sorts contacts based on city, state, or zip code and displays the sorted list."""
        location = location.strip().lower()
        valid_keys = {"city", "state", "zip_code"}

        if location in valid_keys:
            self.sorting(location)
            print(f"\nContacts sorted by {location}:\n")
            self.print_address()
        else:
            print("Invalid choice. Please enter 'city', 'state', or 'zip_code'.")

    def edit_contact(self):
        """Edits an existing contact."""
        if not self.contacts:
            print("No contacts available to edit.")
            return

        search_fname = input("Enter the first name: ").strip()
        search_lname = input("Enter the last name: ").strip()

        for contact in self.contacts:
            if contact.fname.lower() == search_fname.lower() and contact.lname.lower() == search_lname.lower():
                print(f"\nEditing Contact: {contact}")

                for field in ["fname", "lname", "city", "state", "zip_code", "address", "phone_num", "email"]:
                    new_value = input(f"Enter new {field} (or press Enter to keep existing): ").strip()
                    if new_value:
                        temp_data = {field: new_value}
                        validated_data = validate_user_data(temp_data)
                        if validated_data:
                            setattr(contact, field, new_value)
                        else:
                            print(f"Invalid {field}. Please try again.")

                print("Contact updated successfully!")
                self.save_contacts()
                return

        print("Contact not found.")

    def delete_contact(self):
        """Deletes an existing contact."""
        if not self.contacts:
            print("No contacts available to delete.")
            return

        search_fname = input("Enter the first name: ").strip()
        search_lname = input("Enter the last name: ").strip()

        for i, contact in enumerate(self.contacts):
            if contact.fname.lower() == search_fname.lower() and contact.lname.lower() == search_lname.lower():
                del self.contacts[i]
                print(f"{search_fname} {search_lname} has been deleted.")
                self.save_contacts()
                return

        print("Contact not found.")

    def contact_exists(self, fname, lname):
        """Checks if a contact already exists."""
        return any(contact.fname.lower() == fname.lower() and contact.lname.lower() == lname.lower() for contact in self.contacts)

    def load_contacts(self):
        """Loads contacts from the JSON file."""
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact(**contact) for contact in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("No previous contacts found, starting fresh.")

    def save_contacts(self):
        """Saves contacts to the JSON file."""
        with open(self.file_path, 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file, indent=4)






        












        



   

            
                        

            

                
            
    










        



   

            
                        

            

                
            
    
