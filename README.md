# Student Management System

A simple Student Management System developed using Python, FastAPI, MySQL, HTML, CSS and JavaScript.

 Technologies Used

1. Python
2. FastAPI
3. MySQL
4. HTML
5. CSS
6. JavaScript

 Features

 Add student details
 View all students
 Search student by roll number
 Delete student
 REST APIs for student management
 MySQL database integration
 Frontend and backend integration

 Student Details

The System stores:

 Student ID
  Name
  Roll Number
  Class
  Tamil Mark
  English Mark
  Social Mark
  Maths Mark
  Science Mark

## REST APIs

  POST /students - Add student
  GET /students - Get all students
  GET /students/roll/{roll_number} - Get student by roll number
  PUT /students/{student_id} - Update student
  DELETE /students/{student_id} - Delete student

 Project Structure

Backend:

  app.py
  db.py
  student.py
  .gitignore

 Frontend:

  index.html
  student.html
  index.js
  index.css

 How It Works

The frontend sends requests to the FastAPI REST API using JavaScript `fetch()`.

The FastAPI backened processes the requests and communicates with the MySQL database using Python MySQL Connector.


Frontend
   |
JavaScript Fetch
   |
FastAPI REST API
   |
Python MySQL Connector
   |
MySQL

 API Documentation

FastAPI provides interactive API documentation through Swagger UI:

`http://127.0.0.1:8000/docs`

 Database

* Database: `student_db`
* Table: `students`
