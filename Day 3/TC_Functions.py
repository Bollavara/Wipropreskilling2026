#basic syntax of python functions
def add(a,b):  #Definefirst
    print(a+b)

#Return Value - print
def sub(a,b):
    return a-b

add(10,20)
print(sub(100,20))

#can Return multiple values - print
def sub(a,b):
    return a-b,a
print(sub(100,20))

def hello(greeting="Hello",name="world"):
    print('%s,%s'%(greeting,name))
hello() #default parameters will be used
hello('Greetings','Harika')

#Pass n number of parameters
def print_param(*params):
    print(params)
print_param('Testing')
print_param(1,2,3,4)

#Named parameters passing
def print_param1(**params):
    print(params)
print_param1(x=1,y=2,z=3)


