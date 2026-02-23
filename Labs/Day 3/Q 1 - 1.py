import time
from functools import wraps

# Decorator to measure execution time
def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper


# Function to write numbers to a file
def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        for i in range(1, 11):
            file.write(str(i) + "\n")
    print("Numbers written to file successfully")


# Recursive factorial function with decorator
@execution_time
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Main program
result = factorial(5)
print("Factorial result:", result)

write_numbers_to_file("numbers.txt")
