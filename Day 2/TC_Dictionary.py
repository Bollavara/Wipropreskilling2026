student={
    "name": "Rahul",
    "age":20,
    "Course": "Python"

}
print(student)
print(student["name"])
print(student.get("age"))
#update age
student["Marks"]=85
student["age"]=25
print(student)
print(student["name"])
print(student.get("age"))
student.pop("age")
print(student)
student.popitem()
print(student)

#only keys
print(student.keys())
print(student.values())

#for loop
for key in student:s
    print(key,student[key])

# to check
if "name" in student:
    print("key exists")

#Nested Dictionary
employees={

    101:{"name":"Harika","salary":20000},
    102:{"name":"Harika","salary":20000}
}
print(employees[101]["name"])



