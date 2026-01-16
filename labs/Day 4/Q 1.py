class student:
    def __init__(self,name,roll_no):  #attributes
        self.name=name
        self.roll_no=roll_no
    def display_details(self):  #Method display_details
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
s1=student("Harika",1) #objects
s2=student("Mounika",2)

s1.display_details() #Display details
s2.display_details()
