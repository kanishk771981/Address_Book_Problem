from address import AddressBook

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
        """Retrieves an address book by name."""
        return self.address_books.get(address_book_name)



