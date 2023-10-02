"""
    <name: Alcarmen, Brandon V.>
    <schedule: MW 9:00-10:30 AM>
    <edpcode: 13953>
	create a file 'student.txt', read, write and update this file
	for the student list
	Create the student list with a menu provided below
	----------- Student List -----------
    1. Add Student
    2. Find Student
    3. Delete Student
    4. Update Student
    5. Display All Student
    0. Quit/End
    ------------------------------------
    Enter Option(0..5):
    sample student entry below
    
    student:dict = {
        'idno':'0001',
        'lastname':'alpha',
        'firstname':'bravo',
        'course':'bsit',
        'level':'3',
    }
"""
from os import system

def checks(ID):
    return ID.isdigit()
def Add()->None:
    system("cls")
    print("== ADD student ==")
    checker = False

    while True:
        ID = input("Enter ID: ")

        if checks(ID):
            students_file = "student.txt"
            with open(students_file, "r") as file:
                for line in file:
                    if str(ID) in line:
                        print()
                        print("Student ID already exists\n")
                        print("Returning\n")
                        return ID

            if not checker:
                with open("student.txt", "a") as student_file:
                    last_name = input("Enter Last Name: ")
                    first_name = input("Enter First Name: ")
                    course = input("Enter Course: ")
                    level = input("Enter Level: ")

                    student = {
                        'idno:': ID,
                        'Last name:': last_name,
                        'First name:': first_name,
                        'Course:': course,
                        'Level:': level
                    }

                    student_file.write(f"{student['idno:']}\t{student['First name:']}\t{student['Last name:']}\t{student['Course:']}\t{student['Level:']}\n")
                break
        else:
            print("\nPlease enter numbers in ID.")
   
    

def Find()->None:
    system("cls")
    print("==Find Student Page==")
    found = False
    search = input("Enter Search: ")
    students_file = "student.txt" 
    
    with open(students_file, "r") as find:
        for line in find:
            if search in line:
                print("Student Found:", line)
                found = True
    if not found:
        print("Student doesn't exist.")
    
    

def Delete()->None:
    system("cls")
    print("==Delete Student Page==")
    found = False
    store = []  
    students = "student.txt"  

    remove= input("Enter the student name to delete: ")
    store = []
    if remove != "":  
        print()
        decide = input("=Delete Confirmation=\n Do you really want to delete:?(Y/N) ")
        if decide == "Y" or decide == 'y':
            with open(students, "r") as find:
                for line in find:
                    if remove in line:
                        print(f"Student Found: {line}")
                        found = True
                    else:
                        store.append(line)
            if not found:
                print("==Error==")
                print("Student not found.")
            else:
                with open(students, "w") as find:
                    find.writelines(store)
                print(f"Delete confirmed")
                print(f"Student '{remove}' has been deleted.")
                print()
        else:
            print()
            print("Cancel.")
            print("Return..\n")
    else:
        print()
        print("Invalid.")
     
def Update()->None:
    system("cls")
    print("==Update Page==")
    students = "student.txt"
    try:
        ID = input("Enter student ID number to update:")
        if checks(ID):
            agree = input("Are you really sure?(Y/N): ")
            if agree == "Y" or agree == 'y':
                FName = input ("Enter First Name: ")
                LName = input ("Enter Last Name: ")
                Course= input ("Enter Course/Program: ")
                Level= input ("Enter Level: ") 
                with open(students) as check:
                    lines = check.readlines()
                if 1 <= int(ID) <= len(lines):
                    lines[int(ID) - 1] = f"{ID},{FName},{LName},{Course},{Level}\n"

                    with open(students, "w") as check:
                        check.writelines(lines)
                else:
                    print("Invalid ID specified.")
            else:
                print()
                print("Update Cancel.")
                print("Return")            
        else:
            print("\nPlease input numbers in ID.")
            print("Return")
    except ValueError:
        print("\nPlease input Student's ID number") 
def DisplayAll()->None:
    system("cls")
    print("==Display student Page==")
    with open("student.txt", "r") as f:
        lines = f.readlines()

    print("==Display Student Profile==\n")
    print("ID:\tLast Name:\tFirst Name:\tCourse:\tLevel:")

    for line in lines:
        fields = line.strip().split('\t')
        if len(fields) >= 5:
            student_id, last_name, first_name, course, level = fields
            print(f"{student_id}\t{last_name}\t\t{first_name}\t\t{course}\t{level}")
        else:
            print("Invalid format in line:", line.strip())
    f.close()
    
def Quit()->None:
    system("cls")
    print("Program Ended...")
	


def displaymenu()->None:
	system("cls")
	Option:tuple=(
	"-------Student List Menu-------",
	"1. Add Student",
	"2. Find Student",
	"3. Delete Student",
	"4. Update Student",
	"5. Display All Student",
	"0. Exit",
	"--------------------------------"
	)
	[print(menu) for menu in Option]	
def main()->None:
	
	option:int = -1
	menuitems = {
		1:Add,
		2:Find,
		3:Delete,
		4:Update,
		5:DisplayAll,
		0:Quit
	}
	while option != 0:
		displaymenu()
		option=int(input("Enter option (0-5): "))
		menuitems.get(option)()

		input("Press any key to continue...")


if __name__=="__main__":
	main()