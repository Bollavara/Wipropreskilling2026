#No implementation in Abstraction
#Abstract class can have both abstract method and normal method
#But normal class don't have abstract method, it only has normal method
from abc import ABC,abstractmethod

class shape(ABC): #if remove ABC it will be normal method
    def display(self):
        print("normal method")
    @abstractmethod
    def area(self):
        pass #python won't allow empty blocks
#Can't directly create/implement
#a=shape()
#a.area()
#using inheritance
class rectangle(shape):
    def area(self):
        print("area method implemented")

r=rectangle()
r.area()
r.display()





