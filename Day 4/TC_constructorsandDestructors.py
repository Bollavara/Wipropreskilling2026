class employee:
    def __init__(self,name):
        self.name=name
        print("Constructor is called")
#Destructing
    def __del__(self):
        print("Destructor is called")

e=employee("Harika")