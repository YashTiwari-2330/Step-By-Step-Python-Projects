def add_student(data):
    name = input("Enter student name: ")
    marks = []
    for i in range(1):
        mark = float(input(f"Enter Total mark of {name}: "))
        marks.append(mark)
    data.append((name, marks))
    print("✅ Student added successfully.\n")

def display_students(data):
    if not data:
        print("No student data found. add students\n")
        return
    print("\nStudent List:")
    for name, marks in data:
        print((f"Name: {name},\nTotal Marks: {marks}"))
    print()

def top_student(data):
    if not data:
        print("No data available.add students\n")
        return
    top = max(data, key=lambda x: sum(x[1]))
    print(f"🏆 Topper is {top[0]} with {sum(top[1])} marks.\n")

def average_marks(data):
    if not data:
        print("No data available.\n")
        return
    total = sum([sum(marks) for _, marks in data])
    count = len(data) * 3
    print(f"📊 Average mark of class: {total / count:.2f}\n")

def search_student(data):
    name = input("Enter student name to search: ")
    for student in data:
        if student[0].lower() == name.lower():
            print(f"Found: {student[0]} - Marks: {student[1]}")
            return
    print("❌ Student not found.\n")

def menu():
    data = []
    while True:
        print("1. Add Student\n2. Display Students\n3. Top Student\n4. Average Marks\n5. Search Student\n6. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_student(data)
        elif choice == '2':
            display_students(data)
        elif choice == '3':
            top_student(data)
        elif choice == '4':
            average_marks(data)
        elif choice == '5':
            search_student(data)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()
