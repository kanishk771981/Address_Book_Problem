from contact import Contact
from address import AddressBook
from validator import validate_user_data


def main():
     """
     Main function to handle user input, validate data, and manage the address book.

    The function prompts the user for contact details, validates them, creates a Contact object,
    adds it to an AddressBook, and prints the address book's contents.
     """
     user_data = {
        "fname": input("Enter First Name: "),
        "lname": input("Enter Last Name: "),
        "city": input("Enter City: "),
        "state": input("Enter State: "),
        "zip_code": input("Enter Zip Code: "),
        "address": input("Enter Address: "),
        "phone_num": input("Enter Phone Number: "),
        "email": input("Enter Email: ")
    }
     if validate_user_data(user_data):
        contact = Contact(**user_data)
        address_book = AddressBook()
        address_book.add_contact(contact)
        address_book.print_address()

if __name__ == "__main__":
    main()


   
   
    

