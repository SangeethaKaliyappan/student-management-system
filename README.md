Student Management System

A simple Student Management System developed using Java Spring Boot, MySQL, HTML, CSS and JavaScript.

 Technologies Used

  1. Java
  2.Spring Boot
  3. Spring Data JPA
  4. MySQL
  5. HTML
  6. CSS
  7. JavaScript
  8. Maven

 Features

 Add student details
 View all students
 Search student by roll number
 Delete student
 REST APIs for student management
 MySQL database integration

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

 REST APIs

POST /students - Add student
GET /students - Get all students
GET /students/roll/{rollNumber} - Get student by roll number
PUT /students/{id} - Update student
DELETE /students/{id} - Delete student

 Project Structure

Backend:
- pom.xml
- src/

Frontend:
- index.html
- student.html
- index.js
- index.css




The frontend sends requests to the Spring Boot REST API using JavaScript fetch.

The Spring Boot backend processes the request and communicates with the MySQL database using Spring Data JPA.


Frontend
   |
JavaScript Fetch
   |
Spring Boot REST API
   |
Spring Data JPA
   |
MySQL
