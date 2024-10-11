import sqlite3
import json

try:
    conn = sqlite3.connect("HyperionDev.db")
except sqlite3.Error:
    print("Please store your database as HyperionDev.db")
    quit()

cur = conn.cursor()

def usage_is_incorrect(input, num_args):
    if len(input) != num_args + 1:
        print(f"The {input[0]} command requires {num_args} arguments.")
        return True
    return False

def store_data_as_json(data, filename):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def store_data_as_xml(data, filename):
    with open(filename,'w') as f:
        f.write(data)

def offer_to_store(data):
    while True:
        print("Would you like to store this result?")
        choice = input("Y/[N]? : ").strip().lower()

        if choice == "y":
            filename = input("Specify filename. Must end in .xml or .json: ")
            ext = filename.split(".")[-1]
            if ext == 'xml':
                store_data_as_xml(data, filename)
            elif ext == 'json':
                store_data_as_json(data, filename)
            else:
                print("Invalid file extension. Please use .xml or .json")

        elif choice == 'n':
            break

        else:
            print("Invalid choice")

usage = '''
What would you like to do?

d - demo
vs <student_id>            - view subjects taken by a student
la <firstname> <surname>   - lookup address for a given firstname and surname
lr <student_id>            - list reviews for a given student_id
lc <teacher_id>            - list all courses taken by teacher_id
lnc                        - list all students who haven't completed their course
lf                         - list all students who have completed their course and achieved 30 or below
e                          - exit this program

Type your option here: '''

print("Welcome to the data querying app!")

while True:
    print()
    # Get input from user
    user_input = input(usage).split(" ")
    print()

    # Parse user input into command and args
    command = user_input[0]
    if len(user_input) > 1:
        args = user_input[1:]

    if command == 'd': # demo - a nice bit of code from me to you - this prints all student names and surnames :)
        data = cur.execute("SELECT * FROM Student")
        for _, firstname, surname, _, _ in data:
            print(f"{firstname} {surname}")
        
    elif command == 'vs': # view subjects by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None

        # Run SQL query and store in data
        cursor = cur.execute('''SELECT Course.course_name 
                       FROM Course INNER JOIN StudentCourse
                       ON StudentCourse.course_code = Course.course_code
                       WHERE StudentCourse.student_id = student_id''') 
        rows = cursor.fetchall()
        data = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
                data.append(d)
        offer_to_store(data)

    elif command == 'la':# list address by name and surname
        if usage_is_incorrect(user_input, 2):
            continue
        firstname, surname = args[0], args[1]
        data = None

        # Run SQL query and store in data
        cursor = cur.execute('''SELECT Address.street, Address.city
                       FROM Address INNER JOIN Student
                       ON Student.address_id = Student.address_id
                       WHERE Student.first_name = firstname AND Student.last_name = surname''') 
        rows = cursor.fetchall()
        data = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
                data.append(d)

        offer_to_store(data)
    
    elif command == 'lr':# list reviews by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        student_id = args[0]
        data = None

        # Run SQL query and store in data
        cursor = cur.execute('''SELECT Review.completeness, Review.efficiency, Review.style, Review.documentation
                       FROM Review INNER JOIN StudentCourse
                       ON Review.student_id = Student.student_id
                       WHERE StudentCourse.student_id = student_id''') 
        rows = cursor.fetchall()
        data = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
                data.append(d)
        offer_to_store(data)

    elif command == 'lc':# list reviews by student_id
        if usage_is_incorrect(user_input, 1):
            continue
        teacher_id = args[0]
        data = None

        # Run SQL query and store in data
        cursor = cur.execute('''SELECT Course.course_name
                       FROM Course INNER JOIN Teacher
                       ON Course.teacher_id = Teacher.teacher_id
                       WHERE Teacher.teacher_id = teacher_id''') 
        rows = cursor.fetchall()
        data = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
                data.append(d)
        offer_to_store(data)

    
    elif command == 'lnc':# list all students who haven't completed their course
        data = None

        # Run SQL query and store in data
        cursor = cur.execute('''SELECT Student.student_id, Student.first_name, Student.last_name, Student.email, Course.course_name
                       FROM Student INNER JOIN StudentCourse
                       ON Student.student_id = StudentCourse.student_id
                       INNER JOIN Course
                       ON Student.course._code = Course.course_code
                       WHERE Student.is_completed = TRUE''') 
        rows = cursor.fetchall()
        data = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
                data.append(d)

    elif command == 'lf':# list all students who have completed their course and got a mark <= 30
        data = None

        # Run SQL query and store in data
        cursor = cur.execute('''SELECT Student.student_id, Student.first_name, Student.last_name, Student.email, Course.course_name,                           StudentCourse.mark
                       FROM Student INNER JOIN StudentCourse 
                       ON Student.student_id = StudentCourse.student_id
                       INNER JOIN Course
                       ON Student.course._code = Course.course_code
                       WHERE StudentCourse.mark < 30''') 
        rows = cursor.fetchall()
        data = []
        for row in rows:
            d = {}
            for i, col in enumerate(cursor.description):
                d[col[0]] = row[i]
                data.append(d)

        offer_to_store(data)
        pass
    
    elif command == 'e':# list address by name and surname
        print("Programme exited successfully!")
        break
    
    else:
        print(f"Incorrect command: '{command}'")