from validator import validate_user_data
from contact import Contact

class AddressBook:
    """
    A class to manage a collection of contacts in an address book.

    Methods:
    add_contact(contact_o):
        Adds a contact object to the address book.
    print_address():
        Prints all the contacts in the address book.
    edit_contact():
        Edit the Existing Contact ,takes input as First Name and Last Name of user
    Delete_contact():
    Delete the Existing Contact ,takes input as First Name and Last Name of user
    contact_exists():
    find if there is any any duplicate contact exits or not

    """
    def __init__(self,name):
         """
        Initializes an empty address book with an empty dictionary to hold contacts.
        """
         self.address_book_name = name
         self.contacts = []
   
        

    def add_contact(self, contact_o):
       self.contacts.append(contact_o)

        
    def print_address(self):
        """
        Prints all contacts stored in the address book.
        """
        for contact in self.contacts:
            print(contact)

    def sort_name(self):
        """
        sort the contact alphabetically by first name

        parameters:
        self
        
        return:
        none
        """
        self.contacts.sort(key = lambda contact : contact.fname)
        print("contact in sorting format")
        for contact in self.contacts:
            print(contact)
    
    def sorting(self, key):
        """Sorts contacts based on the specified key."""
        self.contacts.sort(key=lambda con: getattr(con, key))
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
        """
        Edit the Existing Contact in the address book
        """
    
        if not self.contacts:
            print("No contacts available to edit.")
            return

        search_fname = input("Enter the first name of the person you want to edit: ").strip()
        search_lname = input("Enter the last name of the person you want to edit: ").strip()

        for contact in self.contacts:
            if contact.fname.lower() == search_fname.lower() and contact.lname.lower() == search_lname.lower():
                print(f"\nEditing Contact: {contact}")

                for field in ["fname", "lname", "city", "state", "zip_code", "address", "phone_num", "email"]:
                    while True:
                        new_value = input(f"Enter new {field} (or press Enter to keep existing): ").strip()
                        if not new_value:
                            break  

                        temp_data = {field: new_value}
                        validated_data = validate_user_data(temp_data)
                        if validated_data:  
                            setattr(contact, field, new_value)
                            break
                        else:
                            print(f"Invalid {field}, please enter a valid value.")

                print("Contact updated successfully!")
                return

        print("Contact not found.")


    def delete_contact(self):
        """
        Delete the Existing Contact in the address book
        """

        if not self.contacts:
            print("NO Contact available to delete")  
            return 
        
        search_fname = input("Enter the first name of the person you want to Delete: ").strip()
        search_lname = input("Enter the last name of the person you want to Delete: ").strip()

        for contact in self.contacts:
            
            if contact.fname .lower() == search_fname.lower() and contact.lname.lower() == search_lname.lower():
                self.contacts.remove(contact)
                print(f" {search_fname} {search_lname }Contact is deleted ")
                return
            
            else:
                print("Contact not found")
                return
    
    def contact_exists(self,fname,lname):
        for contact in self.contacts:
            if contact.fname.lower() == fname.lower() and contact.lname.lower() == lname.lower():
                return True
        












        



   

            
                        

            

                
            
    










        



   

            
                        

            

                
            
    
