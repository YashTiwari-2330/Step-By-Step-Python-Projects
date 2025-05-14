from cmath import phase

contact = {}

def is_valid_number(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact():
    name = input("Enter Contact Name :-").strip()

    if name in contact:
        print("Contact Is Already Exists,try with different name.")

    else:
        phone = (input("Enter Phone Number (10-digit) :-"))
        if not is_valid_number(phone):
            print("❌ Invalid phone number. Must be exactly 10 digits.\n")
            return
        email = input("Enter E-mail address:-")
        contact [name] = {phone , email}
        print(f"✅ CONTACT '{name}' ADDED SUCCESSFULLY.\n")

def view_contact():
    if not contact:
        print("CONTACT BOOK ARE EMPTY, !PLEASE ADD CONTACTS")
        return
    print("--------- CONTACTS LIST --------")
    for name , details in contact.items():
        print(f"Name : {name}")
        print(f"Details : {details}")
        print("------------------------------")

def search_contact():
    name = input("Enter Name to search :-").strip()

    if name in contact:
        print(f"NAME : {name}")
        print(f"DETAILS : {contact[name]}\n")

    else:
        print("Contact not found..")

def update_contact():
    name = input("Enter contact name to update: ").strip()
    if name in contact:
        confirm = input(f"Are you sure you want to update '{name}'? (yes/no): ").lower()
        if confirm == 'yes':
            print(f"Current details: {contact[name]}")
            name = input("Enter Your Updated Name :-")
            phone = input("Enter new phone number (10 digits): ")
            if not is_valid_number(phone):
                print("❌ Invalid phone number. Must be exactly 10 digits.\n")
                return
            email = input("Enter new email address: ")
            contact[name] = {name , phone, email}
            print(f"✅ Contact '{name}' updated successfully.\n")
        else:
            print("❌ UPDATE CANCELED.\n")
    else:
        print("❌ Contact not found.\n")

def delete_contact():
    name = input("Enter contact name to delete..").strip()
    if name in contact:
        confirm = input(f"Are you sure you want to update '{name}'? (yes/no): ").lower()
        if confirm =="yes":
            print(f"CONTACT FOUND AND DETAILS IS {contact[name]}")
            del contact[name]
            print(f"✅ CONTACT {name} DELETED SUCCESSFULLY.\n")

        else:
            print("❌ DELETE CANCELED.\n")

    else:
        print("❌ CONTACT NOT FOUND.\n")

def count_contact():
    print(f"Total Contacts : {len(contact)}\n")


def menu():
    while True:
        print("\n *********** CONTACT BOOK APP ***********")
        print("1. ADD CONTACT")
        print("2. VIEW CONTACT")
        print("3. SEARCH CONTACT")
        print("4. UPDATE CONTACT")
        print("5. DELETE CONTACT")
        print("6. COUNT TOTAL CONTACT")
        print("7. EXIT")

        choice = input("Enter Choice Between (1-7) :-")

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contact()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            count_contact()

        elif choice == "7":
            exit("GOOD BYE , THANK YOU FOR USING")

        else:
            print("INVALID CHOICE PLEASE CHOICE (1-7) NUMBERS :-\n")

menu()