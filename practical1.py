#Student mark management

def input_number_of_students():
    return int(input("Enter the number of the class: "))

def input_student_information(num_students):
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD-MM-YYYY): ")
        students.append((student_id, name, dob))  
    return students

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information(num_courses):
    courses = {}
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name  
    return courses

def input_student_marks(courses, students):
    marks = {}
    for course_id in courses.keys():
        marks[course_id] = {}
        print(f"\nEntering marks for course: {courses[course_id]}")
        for student in students:
            student_id = student[0]
            mark = float(input(f"Enter mark for {student[1]} (ID: {student_id}): "))
            marks[course_id][student_id] = mark  # {course_id: {student_id: mark}}
    return marks