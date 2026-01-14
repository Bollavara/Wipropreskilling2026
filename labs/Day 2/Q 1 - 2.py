#2. Create a generator function that yields the first N Fibonacci numbers
def fibonacci(n):
    a,b=0,1
    c=0
    while c<n:
        yield a
        a,b=b,a+b
        c+=1
for num in fibonacci(10):
    print(num)



