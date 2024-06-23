
def add_course(courses : dict) :
    code, name, faculty, reg = input("Enter code, name, faculty, reg : ").split()
    reg = int(reg)
    courses[code] = [name, faculty, reg]
    pass


def print_details(courses : dict) :    
    if len(courses) == 0 :
        print("Course List is empty")
        return
    
    code = input("Enter course code ")
    if code in courses :
        details = courses[code]
        print(code,details[0], details[1], details[2])
        return

    print("Course with code", code, " doesn't exist")
    pass


def all_courses(courses : dict) :
    if len(courses) == 0 :
        print("Course List is empty")
        return
    
    print("\nAll Courses Are : ")
    for code, details in courses.items() :
        print(code, details[0], details[1], details[2])
    pass

def max_register(courses : dict) :
    if len(courses) == 0 :
        print("Course List is empty")
        return
    
    max_reg = 0
    for details in courses.values() :
        if details[2] > max_reg :
            max_reg = details[2]

    print("\nMax reg details")
    for code, details in courses.items() :
        if details[2] == max_reg :            
            print(code,details[0],details[1], details[2])

    pass


def main():
    courses = {"c0de001":  ["python",  "faculty1", 10],"c0de002":  ["python",  "faculty1", 20], "c0de003":  ["python",  "faculty1", 20] }
    menu = {1:add_course, 2:print_details, 3:all_courses, 4:max_register}
    while True :
        choice = int(input("\n(1)Add Course (2) print details (3)print Couses (4)Max reg (5)Exit\nEnter option >"))
        if(choice == 5) :
            return
        menu[choice](courses)



if __name__ == "__main__" :
    main()