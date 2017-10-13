#i dont have a remove a whole course


class Student:

    def __init__ (self,n,i):
        self.name=n
        self.id=i
        self.courses=[]
        self.grade=0
        self.gpa=0

    def editName(self,n):
        self.name=n

    def editId(self,i):
        self.id=i

    def addCourse(self,c):
        self.courses.append(c)

    def deleteCourse(self,c):
        self.courses.remove(c)

    def getGPA(totalscore,totalunits):
        self.GPA= totalscore/totalunits

class Course:
        
        def __init__(self,c,u):
            self.students=[]
            self.code=c
            self.unit=u
            self.grades=[]
        



        def editCode(self,c):
            if(len(c)==7):
                self.code=c
        
        def editUnit(self,u):
            self.unit=u

        def addStudent(self,student):
            self.students.append(student)

        def deleteStudent(self,student):
            self.students.remove(student)

def menu():
    i=int(input("0-STUDENT command\n1-COURSE command\n2-EXIT\n" ))
    while(i<=-1 and i>=2):
        print("you have entered an INVALID option")
        i=int(input("0-STUDENT command\n1-COURSE command\n2-EXIT\n" ))
    return i
        

def StudentMenu(allStudents,cStudent):
    found=False
    i=int(input("0-Create Student\n1-View Students\n2-back\n"))
    while(i<0 and i>2):
        print("you have entered and INVALID option")
        i=int(input("0-Create Student\n1-View Students and select Student\n2-back\n"))
    if(i==0):
            n =input("enter name please T_T\n")
            studentId= int(input ("ENTER ID NUMBER LODI\n"))
            while( studentId<10000000 or studentId>=100000000):
                    studentId= int(input ("ENTER ID NUMBER LODI\n"))
            kid=Student(n,studentId)
            cStudent=kid
            allStudents.append(cStudent)
    elif(i==1):
            ctr=0
            for x in allStudents:
                print(x.name + "\n" + str(x.id)+"\n")
            sName= input("please enter student's name ")
            for x in allStudents:
                if(sName==x.name):
                    cStudent=x
                    found=True
                    return ctr
                ctr+=1
            if(found==False):
                print("no name was found")
                return 2
    elif(i==2):
            return -1
    return -2
                    

def StudentMenu2(allCourses,cStudent):
    found=False
    i=int(input("0-add Course\n1-Remove Course\n2-editName\n3-Edit ID\n4-ALL view courses\n5 view current student's courses \n6- back\n"))
    if(i==0):
        subject=input("PLEASE ENTER THE NAME OF THE COURSE LODI :D ")
        for x in allCourses:
            if(x.code==subject):
                cStudent.addCourse(x)
                x.addStudent(cStudent)
                print("course has been added ")
                found=True
                return 2
            if(found==False):
                print("INVALID COURSE CODE ") 
    elif(i==1):
        subject=input("PLEASE ENTER THE NAME OF THE COURSE LODI :D")
        for x in cStudent.courses:
            if(x.code==subject):
                cStudent.deleteCourse(x)
                x.deleteStudent(cStudent)
                
    elif(i==2):
        n=input("enter new name\n")
        cStudent.editName(n)
    elif(i==3):
        n=input("enter new ID\n")
        cStudent.editId(n)
    elif(i==4):
        for x in allCourses:
            print(x.code)
    elif(i==5):
        for x in cStudent.courses:
            print(x.code)
    elif(i==6):
        return -1
    return 1

def StudentMenu3(cStudent,AllCourses):
    i= int(input("0-set Grade\n1 view grades\n2 get gpa\n3 back"))
    if(i==0):
        score= int(input("enter GRADE "))
        while(score<0 or score>100):
                   score= int(input("enter a valid grade"))
        cStudent.grade=score
    elif(i==1):
        print(cStudent.name+"\n")
        for x in AllCourse:
            for y in x.students:
                if(cStudent.name==y.name):
                    print(x.name+": "+y.grade)
    elif(i==2):
        totalunits=0
        totalgrade=0
        print(cStudent.name+"\n")
        for x in AllCourse:
            for y in x.students:
                if(cStudent.name==y.name):
                    totalgrade+=y.grade
                    totalunits+= x.unit
        print("GPA :"+cStudent.getGPA(totalgrade,totalunits))
    elif(i==3):
        return 0
    return 1
                   

    
def CourseMenu(allCourses,cCourse):
    ctr=0
    i=int(input("0-Create Course\n1-View Course and select Course\n2-back\n"))
    while(i<0 and i>2):
        print("you have entered and INVALID option ")
        i=int(input("0-Create Student\n1-View Students\n21-back\n"))
    if(i==0):
        cCode= input("please enter the course name for more werpah: ")
        cUnits= int(input("please enter the units of the course for a petmalu term: "))
        while(len(cCode)!=7 and 0>=cUnits>=4):
            print(" the code you have entered is invalid lodi")
            cCode= input("please enter the course name for more werpah")
            cUnits= int(input("please enter the units of the course for a petmalu term"))
        subject=Course(cCode,cUnits)
        cCourse=subject
        allCourses.append(cCourse)
    elif(i==1):
        for x in allCourses:
            print(x.code+"\n"+str(x.unit)+"\n")
        cCode= input("enter name of course code")
        for x in allCourses:
            if(x.code==cCode):
                cCourse=x
                print("PETMALU Course has been selected")
                return ctr
            ctr+=1
    elif(i==3):
        return -1
    return -2


def CourseMenu2(AllCourse,AllStudent,cCourse):
    found=False
    i=int(input("0-add Student\n1-Remove Student\n2-edit Course Code\n3-Edit units\n4 view Students in the course\n5 back\n"))
    if(i==0):
        sName =input("Enter name of student you wish to add on the Current course Lodi : ")
        for x in AllStudent:
            if(x.name==sName):
                cCourse.addStudent(x)
                x.addCourse(cCourse)
                found=True
        if(found==False):
            print("No Name was found")
    elif(i==1):
        sName =input("Enter name of student you wish to remove on the course LODI : ")
        for x in AllStudent:
            if(x.name==sName):
                cCourse.deleteStudent(x)
                x.deleteCourse(cCourse)
                found=True
        if(found==False):
            print("No Name was found")
    elif(i==2):
        cCode= input("enter new course code")
        cCourse.editCode(cCode)
        print("PETMALU course code has been changed")
    elif(i==3):
        cUnit= int(input("Enter the new number of units"))
        while(-1>=cUnits>=4):
            cUnit= int(input("Enter the new number of units"))
        print("PETMALU course unit has been changed")
        cCourse.editUnit(cUnit)
    elif(i==4):
        for x in cCourse.students:
            print(x.name+"\n")
        print("NAMES have been printed if\n no names was printed it means course is empty")
    elif(i==5):
        return 0
    return 1
                                    



                
AStudents=[]
currentStudent=Student("wew",11090954)
currentCourse=Course("CCSCAL1",3)
ACourse=[]
answer=1
while(answer!=2):
    answer=menu()
    if(answer==0):
        option=StudentMenu(AStudents,currentStudent)
        if(len(AStudents)>=1):
            currentStudent=AStudents[(len(AStudents)-1)]
        if(option==-2):
            option2=StudentMenu2(ACourse,currentStudent)
        elif(option>=0):
            currentStudent=AStudents[option]
            option2 =StudentMenu2(ACourse,currentStudent)
        elif(option==-1):
            answer=menu()
        if(option2==-1):
            option=StudentMenu(AStudents,currentStudent)
            currentStudent=AStudents[(len(AStudents)-1)]
        elif(option2>=0):
            option2=StudentMenu2(ACourse,currentStudent)
        elif(option2==-2):
            option3=StudentMenu3(currentStudent,ACourse)
            if(option3==0):
                option2=StudentMenu2(ACourse,currentStudent)
            elif(option3==1):
                option3=StudentMenu3(currentStudent,ACourse)
    elif(answer==1):
        cMenu =CourseMenu(ACourse,currentCourse)
        if(len(ACourse)>=1):
                currentCourse=ACourse[len(ACourse)-1]
        if(cMenu==-2):
            cMenu1=CourseMenu2(ACourse,AStudents,currentCourse)
        if(cMenu1==0):
            cMenu =CourseMenu(ACourse,currentCourse)
        if(len(ACourse)>=1):
            currentCourse=ACourse[len(ACourse)-1]
        if(cMenu>=0):
            currentCourse=ACourse[cMenu]
            cMenu1=CourseMenu2(ACourse,AStudents,currentCourse)
        if(cMenu==-1):
            answer=menu()

                
               
                
 

            
            
            
