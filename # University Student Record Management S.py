 import os
students=[]

def add_student():
    stu_id = input("Enter the student ID (e.g., U20251105): ").strip().upper()
    for s in stu_id:
        if len(stu_id) == 9:
            if stu_id[0]== 'U':
                for x in range (1,9):
                    if stu_id[x].isnumeric():
                        student_id = stu_id
                        break
                    else:
                        print("2nd to 8th charecters must be numerical value.")
                        stu_id = input("Enter the student ID (e.g., U20251105): ").strip().upper()
            else:
                print("Student Id must be starting with 'U'.")
                stu_id = input("Enter the student ID (e.g., U20251105): ").strip().upper()
        else:
            print("Student id must be in 9 charecters.")
            stu_id = input("Enter the student ID (e.g., U20251105): ").strip().upper()
    
    first = input("First name: ").strip().capitalize()
    for x in first:
        if first.isalpha():
            first_name = first
            break
        else:
            print("First name must be alphabetic.")
            first = input("First name: ").strip().capitalize()

    last = input("Last name: ").strip().capitalize()
    for x in last:
        if last.isalpha():
            last_name = last
            break
        else:
            print("Last name must be alphabetic.")
            last = input("Last name: ").strip().capitalize()
    
    course = input("Course: ").strip().upper()
    while True:
        sem_al = input("Semester ('1' to '8'): ").strip()
        if sem_al.isnumeric():
            sem = int(sem_al)
            break
        else:
            print("Only numerical value is allowed.")
    for x in sem_al:
        if sem>=1 and sem<=8 :
            semester= sem
            break
        else:
            print("Semezster must be 1 to 8.")
            while True:
                sem_al = input("Semester ('1' to '8'): ").strip()
                if sem_al.isnumeric():
                    sem = int(sem_al)
                    break
                else:
                    print("Only numerical value is allowed.")
            
    
    marks = {}
    while True:
        num_sub_alt = input("Enter how many subjects to add: ").strip()
        if num_sub_alt.isnumeric():
            num_sub= int(num_sub_alt)
            break
        else:
            print("Please enter a numerical value.")

    for i in range(num_sub):
        while True:
            subject_alt = input("Subject: ").strip().title()
            if subject_alt.isalpha:
                subject= subject_alt
                break
            else:
                print("Please enter a alphabetic value.")
        while True:
            print("Adding marks")
            mark = input(f"Enter Score in {subject}: ").strip()
            if mark.isnumeric():
                marks[subject] = int(mark)
                break
            else:
                print("Please enter a numerical value")

    house = input("House: ").strip().upper()
    for student in students:
        if student["id"] == student_id:
            print("Sorry! This student already added.")
            return
    street = input("Street: ").strip().capitalize()
    city = input("City: ").strip().capitalize()
    pin_no= input("Pincode: ").strip()
    pin=int()
    if pin_no.isnumeric():
        if len(pin_no)==6:
            pin= pin_no
        else:
            print("Invalid input!!! PIN No. must be 6 numbers.")
    else:
        print("Invalid input!!! PIN No. must be numerical value.")
    stu_data = {
        "id": student_id,
        "name": {"first": first_name, "last": last_name},
        "course": course,
        "semester": semester,
        "marks": marks,
        "address": [house, street, city, pin]
    }
    students.append(stu_data)
    print("Congratulation! Student added successfully.")

def ser_by_id():
    stu_id = input("Enter the Id: ").strip().upper()
    for student in students:
        if student["id"] == stu_id:
            print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:", student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}")
            return
    print("Sorry! No student found by this ID.")

def ser_by_name():
    first = input("Enter first name: ").strip()
    last = input("Enter last name: ").strip()
    found = False
    for student in students:
        if first.capitalize() in student["name"]["first"] and last.capitalize() in student["name"]["last"]:
            print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:", student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}","\n")
            found = True
    if not found:
        print("Sorry! No student found by this name.")

def ser_by_course():
    cou = input("Enter the course: ").strip().upper()
    found = False
    for student in students:
        if cou in student["course"]:
            print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:", student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}","\n")
            found = True
    if not found:
        print("Sorry! No student found in this course.")

def ser_by_sem():
    while True:
        sem_al = input("Semester ('1' to '8'): ").strip()
        if sem_al.isnumeric():
            sem = int(sem_al)
            break
        else:
            print("Only numerical value is allowed.")
    for x in range(500):
        if sem>=1 and sem<=8 :
            semester= sem
            break
        else:
            print("Semester must be 1 to 8.")
            while True:
                sem_al = input("Semester ('1' to '8'): ").strip()
                if sem_al.isnumeric():
                    sem = int(sem_al)
                    break
                else:
                    print("Only numerical value is allowed.")
    found = False
    for student in students:
        if sem in student["semester"]:
            print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:", student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}","\n")
            found = True
    if not found:
        print("Sorry! No student found in this course.")

def ser_by_city():
    ci = input("Enter the city: ").strip().capitalize()
    found = False
    for student in students:
        if ci == student["address"][2]:
            print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:",student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}","\n")
            found = True
    if not found:
        print("Sorry! No student found in this city.")

def ser_by_marks():
    sub = input("Enter the subject: ").strip().capitalize()  
    while True:
        mark = input("Enter the marks threshold: ").strip()
        if mark.isnumeric():
            mar= int(mark)
            break
        else:
            print("Only numerical value is allowed.")
    a_b = input("Enter 'above' or 'below'. What do you want to see? ").strip().lower()
    
    found = False
    for student in students:
        if sub in student["marks"]:
            if (a_b == "above" and student["marks"][sub] >= mar) or (a_b == "below" and student["marks"][sub] <= mar):
                print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:", student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}","\n")
                found = True
    
    if not found:
        print("No students found matching this criteria.")

def show_all():
    if students:
        print(">>> Showing all students records...")
        for student in students:
            print("{\nId:",student["id"],\
                    "\nName:",student["name"]["first"],student["name"]["last"], \
                    "\nCourse:",student["course"], \
                    "\nSemester:", student["semester"], \
                    "\nMarks:",student["marks"], \
                    "\nAddress:-", \
                    "\n     House:",student["address"][0], \
                    "\n     Sreet:",student["address"][1], \
                    "\n     City:",student["address"][2], \
                    "\n     PIN No.:",student["address"][3], \
                    "\n}","\n")
    else:
        print("No student records found.")

def top_scorer():
    subject = input("Enter the subject: ").strip().capitalize()
    top = None
    
    for student in students:
        if subject in student["marks"]:
            if top is None or student["marks"][subject] > top["marks"][subject]:
                top = student
    
    if top:
        print(f"Top scorer in {subject} is {top['name']['first']} {top['name']['last']} with {top['marks'][subject]} marks.")
    else:
        print(f"No student has marks in {subject}.")

def re_name():
    id= input("Enter the id: ").upper().strip()
    for student in students:
        if id== student["id"]:
            print("Enter the new name:-")
            first= input("First Name: ").capitalize().strip()
            for x in first:
                if first.isalpha():
                    student["name"]["first"] = first
                    break
                else:
                    print("First name must be alphabetic.")
                    first = input("First name: ").strip().capitalize()
            last = input("Last name: ").strip().capitalize()
            for x in last:
                if last.isalpha():
                    student["name"]["last"] = last
                    break
                else:
                    print("Last name must be alphabetic.")
                    last = input("Last name: ").strip().capitalize()
            return
    print("Sorry! No student found by this ID.")

def re_course():
    id= input("Enter the id: ").upper().strip()
    for student in students:
        if id== student["id"]:
            student["course"]= input("Enter the new course name: ").upper().strip()
            return
    print("Sorry! No student found by this ID.")

def re_sem():
    id= input("Enter the id: ").upper().strip()
    for student in students:
        if id== student["id"]:
            while True:
                sem_al = input("Semester ('1' to '8'): ").strip()
                if sem_al.isnumeric():
                    sem = int(sem_al)
                    break
                else:
                    print("Only numerical value is allowed.")
            for x in range(500):
                    if sem>=1 and sem<=8 :
                        semester= sem
                        break
                    else:
                        print("Semester must be 1 to 8.")
                        while True:
                            sem_al = input("Semester ('1' to '8'): ").strip()
                            if sem_al.isnumeric():
                                sem = int(sem_al)
                                break
                            else:
                                print("Only numerical value is allowed.")
            return
    print("Sorry! No student found by this ID.")

def re_num():
    id= input("Enter the id: ").upper().strip()
    while True:
        sub1 = input("Enter the subject to change number: ").capitalize().strip()
        if sub1.isalpha():
            sub = sub1
            break
        else:
            print("Subject must be alphbetic.")

    for student in students:
        if id == student["id"]:
            if sub in student["marks"]:
                while True:
                    num_al=input("Enter the new number: ").strip()
                    if num_al.isnumeric():
                        num =int(num_al)
                        break
                    else:
                        print("Only numerical value is allowed.")
                    for x in num:
                        student["marks"][sub]= num
                        break
            else:
                print("Sorry! This student has not any subject by this name.")
            return
    print("Sorry! No student found by this ID.")

def re_sub():
    id= input("Enter the id: ").upper().strip()
    while True:
        sub1= input("Enter the subject to change: ").capitalize().strip()
        if sub1.isalpha():
            sub = sub1
            break
        else:
            print("Subject must be alphabetic.")
    while True:
        sub2= input("Enter the new subject: ").capitalize().strip()
        if sub1.isalpha():
            n_sub = sub1
            break
        else:
            print("Subject must be alphabetic.")

    while True:
        num_al=input("Enter the number: ").strip()
        if num_al.isnumeric():
                num =int(num_al)
                break
        else:
            print("Only numerical value is allowed.")
    a=0
    for student in students:
        if id== student["id"]:
            do=student["marks"]
            if sub in do:
                do[n_sub]=num
                del do[sub]
            else:
                print("Sorry! This student has not any subject by this name.")
            return
    print("Sorry! No student found by this ID.")

def re_marks():
    while True:
        print("1. Rename only number of specific subject." \
          "\n2. Rename subject."
          "\n0. Exit.")
        choice= input("Enter the choice: ").strip()
        if choice== "1":
            re_num()
        elif choice== "2":
            re_sub()
        elif choice == "0":
            print("Exiting.....")
            break
        else:
            print("Invalid choice! Please try again.")

def re_add():
    id= input("Enter the id: ").upper().strip()
    for student in students:
        if id== student["id"]:
            print("Enter the new address:-")
            student["address"][0]= input("House: ").upper().strip()
            student["address"][1]= input("Street: ").capitalize().strip()
            student["address"][2]= input("City: ").capitalize().strip()
            pin_no= input("PIN No.: ").strip()
            for x in pin_no:
                if pin_no.isnumeric():
                    if len(pin_no)==6:
                        student["address"][3] = pin_no
                        break
                    else:
                        print("Invalid input!!! PIN No. must be 6 numbers.")
                        pin_no= input("PIN No.: ").strip()
                else:
                    print("Invalid input!!! PIN No. must be numeric value.")
                    pin_no= input("PIN No.: ").strip()
            return
    print("Sorry! No student found by this ID.")

def rem():
    id = input("Enter the id:").strip().upper()
    for student in students:
        if id == student["id"]:
            w=students.index(student)
            del students[w]
            break
        else:
            print("Please try again! Student id does not found.")

def main_menu1():
    while True:    
        print(">>> Search any student.")
        print("1. Search by Student ID")
        print("2. Search by Name")
        print("3. Search by Course")
        print("4. Search by Semester")
        print("5. Search by City")
        print("6. Search by Marks (above/below)")
        print("0. Back to main manu")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            ser_by_id()
        elif choice == "2":
            ser_by_name()
        elif choice == "3":
            ser_by_course()
        elif choice== "4":
            ser_by_sem()
        elif choice == "5":
            ser_by_city()
        elif choice == "6":
            ser_by_marks()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

def main_menu2():
    while True:
        print(">>> Edit any student imformation." \
        "\n1. Rename any students name" \
        "\n2. Change the course name" \
        "\n3. Change the semester name of any student" \
        "\n4. Change the number of any subject of any student" \
        "\n5. Change the address of any student" \
        "\n0. back to main manu")
        
        choice = input("Enter the choice: ").strip()
        
        if choice == "1":
            re_name()
        elif choice == "2":
            re_course()
        elif choice =="3":
            re_sem()
        elif choice == "4":
            re_marks()
        elif choice == "5":
            re_add()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

def main_menu():
    while True:
        print(">>> Main Menu" \
        "\n1. Add Student." \
        "\n2. Search Any Student." \
        "\n3. Edit Student Imformation." \
        "\n4. Show All Students Data." \
        "\n5. Find Top Scorer in Subject." \
        "\n6. Remove any student imformation." \
        "\n0. Exit")
        choice= input("Enter what you want to do: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            main_menu1()
        elif choice == "3":
            main_menu2()
        elif choice == "4":
            show_all()
        elif choice == "5":
            top_scorer()
        elif choice == "6":
            rem()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

os.system("cls")
print("University Student Record Management System:-")
main_menu()