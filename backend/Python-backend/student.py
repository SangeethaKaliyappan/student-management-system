from pydantic import BaseModel


class Student(BaseModel):
    name: str
    roll_number: str
    class_name: str
    tamil: int
    english: int
    social: int
    maths: int
    science: int