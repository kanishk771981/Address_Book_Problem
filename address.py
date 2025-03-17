
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
    """

    def __init__(self):
         """
        Initializes an empty address book with an empty dictionary to hold contacts.
        """
         self.contacts = {}

    def add_contact(self, contact_o):
        """
        Adds a contact to the address book.

        Parameters:
        -----------
        contact_o : object
            An instance of the Contact class.
        """
        print(contact_o.__dict__) 
        print(contact_o.phone_num)  
        self.contacts[contact_o.phone_num] = contact_o

        
    def print_address(self):
        """
        Prints all contacts stored in the address book.
        """
        for key,value in self.contacts.items():
            print(key,":",value)