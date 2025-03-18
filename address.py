
class AddressBook:
    """
    A class to manage a collection of contacts in an address book.

    Attributes:
    contacts : dict
        A dictionary to store contact objects with phone numbers as keys.

    Methods:
    add_contact(contact_o):
        Adds a contact object to the address book.

    print_address():
        Prints all the contacts in the address book.

    edit_contact():
        Edit the Existing Contact ,takes input as First Name and Last Name of user

    Delete_contact():

    Delete the Existing Contact ,takes input as First Name and Last Name of user

    """

    def __init__(self):
         """
        Initializes an empty address book with an empty dictionary to hold contacts.
        """
         self.contacts = []

    def add_contact(self, contact_o):
       self.contacts.append(contact_o)

        
    def print_address(self):
        """
        Prints all contacts stored in the address book.
        """
        for contact in self.contacts:
            print(contact)

    def edit_contact(self):
        """
        Edit the Existing Contact in the address book
        """
    
        if not self.contacts:
            print("No contacts available to edit.")
            return

        
        for contact in self.contacts:
            print(contact)

        search_fname = input("Enter the first name of the person you want to edit: ").strip()
        search_lname = input("Enter the last name of the person you want to edit: ").strip()

        for contact in self.contacts:
            if contact.fname.lower() == search_fname.lower() and contact.lname.lower() == search_lname.lower():
                print(f"\nEditing Contact: {contact}")
                
            

                for field in ["fname", "lname", "city", "state", "zip_code", "address", "phone_num", "email"]:
                    new_value = input(f"Enter new {field} (or press Enter to keep existing): ").strip()
                    if new_value:
                        setattr(contact, field, new_value)

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











        



   

            
                        

            

                
            
    
