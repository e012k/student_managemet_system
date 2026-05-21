# Student Management System (Python + SQLite)


# main.py

import sqlite3

# Database Connection
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
''')

conn.commit()


# Student Class
class Student:

    def add_student(self):
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        marks = int(input("Enter Marks: "))

        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (student_id, name, course, marks)
        )

        conn.commit()

        print("Student Added Successfully\n")


    def view_students(self):

        cursor.execute("SELECT * FROM students")

        records = cursor.fetchall()

        if len(records) == 0:
            print("No Records Found\n")

        else:
            print("\nStudent Records")
            print("----------------------------")

            for row in records:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Course: {row[2]}")
                print(f"Marks: {row[3]}")
                print("----------------------------")


    def search_student(self):

        student_id = int(input("Enter Student ID to Search: "))

        cursor.execute(
            "SELECT * FROM students WHERE student_id=?",
            (student_id,)
        )

        row = cursor.fetchone()

        if row:
            print("\nStudent Found")
            print("----------------------------")
            print(f"ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Course: {row[2]}")
            print(f"Marks: {row[3]}")
            print("----------------------------")

        else:
            print("Student Not Found\n")


    def update_marks(self):

        student_id = int(input("Enter Student ID: "))
        new_marks = int(input("Enter New Marks: "))

        cursor.execute(
            "UPDATE students SET marks=? WHERE student_id=?",
            (new_marks, student_id)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Marks Updated Successfully\n")
        else:
            print("Student Not Found\n")


    def delete_student(self):

        student_id = int(input("Enter Student ID to Delete: "))

        cursor.execute(
            "DELETE FROM students WHERE student_id=?",
            (student_id,)
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully\n")
        else:
            print("Student Not Found\n")


# Main Menu
obj = Student()

while True:

    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        obj.add_student()

    elif choice == 2:
        obj.view_students()

    elif choice == 3:
        obj.search_student()

    elif choice == 4:
        obj.update_marks()

    elif choice == 5:
        obj.delete_student()

    elif choice == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice\n")


conn.close()

