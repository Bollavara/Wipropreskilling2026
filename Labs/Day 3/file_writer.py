#1. A module containing a function write_numbers_to_file(filename)
def write_numbers_to_file(filename):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Write numbers 1 through 10, each on a new line
        for num in range(1, 11):
            file.write(str(num) + "\n")
import Q 2 -1

# Call the function to write numbers to a text file
Q 2 - 1.write_numbers_to_file("numbers.txt")

print("Numbers written to numbers.txt successfully!")