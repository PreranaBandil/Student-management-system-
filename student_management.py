students = {}

while True:

    print("--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        roll_no = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        students[roll_no] = name

        print("Student Added Successfully")

    elif choice == "2":

        if students == {}:
            print("No Records Found")

        else:
            for roll_no, name in students.items():
                print("Roll No:", roll_no)
                print("Name:", name)

    elif choice == "3":

        search = input("Enter Roll Number: ")

        if search in students:
            print("Student Name:", students[search])

        else:
            print("Student Not Found")

    elif choice == "4":

        print("Program Closed")
        break

    else:
        print("Invalid Choice")