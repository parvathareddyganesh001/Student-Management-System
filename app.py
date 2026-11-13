from flask import Flask, render_template, request, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "student123"

def get_db_connection():
    connection = sqlite3.connect("students.db")
    return connection

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        if "search" in request.form:

            search_id = request.form["search_id"]

            connection = get_db_connection()

            students = connection.execute(
                "SELECT * FROM students WHERE id = ?",
                (search_id,)
            ).fetchall()

            connection.close()

            if students:
                flash("Student found successfully!")
            else:
                flash("Student not found!")

            return render_template("index.html", students=students)

        elif "update" in request.form:

            update_id = request.form["update_id"]
            new_marks = request.form["new_marks"]

            connection = get_db_connection()

            result = connection.execute(
                "UPDATE students SET marks = ? WHERE id = ?",
                (new_marks, update_id)
            )

            connection.commit()
            connection.close()

            if result.rowcount > 0:
                flash("Student marks updated successfully!")
            else:
                flash("Student ID not found!")

        elif "delete" in request.form:

            delete_id = request.form["delete_id"]

            connection = get_db_connection()

            result = connection.execute(
                "DELETE FROM students WHERE id = ?",
                (delete_id,)
            )

            connection.commit()
            connection.close()

            if result.rowcount > 0:
                flash("Student deleted successfully!")
            else:
                flash("Student ID not found!")

        else:

            student_id = request.form["student_id"]
            student_name = request.form["student_name"]
            marks = request.form["marks"]

            connection = get_db_connection()

            connection.execute(
                "INSERT INTO students (id, name, marks) VALUES (?, ?, ?)",
                (student_id, student_name, marks)
            )

            connection.commit()
            connection.close()

            flash("Student added successfully!")

    connection = get_db_connection()
    students = connection.execute("SELECT * FROM students").fetchall()
    connection.close()

    return render_template("index.html", students=students)

app.run(debug=True)