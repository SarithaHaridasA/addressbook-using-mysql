import manageAddressBookParentClass as AddressBook

# Man class loaded to execute the application
class AddressBookMain(AddressBook.AddressBook):

    def __init__(self):
        super().__init__("data.json")

    def mainFunction(self):
        while True:
            print("\nAddress Book Application")
            print("1. Add Contact")
            print("2. View All Contacts from list")
            print("3. Search Contact")
            print("4. Exit\n")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                super().add_contact()

            elif choice == '2':
                super().view_all_contacts()

            elif choice == '3':
                super().search_contact()

            elif choice == '4':
                print("Exiting Address Book Application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


ob1 = AddressBookMain()
ob1.mainFunction()
