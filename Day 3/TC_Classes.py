#Without Constructor
class student:
    name="Harika"
    age=22

#Create object for student
s1=student() #by using s1, accessing the objects
print(s1.name)
print(s1.age)

#With Constructor = __init__
class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age

e1=employee("Mounika",18)
print(e1.name,e1.age)

