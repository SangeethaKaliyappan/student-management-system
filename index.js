document.getElementById("studentForm").addEventListener("submit", addStudent);

function addStudent(event) {

    event.preventDefault();

    let student = {
        name: document.getElementById("name").value,
        rollNumber: document.getElementById("rollNumber").value,
        className: document.getElementById("className").value,
        tamil: document.getElementById("tamil").value,
        english: document.getElementById("english").value,
        social: document.getElementById("social").value,
        maths: document.getElementById("maths").value,
        science: document.getElementById("science").value
    };

    fetch("http://localhost:8080/students", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(student)
    });

    alert("Student Added!");
}
function getStudents() {

    fetch("http://localhost:8080/students")
        .then(response => response.json())
        .then(students => {

            let list = document.getElementById("studentList");

            list.innerHTML = "";

            students.forEach(student => {

                list.innerHTML += `
                    <tr>
                        <td>${student.id}</td>
                        <td>${student.name}</td>
                        <td>${student.rollNumber}</td>
                        <td>${student.className}</td>
                        <td>${student.tamil}</td>
                        <td>${student.english}</td>
                        <td>${student.social}</td>
                        <td>${student.maths}</td>
                        <td>${student.science}</td>
                        <td>
                            <button onclick="deleteStudent(${student.id})">
                                Delete
                            </button>
                        </td>
                    </tr>
                `;
            });
        });
}
function searchStudent() {

    let rollNumber = document.getElementById("rollNumber").value;

    fetch("http://localhost:8080/students/roll/" + rollNumber)
        .then(response => response.json())
        .then(student => {

            let list = document.getElementById("studentList");

            list.innerHTML = `
                <tr>
                    <td>${student.id}</td>
                    <td>${student.name}</td>
                    <td>${student.rollNumber}</td>
                    <td>${student.className}</td>
                    <td>${student.tamil}</td>
                    <td>${student.english}</td>
                    <td>${student.social}</td>
                    <td>${student.maths}</td>
                    <td>${student.science}</td>
                    <td>
                        <button onclick="deleteStudent(${student.id})">
                            Delete
                        </button>
                    </td>
                </tr>
            `;
        });
}
function deleteStudent(id) {

    fetch("http://localhost:8080/students/" + id, {
        method: "DELETE"
    })
    .then(() => {
        alert("Student deleted!");
        getStudents();
    });
}