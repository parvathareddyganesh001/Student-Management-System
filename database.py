import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, marks INTEGER)")

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        marks = int(input("Enter student marks: "))

        cursor.execute(
            "INSERT OR IGNORE INTO students(id, name, marks) VALUES (?, ?, ?)",(student_id, name, marks) )

        if cursor.rowcount == 0:
            print("Student ID already exists")
        else:
            connection.commit()
            print("Student added successfully!")

    elif choice == 2:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if len(students) == 0:
            print("No students found")
        else:
            for student in students:
                print(student)

    elif choice == 3:
        student_id = int(input("Enter student ID: "))

        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()

        if student is None:
            print("Student not found")
        else:
            print(student)

    elif choice == 4:
        student_id = int(input("Enter student ID: "))
        new_marks = int(input("Enter new marks: "))

        cursor.execute(
            "UPDATE students SET marks = ? WHERE id = ?",(new_marks, student_id))

        connection.commit()

        if cursor.rowcount == 0:
            print("Student not found")
        else:
            print("Student marks updated successfully!")

    elif choice == 5:
        student_id = int(input("Enter student ID to delete: "))

        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        connection.commit()

        if cursor.rowcount == 0:
            print("Student not found")
        else:
            print("Student deleted successfully!")

    elif choice == 6:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice!")

connection.close()