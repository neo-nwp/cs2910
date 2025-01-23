import csv

# File paths 
STUDENTS_FILE = 'students.csv'
COURSES_FILE = 'courses.csv'
GRADES_FILE = 'grades.csv'

# constructor for file operations
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            return [row for row in reader]
    except FileNotFoundError:
        return []


def write_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(data)

#1: Output original list of all students
def list_students():
    students = read_csv(STUDENTS_FILE)
    if not students:
        print("No students found.")
        return
    print("\nOriginal List of Students:")
    for row in students:
        print(row)

#2: Output list of all students sorted by name in ascending or reverse order
def sort_students():
    students = read_csv(STUDENTS_FILE)
    sorted_students = []
    if not students:
        print("No students found!")
        return

    print("Please press (A) for Alphabetical order or (R) for Reverse order")
    order_choice = input("Enter your choice: ").strip().lower()

    if order_choice == 'a':  # Alphabetical order
        students.sort(key=lambda students : students[2])  # Sort by last name
        for i in students:
            print(i) 
    elif order_choice == 'r':  # Reverse order
        students.sort(key=lambda students : students[2], reverse=True)  # Reverse sort
        #print("hellp")
        for i in students:
            print(i)
    else:
        print("Invalid choice. Please enter 'A' or 'R'.")
        return

#3: Output original list of all courses
def list_courses():
    courses = read_csv(COURSES_FILE)
    if not courses:
        print("No courses found.")
        return
    print("\nOriginal List of Courses:")
    for row in courses:
        print(row)

#4: Output courses for a specific semester
def courses_by_semester():
    semester = input("Enter semester (e.g., fall, winter): ").strip().lower()
    courses = read_csv(COURSES_FILE)
    filtered_courses = [row for row in courses if len(row) > 1 and row[1].lower() == semester]
    if not filtered_courses:
        print(f"No courses found for the {semester} semester.")
        return
    print(f"\nCourses in {semester.capitalize()} Semester:")
    for row in filtered_courses:
        print(row)

#5: Output courses for a specific semester sorted by name in alphabetic order or vice versa
def courses_by_semester_sorted():
    semester = input("Enter semester (e.g., fall, winter): ").strip().lower()
    courses = read_csv(COURSES_FILE)
    filtered_courses = [row for row in courses if len(row) > 1 and row[1].lower() == semester]
    
    if not filtered_courses:
        print(f"No courses found for the {semester} semester.")
        return

    print("Please press (A) for Alphabetic order or (R) for Reverse order")
    choice = input("Enter your choice: ").strip().lower()

    if choice == 'a':
        sorted_courses = sorted(filtered_courses, key=lambda row: row[0])  # Alphabetic order
    elif choice == 'r':
        sorted_courses = sorted(filtered_courses, key=lambda row: row[0], reverse=True)  # Reverse alphabetic order
    else:
        print("Invalid choice! Defaulting to alphabetic order.")
        sorted_courses = sorted(filtered_courses, key=lambda row: row[0])

    print(f"\nCourses in {semester.capitalize()} Semester (Sorted):")
    for row in sorted_courses:
        print(row)



#6: Add new student, course, or grade
def add_student_course_grade():
    # Step 1: Add a new student
    last_name = input("Enter last name: ").strip()
    first_name = input("Enter first name: ").strip()
    phone_number = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    students = read_csv(STUDENTS_FILE)
    new_student_id = str(len(students) + 1)  # Generate a new unique ID
    new_student = [new_student_id, last_name, first_name, phone_number, email]
    students.append(new_student)
    write_csv(STUDENTS_FILE, students)  # Save back to the CSV
    print("New student added successfully!")

    # Step 2: Add a new course
    course_name = input("Enter course name: ").strip()
    course_code = input("Enter course code: ").strip()
    semester = input("Enter semester: ").strip()

    courses = read_csv(COURSES_FILE)
    new_course_id = str(len(courses) + 1)  # Generate a new unique course ID
    new_course = [course_name, course_code, semester]
    courses.append(new_course)
    write_csv(COURSES_FILE, courses)  # Save back to the CSV
    print("New course added successfully!")

    # Step 3: Add a grade for the student and course
    print("Entering grade----")
    student_last_name = last_name
    entered_course_code = course_code
    grade = input("Enter grade: ").strip()

    # Find the student ID based on the last name
    student = next((row for row in students if row[1].lower() == student_last_name.lower()), None)
    if not student:
        print("Student not found!")
        return

    student_id = student[0]

    # Find the course ID based on the course code
    course = next((row for row in courses if row[1].lower() == entered_course_code.lower()), None)
    if not course:
        print("Course not found!")
        return

    course_id = course[1]

    # Add the grade
    grades = read_csv(GRADES_FILE)
    new_grade_entry = [student_id, student_last_name, course_id, grade]
    grades.append(new_grade_entry)
    write_csv(GRADES_FILE, grades)  # Save back to the CSV
    print("Grade added successfully!")


#7: Update student info
def update_student():
    students = read_csv(STUDENTS_FILE)
    grades= read_csv(GRADES_FILE)
    student_id = input("Enter student ID: ").strip()
    for row in students:
        if row[0] == student_id:
            print(f"Current info: {row}")
            row[1] = input("Enter new last name: ").strip() or row[1]
            row[2] = input("Enter new first name: ").strip() or row[2]
            row[3] = input("Enter new phone: ").strip() or row[3]
            row[4] = input("Enter new email: ").strip() or row[4]
            write_csv(STUDENTS_FILE, students)
            write_csv(GRADES_FILE, students)
            print("Student info updated successfully!")
            return
    print("Student ID not found!")

#8-9: Search for courses
def search_course():
    courses = read_csv(COURSES_FILE)
    choice = input("Search by (1) Name or (2) Code? Enter 1 or 2: ").strip()
    if choice == '1':
        name = input("Enter course name: ").strip()
        result = [row for row in courses if len(row) > 0 and row[0].lower() == name.lower()]
    elif choice == '2':
        code = input("Enter course code: ").strip()
        result = [row for row in courses if len(row) > 1 and row[1] == code]
    else:
        print("Invalid choice!")
        return
    if result:
        print("Search Result:")
        for row in result:
            print(row)
    else:
        print("No matching course found!")

#10-11 Search for students
def search_student():
    students = read_csv(STUDENTS_FILE)
    choice = input("Search by (1) Last Name or (2) Phone Number? Enter 1 or 2: ").strip()
    if choice == '1':
        last_name = input("Enter last name: ").strip()
        result = [row for row in students if len(row) > 1 and row[1].lower() == last_name.lower()]
    elif choice == '2':
        phone = input("Enter phone number: ").strip()
        result = [row for row in students if len(row) > 3 and row[3] == phone]
    else:
        print("Invalid choice!")
        return
    if result:
        print("Search Result:")
        for row in result:
            print(row)
    else:
        print("No matching student found!")

#12-13: Show courses and grades by student
def courses_and_grades_by_student():
    student_last_name = input("Enter student last name: ").strip().lower()

    # Read data from CSV files
    grades = read_csv(GRADES_FILE)
    courses = read_csv(COURSES_FILE)
    students = read_csv(STUDENTS_FILE)

    if not grades or not courses or not students:
        print("Error: One or more files could not be loaded.")
        return

    # Find student ID(s) for the given last name
    student_ids = [
        row[0] for row in students
        if len(row) > 1 and row[1].strip().lower() == student_last_name
    ]

    if not student_ids:
        print(f"No student found with last name: {student_last_name}.")
        return

    # Map course IDs to course names and semesters
    course_map = {row[2]: (row[0], row[1]) for row in courses if len(row) > 2}

    # Get courses and grades for the student
    results = []
    for row in grades:
        if row[0] in student_ids:  # Match student ID
            course_id = row[0]
            course_info = course_map.get(course_id, ("Unknown Course", "Unknown Semester"))
            course_name, semester = course_info
            grades_list = [g if g.lower() != "na" else "N/A" for g in row[3:]]
            results.append((course_name, semester, grades_list))

    # Display the results
    if not results:
        print(f"No courses or grades found for {student_last_name}.")
        return

    print(f"\nCourses and Grades for {student_last_name.capitalize()}:")
    for course_name, semester, grades_list in results:
        print(f"Course: {course_name} (Semester: {semester.capitalize()})")
        print(f"Grades: {', '.join(grades_list)}")




#14 Calculate average grade for a student
def calculate_average_grade():
    student_last_name = input("Enter student last name: ").strip()
    grades = read_csv(GRADES_FILE)
    student_grades = [float(g) for row in grades if len(row) > 1 and row[1].lower() == student_last_name.lower() for g in row[4:] if g != 'na']
    if student_grades:
        print(f"Average Grade for {student_last_name}: {sum(student_grades) / len(student_grades):.2f}")
    else:
        print("No grades found for the student!")

#15: Calculate average grade for student for specific term
def calculate_average_grade_for_term():
    # Input from the user
    student_last_name = input("Enter student last name: ").strip()
    semester = input("Enter semester: ").strip().lower()

    # Read CSV files
    grades = read_csv(GRADES_FILE)
    courses = read_csv(COURSES_FILE)
    students = read_csv(STUDENTS_FILE)

    if not grades or not courses or not students:
        print("Error: One or more files could not be loaded.")
        return

    # Map student ID by last name
    student_ids = [
        row[0] for row in students
        if len(row) > 1 and row[1].strip().lower() == student_last_name.lower()
    ]

    if not student_ids:
        print(f"No student found with last name: {student_last_name}")
        return

    # Find course IDs for the given semester
    course_ids = [
        row[2] for row in courses
        if len(row) > 1 and row[1].strip().lower() == semester
    ]

    if not course_ids:
        print(f"No courses found for semester: {semester.capitalize()}")
        return

    # Find grades for the student in the relevant courses
    student_grades = []
    for row in grades:
        if row[0] in student_ids and row[0] in course_ids:
            for grade in row[3:]:
                if grade.lower() != "na":
                    try:
                        student_grades.append(float(grade))
                    except ValueError:
                        print(f"Warning: Invalid grade format in row: {row}")

    # Calculate and display the average
    if student_grades:
        average = sum(student_grades) / len(student_grades)
        print(f"Average Grade for {student_last_name} in {semester.capitalize()} Semester: {average:.2f}")
    else:
        print(f"No grades found for {student_last_name} in {semester.capitalize()} semester!")

#16: Calculate average grade for specific course(user input course name)
def calculate_average_grade_for_course():
    course_name = input("Enter course name: ").strip().lower()

    # Read CSV files
    grades = read_csv(GRADES_FILE)
    courses = read_csv(COURSES_FILE)

    if not grades or not courses:
        print("Error: One or more files could not be loaded.")
        return

    # Find the course ID for the given course name
    course_ids = [
        row[2] for row in courses
        if len(row) > 1 and row[0].strip().lower() == course_name
    ]

    if not course_ids:
        print(f"No course found with name: {course_name}")
        return

    # Find grades for the given course ID(s)
    course_grades = []
    for row in grades:
        if row[0] in course_ids:  # Match course IDs
            for grade in row[3:]:
                if grade.lower() != "na":
                    try:
                        course_grades.append(float(grade))
                    except ValueError:
                        print(f"Warning: Invalid grade format in row: {row}")

    # Calculate and display the average
    if course_grades:
        average = sum(course_grades) / len(course_grades)
        print(f"Average Grade for {course_name.capitalize()}: {average:.2f}")
    else:
        print(f"No grades found for course: {course_name.capitalize()}!")

# Main menu
def main():
    while True:
        print("\n--- Menu ---")
        print("1. List all students")
        print("2. Sort students by name")
        print("3. List all courses")
        print("4. List courses by semester")
        print("5. List all courses sorted by course name")
        print("6. Add a new student , course and grade")
        print("7. Update student info")
        print("8. Search for a course (by name or code)")
        print("9. Search for a student (by last name or phone number)")
        print("10. Show courses and grades by student")
        print("11. Calculate average grade for a student (user inputs last name)")
        print("12. Calculate average grade for student for specific term (user inputs last name and term)")
        print("13. Calculate average grade for specific course(user input course name)")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            list_students()
        elif choice == '2':
            sort_students()
        elif choice == '3':
            list_courses()
        elif choice == '4':
            courses_by_semester()
        elif choice=='5':
            courses_by_semester_sorted()
        elif choice == '6':
            add_student_course_grade()   #6,7,8
        elif choice == '7':
            update_student()    #9
        elif choice == '8':
            search_course()    #10
        elif choice == '9':
            search_student()    #11
        elif choice == '10':
            courses_and_grades_by_student() #12
        elif choice == '11':
            calculate_average_grade()   #14
        elif choice == '12':
            choice = calculate_average_grade_for_term()
        elif choice == '13':
            calculate_average_grade_for_course()
        
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
