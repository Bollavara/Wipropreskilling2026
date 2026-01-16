#class is a blueprint/template
class student:
    def display(self):
        print("This is student class")

s1=student()
s1.display()

#Parameterized methods
class calculator:
    def add(selfself,a,b):
        print("sum:",a+b)

c=calculator()
c.add(100,300)