from contact import Contact
from address import AddressBook
from validator import validate_user_data
from addressbookmain import AddressBookMain
from addressbookmain import AddressBookMainSearch

def main():
    """
    Main function to handle user input, validate data, and manage the address book.

    The function prompts the user for contact details, validates them, creates a Contact object,
    adds it to an AddressBook, also search contact by city and state ,and prints the address book's contents.
    """
    address_book_main = AddressBookMain()

    while True:
        try:
            choice = int(input("\n1. Create New Address Book\n2. Manage Address Book\n3. Search Contact\n4. Exit\nEnter choice: "))

            match choice:
                case 1:
                    address_book_name = input("Enter Name for Address Book: ").strip()
                    address_book_main.add_address_book_to_main(address_book_name)
                    print(f"Address book '{address_book_name}' created successfully.")

                case 2:
                    address_book_name = input("Enter the Name of the Address Book you want to manage: ").strip()
                    address_book = address_book_main.get_address_book_from_main(address_book_name)

                    if address_book is None:
                        print(f" Address Book '{address_book_name}' Not Found! Please create it first.")
                        continue  

                    print(f" Managing Address Book: {address_book_name}")

                    while True:
                        try:
                            ch = int(input("\n1. Add Contact\n2. Display Contacts\n3. Edit Contact"
                                           "\n4. Delete Contact\n5. Exit\nEnter your choice: "))

                            match ch:
                                case 1:
                                    user_data = {
                                        "fname": input("Enter First Name: ").strip(),
                                        "lname": input("Enter Last Name: ").strip(),
                                        "city": input("Enter City: ").strip(),
                                        "state": input("Enter State: ").strip(),
                                        "zip_code": input("Enter Zip Code: ").strip(),
                                        "address": input("Enter Address: ").strip(),
                                        "phone_num": input("Enter Phone Number: ").strip(),
                                        "email": input("Enter Email: ").strip()
                                    }
                                    if address_book.contact_exists(user_data["fname"], user_data["lname"]):
                                        print(f" Contact {user_data['fname']} {user_data['lname']} already exists.")
                                    elif validate_user_data(user_data):
                                        contact = Contact(**user_data)
                                        address_book.add_contact(contact)
                                        print(" Contact added successfully.")
                                    else:
                                        print(" Invalid contact details. Please try again.")

                                case 2:
                                    print(" Displaying contacts:")
                                    address_book.print_address()

                                case 3:
                                    address_book.edit_contact()

                                case 4:
                                    address_book.delete_contact()

                                case 5:
                                    print(f" Exiting Address Book '{address_book_name}' management.")
                                    break  

                                case _:
                                    print(" Invalid choice. Please try again.")

                        except ValueError:
                            print(" Invalid input! Please enter a number.")

                case 3:
                    search_by = input("Search by 'city' or 'state': ").strip().lower()
                    if search_by == "city":
                        city = input("Enter city name to search contacts: ").strip()
                        contact_searcher = AddressBookMainSearch(address_book_main, city, "")
                        contact_searcher.search_person_city()
                    elif search_by == "state":
                        state = input("Enter state name to search contacts: ").strip()
                        contact_searcher = AddressBookMainSearch(address_book_main, "", state)
                        contact_searcher.search_person_state()
                    else:
                        print(" Invalid option. Please enter 'city' or 'state'.")

                case 4:
                    print(" Exiting program.")
                    break

                case _:
                    print(" Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()







   
   
    






   
   
    

