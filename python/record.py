students = {
    1: {
        'id': 1,
        'name': 'Alice',
        'age': 20,
        'school_name': 'XYZ School',
        'completed_courses': {
            'Math': 90,
            'Science': 88,
            'History': 75,
        },
        'ongoing_courses': {
            'English': 'In Progress',
            'Art': 'In Progress',
        }
    },
     2: {
        'id': 2,
        'name': 'Bob',
        'age': 21,
        'school_name': 'ABC School',
        'completed_courses': {
            'Math': 85,
            'Science': 92,
            'History': 78,
        },
        'ongoing_courses': {
            'English': 'In Progress',
            'Gym': 'In Progress',
        }
    },
}
def view_all_students():
    for student_id, student_info in students.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"School Name: {student_info['school_name']}")
        print()
        
def view_student_info(student_id):
    student_info = students.get(student_id)
    if student_info:
        print(f"Student ID: {student_info['id']}")
        print(f"Name: {student_info['name']}")
        print(f"Age: {student_info['age']}")
        print(f"School Name: {student_info['school_name']}")
        print()
    else:
        print("Student not found.")
