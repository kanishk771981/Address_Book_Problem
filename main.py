from contact import Contact
from address import AddressBook
from validator import validate_user_data
from addressbookmain import AddressBookMain


def main():
    """
    Main function to handle user input, validate data, and manage the address book.

    The function prompts the user for contact details, validates them, creates a Contact object,
    adds it to an AddressBook, and prints the address book's contents.
    """
    address_book_main = AddressBookMain()
    address_book = None

    while True:
        try:
            choice = int(input("\n1. Create New Address Book\n2. Manage Address Book\n3. Exit "))

            match choice:
                case 1:
                    address_book_name = input("Enter Name for Address Book: ")
                    address_book = address_book_main.add_address_book_to_main(address_book_name)

                case 2:
                    address_book_name = input("Enter the Name of Book you want to manage: ")
                    address_book = address_book_main.get_address_book_from_main(address_book_name)

                    if not address_book:
                        print("Address Book Not Found")
                        continue

                    while True:
                        try:
                            ch = int(input("\n1. Add Contact\n2. Display Contacts\n3. Edit Existing Contact"
                                           "\n4. Delete Existing Contact\n5. Exit\nEnter your choice: "))

                            match ch:
                                case 1:
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
                                    if address_book.contact_exists(user_data["fname"],user_data["lname"]):
                                        print(f"Contact with {user_data['fname']}{user_data['lname']} already exists")
                                    elif validate_user_data(user_data):
                                        contact = Contact(**user_data)
                                        address_book.add_contact(contact)
                                        print("Contact added successfully.")
                                    else:
                                        print("Invalid contact details. Please try again.")

                                case 2:
                                    address_book.print_address()

                                case 3:
                                    address_book.edit_contact()

                                case 4:
                                    address_book.delete_contact()

                                case 5:
                                    print("Exiting address book management.")
                                    break
                                case _:
                                    print("Invalid choice. Please try again.")

                        except ValueError:
                            print("Invalid input! Please enter a number.")

                case 3:
                    print("Exiting program.")
                    break

                case _:
                    print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")


if __name__ == "__main__":
    main()



   
   
    






   
   
    

