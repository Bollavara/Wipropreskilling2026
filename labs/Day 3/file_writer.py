#1. A module containing a function write_numbers_to_file(filename)
def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        for num in range(1, 11):
            file.write(str(num) + "\n")
import file_writer

file_writer.write_numbers_to_file("numbers.txt")

print("Numbers written to numbers.txt successfully!")



