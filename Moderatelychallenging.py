class Person():
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    
    def getName(self): 
        return self.__name
    
    def getAddress(self):
        return self.__address
    
    def setAddress(self, address):
        self.__address = address

    def __str__(self):
        return self.getName() + '(' + self.getAddress() + ')'

class Student(Person):
    def __init__(self, name, address, numCourses = 0, courses = [], grades = []):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.__courses = courses
        self.__grades = grades
    
    def addCourseGrade(self, course, grade):
        self.__courses.append(course)
        self.__grades.append(grade)

    def printGrades(self):
        print(self.__grades)

    def AverageGrade(self):
        return(sum(self.__grades)/len(self.__grades))

    def __str__(self):
        return 'Student: ' + self.getName() + '(' + self.getAddress() + ')'

class Teacher(Person):

    def __init__(self, name, address, numCourse =  0, courses  = []):
        super().__init__(name, address)
        self.__numCourse = numCourse
        self.__courses = courses

    def addCourse(self, course):
        for courses in self.__courses:
            if course == courses:
                return False
        self.__courses.append(course)
        return True
    
    def removeCourse(self, course):
        if course in self.__courses:
            self.__courses.remove(course)
            return True
        else:
            return False

    def __str__(self):
        return 'Student: ' + self.getName() + '(' + self.getAddress() + ')'


            


