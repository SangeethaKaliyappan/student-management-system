from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from student import Student
from db import get_connection

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Student Management System API"}


@app.post("/students")
def add_student(student: Student):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students
        (name, roll_number, class_name, tamil, english, social, maths, science)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        student.name,
        student.roll_number,
        student.class_name,
        student.tamil,
        student.english,
        student.social,
        student.maths,
        student.science
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {"message": "Student added successfully"}


@app.get("/students")
def get_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


@app.get("/students/roll/{roll_number}")
def get_student_by_roll(roll_number: str):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM students WHERE roll_number = %s"
    cursor.execute(query, (roll_number,))

    student = cursor.fetchone()

    cursor.close()
    connection.close()

    if student:
        return student

    return {"message": "Student not found"}


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE students
        SET name=%s, roll_number=%s, class_name=%s,
            tamil=%s, english=%s, social=%s, maths=%s, science=%s
        WHERE id=%s
    """

    values = (
        student.name,
        student.roll_number,
        student.class_name,
        student.tamil,
        student.english,
        student.social,
        student.maths,
        student.science,
        student_id
    )

    cursor.execute(query, values)
    connection.commit()

    updated_rows = cursor.rowcount

    cursor.close()
    connection.close()

    if updated_rows == 0:
        return {"message": "Student not found"}

    return {"message": "Student updated successfully"}


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    connection.commit()

    deleted_rows = cursor.rowcount

    cursor.close()
    connection.close()

    if deleted_rows == 0:
        return {"message": "Student not found"}

    return {"message": "Student deleted successfully"}