package com.example.student_management;

import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class StudentService {

    private final StudentRepository repository;

    public StudentService(StudentRepository repository) {
        this.repository = repository;
    }


    public List<Student> getAllStudents() {
        return repository.findAll();
    }

    public Optional<Student> getStudentByRollNumber(String rollNumber) {
        return repository.findByRollNumber(rollNumber);
    }

        public Student addStudent(Student student) {
        return repository.save(student);
    }


    public Optional<Student> updateStudent(Integer id, Student student) {

        return repository.findById(id)
                .map(existingStudent -> {

                    existingStudent.setName(student.getName());
                    existingStudent.setRollNumber(student.getRollNumber());
                    existingStudent.setClassName(student.getClassName());
                    existingStudent.setTamil(student.getTamil());
                    existingStudent.setEnglish(student.getEnglish());
                    existingStudent.setSocial(student.getSocial());
                    existingStudent.setMaths(student.getMaths());
                    existingStudent.setScience(student.getScience());

                    return repository.save(existingStudent);
                });
    }


    public boolean deleteStudent(Integer id) {

        if (repository.existsById(id)) {
            repository.deleteById(id);
            return true;
        }

        return false;
    }
}