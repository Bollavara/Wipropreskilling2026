#3. Demonstrate the difference between using the iterator and generator
# by printing values using a for loop

class number:

    def __init__(self,limit):
        self.limit=limit
        self.current=1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<=self.limit:
            val=self.current
            self.current+=1
            return val
        else:
            raise StopIteration

def fibonacci(n):
    a,b=0,1
    c=0
    while c<n:
        yield a
        a,b=b,a+b
        c+=1
print("Iterator")
obj=number(5)
for num in obj:
    print(num)
print("Generator")
for num in fibonacci(10):
    print(num)