
def AddData(courses) :
    cc,cname,fac,num = input("Enter Course Code, Course Name, Faculty, Num of regs\n").split()
    num = int(num)
    courses[cc] = [cname,fac,num]

def HighestReg(courses:dict) :
    max = 0
    max_reg_course = []
    for key, val in courses.items() :
        if val[2] > max :
            max = val[2]

    for key, val in courses.items() :
        if val[2] == max :
            max_reg_course.append(key)
           
    for course_key in max_reg_course :
        print(courses[course_key])

def DisplayCourseDetails(courses) :
    if len(courses)==0:
        print("Courses dont exist")
        return
    ccode=input("Enter code: ")
    if ccode in courses:
        print(ccode,'   ', courses[ccode])
    else:
        print("No Course with that code")

def DispAllDetails(courses:dict) :
    if len(courses)==0:
        print("Courses dont exist")
        return
    print("Courses are: ")
    for x, y in courses.items():
        print(x,'   ',y)


def main() :
    courses ={"20CS43":["Python","PVT",20], "20CS42":["Math", "DIG",20], "20CS44":["DBMS", "DIG",24], "20CS45":["SE", "DIG",24], "20CS46":["Kan", "DIG",20] }
    courses = {}
    menuDict = {1:AddData, 2:HighestReg,3:DisplayCourseDetails,4:DispAllDetails}
    while True:
        choice = int(input("Enter 1.AddData 2.HighestRegistration 3.DisplayCourseDetails 4.DisplayAllDetails 5.Exit\n"))
        if choice == 5:
            break
        menuDict[choice](courses)
        
if __name__ == "__main__":
    main()
