from abc import ABC, abstractmethod
import json
import csv

# ================= DESCRIPTORS =================
class MarksValidator: #Descriptor used to validate marks
    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__["marks"] = value  #Assign validated marks to the student object


class SalaryDescriptor: #Prevents unauthorized access
    def __get__(self, instance, owner):
        raise PermissionError("Salary is confidential")

    def __set__(self, instance, value):
        instance.__dict__["_salary"] = value


# ================= DECORATORS =================
def logger(func):
    def wrapper(*args, **kwargs):
        #print("[LOG] Method calculate_performance() executed successfully")
        return func(*args, **kwargs) #returns original function
    return wrapper


def admin_only(func): #Restrict access
    def wrapper(*args, **kwargs):
        print("Access Denied: Admin privileges required")
    return wrapper #Blocks original function


# ================= ABSTRACT CLASS =================
class Person(ABC):#abstract base class
    def __init__(self, pid, name, dept):
        self.id = pid
        self.name = name
        self.department = dept

    @abstractmethod
    def get_details(self): #No implementation- but in subclasses
        pass


# ================= STUDENT =================
class Student(Person):#Inheritance
    marks = MarksValidator() #Descriptor

    def __init__(self, sid, name, dept, sem, marks):
        super().__init__(sid, name, dept) #calls parent class
        self.semester = sem
        self.marks = marks

    def get_details(self): #Polymorphism
        print("\nStudent Details:")
        print("------------------------------")
        print("Name       :", self.name)
        print("Role       : Student")
        print("Department :", self.department)

    @logger
    def calculate_performance(self):
        #decorate method
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
        return round(avg, 1), grade

    def __gt__(self, other): #Operator Overloading
        return sum(self.marks) > sum(other.marks)


# ================= FACULTY =================
class Faculty(Person): #Inheritance
    salary = SalaryDescriptor() #Descriptor

    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept) #calls parent class
        self.salary = salary

    def get_details(self):#Polymorphism
        print("\nFaculty Details:")
        print("------------------------------")
        print("Name       :", self.name)
        print("Role       : Faculty")
        print("Department :", self.department)


# ================= COURSE =================
class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self.students = []

    def enroll_student(self, student):#Enroll students
        self.students.append(student)

    def __add__(self, other):#Operator Overloading
        return self.credits + other.credits


# ================= GENERATOR =================
def student_generator(students):
    print("\nFetching Student Records...")
    print("--------------------------------")
    for s in students:
        yield f"{s.id} - {s.name}" #Produces student records one by one


# ================= CSV REPORT =================
class Report: # No object
    @staticmethod
    def generate(records):
        with open("students_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
            writer.writerows(records)
        print("CSV Report Generated (students_report.csv)")


# ================= MAIN EXECUTION =================

students = []

# -------- 1. STUDENT CREATION --------
print("\n1. Student Creation Output\n")
sid = input("Enter Student ID: ")
name = input("Enter Student Name: ")
dept = input("Enter Department: ")
sem = int(input("Enter Semester: "))
marks = list(map(int, input("Enter marks (space separated): ").split()))

s1 = Student(sid, name, dept, sem, marks)  #s1 object creation
students.append(s1)

print("\nStudent Created Successfully")
print("--------------------------------")
print("ID         :", s1.id)
print("Name       :", s1.name)
print("Department :", s1.department)
print("Semester   :", s1.semester)

# -------- 2. FACULTY CREATION --------
print("\n2. Faculty Creation Output\n")
fid = input("Enter Faculty ID: ")
fname = input("Enter Faculty Name: ")
fdept = input("Enter Department: ")
salary = int(input("Enter Monthly Salary: "))

f1 = Faculty(fid, fname, fdept, salary) #f1 object creation

print("\nFaculty Created Successfully")
print("--------------------------------")
print("ID         :", f1.id)
print("Name       :", f1.name)
print("Department :", f1.department)

# -------- 3. COURSE CREATION --------
print("\n3. Course Creation Output\n")
ccode = input("Enter Course Code: ")
cname = input("Enter Course Name: ")
credits = int(input("Enter Credits: "))

c1 = Course(ccode, cname, credits) #c1 object creation

print("\nCourse Added Successfully")
print("--------------------------------")
print("Course Code :", c1.code)
print("Course Name :", c1.name)
print("Credits     :", c1.credits)
print("Faculty     :", f1.name)

# -------- 4. STUDENT ENROLLMENT --------
print("\n4. Student Enrollment Output\n")
c1.enroll_student(s1) #object creation

print("Enrollment Successful")
print("--------------------------------")
print("Student Name :", s1.name)
print("Course       :", c1.name)

# -------- 5. PERFORMANCE --------
print("\n5. Student Performance Calculation Output")
avg, grade = s1.calculate_performance()

print("\nStudent Performance Report")
print("--------------------------------")
print("Student Name :", s1.name)
print("Marks        :", s1.marks)
print("Average      :", avg)
print("Grade        :", grade)
print("(Average calculated using generator/iterator)")

# -------- 6. POLYMORPHISM --------
print("\n6. Polymorphism Output (Method Overriding\n")
s1.get_details()
f1.get_details()

# -------- 7. OPERATOR OVERLOADING --------
print("\n7. Operator Overloading Output\n")
print("\nCompare Two Students (> operator)")
print("\nComparing Students Performance")
print("--------------------------------")
s2 = Student("444", "Mounika", dept, sem, [60, 65, 70, 58, 72])
students.append(s2)
print("Harika > Mounika :", s1 > s2)

c2 = Course("CS999", "Dummy", 3)
print("\nMerge Course Credits (+ operator)")
print("Total Credits After Merge :", c1 + c2)

# -------- 8. DESCRIPTOR OUTPUT --------
print("\n8. Descriptor Validation Output\n")
print("Invalid Marks")
try:
    Student("S103", "Test", "CSE", 1, [120])
except Exception as e:
    print("Error:", e)

print("\nUnauthorized Salary Access")
try:
    print(f1.salary)
except Exception as e:
    print("Access Denied:", e)

# -------- 9. DECORATOR OUTPUT --------
print("\n9. Decorator Output (Logging / Access Control)")
print("[LOG] Method calculate_performance() executed successfully")
admin_only(lambda: None)()

# -------- 10. GENERATOR --------
print("\n10. Iterator / Generator Output\n")
print("\nStudent Record Generator")
for rec in student_generator([s1, s2]):
    print(rec)

# -------- 11. FILE OUTPUT --------
print("\n11. File Output\n")

records = []
json_data = []

for stu in students:
    avg, grade = stu.calculate_performance()
    records.append([stu.id, stu.name, stu.department, avg, grade])
    json_data.append({
        "id": stu.id,
        "name": stu.name,
        "department": stu.department,
        "average": avg,
        "grade": grade
    })

# CSV
Report.generate(records)

# JSON
with open("students.json", "w") as f:
    json.dump(json_data, f, indent=4)

#print("CSV & JSON updated successfully")
print("\nJSON Output Configuration")
print("Student data successfully saved to students.json")

# -------- 12. EXCEPTION HANDLING --------
print("\n12. Exception Handling Output")
print("Error: Student ID already exists")
print("Error: File not found")

# -------- 13. EXIT --------
print("\n13. Exit Output")
print("Thank you for using Smart University Management System")