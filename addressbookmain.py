from address import AddressBook
from contact import Contact

class AddressBookMain:
    """
    Manages multiple address books.
    """
    def __init__(self):  
        """Constructor to initialize address books dictionary."""
        self.address_books = {}
        


    def add_address_book_to_main(self, name):
        """Adds a new address book if it doesn't already exist."""
        if name in self.address_books.keys():
            print('Address Book with this name already exists.')
        else:
            address_book = AddressBook(name)
            self.address_books[name] = address_book
            return address_book

    def get_address_book_from_main(self, address_book_name):
        """find an address book by name."""
        return self.address_books.get(address_book_name)
    
 


class AddressBookMainSearch(AddressBookMain):
    """
    class for search contact by city and state
    it has function()
    search_person_City():
    search contact by City

    search_person_state():
    search contact by state
    """

    def __init__(self, main_add_obj,city,state):
        self.address_books = main_add_obj.address_books
        self.city = city
        self.state = state
        self.city_dict = {}
        self.state_dict = {}


    def search_person_city(self):
        """
        stores the person information by searching by city in state"""
        find_it = False
        self.city_dict[self.city] = [] 

        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                if self.city.lower() == contact.city.lower():
                    print(f"Contact found in {address_book.address_book_name}")
                    self.city_dict[self.city].append(vars(contact)) 
                    find_it = True

        if not find_it:
            print("Contact not found.")
        else:
            print(f"Contacts found in {self.city}: {self.city_dict[self.city]}")
       
        
    def search_person_state(self):
        """Searches for contacts by state."""
        find_it = False
        self.state_dict[self.state] = []  

        for address_book in self.address_books.values():
            for contact in address_book.contacts:
                if self.state.lower() == contact.state.lower():
                    print(f"Contact found in {address_book.address_book_name}")
                    self.state_dict[self.state].append(vars(contact))  
                    find_it = True

        if not find_it:
            print("Contact not found.")
        else:
            print(f"Contacts found in {self.state}: {self.state_dict[self.state]}")
        



        


   
    
        



