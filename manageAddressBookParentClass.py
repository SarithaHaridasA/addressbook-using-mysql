import database
from datetime import datetime


class AddressBook(database.DatabaseOperations):

    def __init__(self, filepathFomMainClass):
        super().__init__()

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        data = {
            'first_name': name,
            'email': email,
            'phone': phone,
            'created_at': datetime.now()
        }
        super().save_data(data, 'contacts')
        print(f"Contact {name} saved successfully.")

    def search_contact(self):
        search_value = input("Enter the contacts to search: ")
        result = super().search_values_from_contacts(search_value.lower())
        print("** Search Results of Contacts:")
        for row in result:
            print(row)

    def view_all_contacts(self):
        result = super().fetch_all_values('contacts')
        for row in result:
            print(row)
