# home room roster program 
# this program is designed to allow a teacher to:
# 1) See students in home room
# 2) add/remove students to homeroom
# 3) see basic info about students 

# create an object called student
class Student:
    def __init__(self,name,grade,ID,address,age,LockerNum):
        self.name = name
        self.grade = grade
        self.ID = ID
        self.address = address
        self.age = age
        self.LockerNum = LockerNum

List_of_homeroom_students = []

# functions
def Add_To_Homeroom():
    # create a new student object with the folowing properties: name,grade,ID,address,age,LockerNum
   
    print("Creating new student")
    print("what is there name")
    name = input("->")

    print("what is their grade")
    grade = input("->")

    print("what is their id number")
    number_ID = input("->")

    print("what is their address")
    address = input("->")

    print("what is their age")
    age = input("->")

    print("what is their locker number")
    LockerNum = input("->")
    
    # create a new student object with the folowing properties: name,grade,ID,address,age,LockerNum
    potato_of_the_baked_kind = Student(name,grade,number_ID,address,age,LockerNum)
    List_of_homeroom_students.append(potato_of_the_baked_kind)
    print(potato_of_the_baked_kind)
    print("created a student with the details below:")
    print("name:",potato_of_the_baked_kind.name)
    print("grade:",potato_of_the_baked_kind.grade)
    print("ID:",potato_of_the_baked_kind.ID)
    print("address:",potato_of_the_baked_kind.address)
    print("age:",potato_of_the_baked_kind.age)
    print("locker number:",potato_of_the_baked_kind.LockerNum)






def get_number_of_student():
    number = len(List_of_homeroom_students)
    return number 
def student_name():
    pass
def search_list_for_student():
    pass
def get_student_address():
    pass
def get_student_basic_info():
    pass
def list_homeroom_students():
    for french_fries in List_of_homeroom_students:
        print(french_fries.name)

# main code
while True:
    print("what would you like to do")
    print("1: view homeroom roster")
    print("2: add student to home room")
    print("3: remove student")
    print("4: get student id number")
    print("5: see number of students in homeroom")
    print("6: see basic student info")
    print("7: see if a student is on the home room list")
    print("8: EXIT")
    try:
        choice = int(input("->"))
        if choice == 1:
            #see list of students
            list_homeroom_students()
        elif choice == 2:
            #add student to home room  
            Add_To_Homeroom()
        elif choice == 3:
            #remove student
            pass
        elif choice == 4:
            #get student id number
            pass
        elif choice == 5:
            #see number of students in homeroom
            print(get_number_of_student())
        elif choice == 6:
            #see basic student info
            pass
        elif choice == 7:
            #see if a student is on the home room list
            pass
        elif choice == 8:
            #exit
            break
        else:
            print("ERR0R")
    except:
        print("number please")
print("thanks for using the homeroom software")
