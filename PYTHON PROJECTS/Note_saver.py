import os
from random import choice

file_name = "notes.txt"

# FUNCTION TO ADD A NOTE

def add_note():
    note = input("Enter Notes :-")
    with open(file_name , "a") as f:
        f.write(note + "\n")
        print("\nNote Saved Successfully..")

# FUNCTION TO VIEW DATA
def view_data():
    if not os.path.exists(file_name):
        print("No data found!")
        return
    with open (file_name , "r")  as f:
        notes = f.readlines()
    if notes:
        print("\nYour Notes:")
        for i,notes in enumerate(notes,start=1):
            print(f"{i}.{notes.strip()}")
    else:
        print("No notes found")

# FUNCTION TO DELETE ALL DATA
def delete_all_data():
    if os.path.exists(file_name):
        os.remove(file_name)
        print("\n All Note Delete")
    else:
        print("No Notes Deleted")

# FUNCTION TO SEARCH WORD AND GIVE LINE
def search_word():
    word = input("Enter words :-")
    line = 1
    data = True
    with open("notes.txt" , "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f"founded line is :{line}")
                return
            line += 1
    return -1


def main():
    while True:
        print("\n==========Note Saver==========")
        print("1. Add Note")
        print("2. View Data")
        print("3. Delete All data")
        print("4. Search Line")
        print("5 . Exit")

        choice = input("Enter Your Choice :-")

        if choice == "1":
            add_note()

        elif choice == "2":
            view_data()

        elif choice == "3":
            delete_all_data()

        elif choice == "4":
            search_word()

        elif choice == "5":
            exit("Good Bye..")

        else:
            print("Choise Valid Index..")
if __name__ == '__main__':
    main()