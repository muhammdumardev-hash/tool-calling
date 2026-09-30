students = {
    "STU-101": {
        "name": "Muhammad Ali",
        "gpa": 3.4,
        "status": "Passed"
    },
    "STU-102": {
        "name": "Ahmed Khan",
        "gpa": 3.1,
        "status": "Passed"
    },
    "STU-103": {
        "name": "Usman Raza",
        "gpa": 3.7,
        "status": "Passed"
    }
}


def get_student_result(student_id):

    student_id = student_id.upper()

    if student_id not in students:
        return f"No student record was found for {student_id}."

    student = students[student_id]

    return (
        f"Student ID: {student_id}\n"
        f"Name: {student['name']}\n"
        f"GPA: {student['gpa']}\n"
        f"Status: {student['status']}"
    )