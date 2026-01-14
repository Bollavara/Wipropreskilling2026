def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        for num in range(1, 101):
            file.write(str(num) + "\n")

write_numbers_to_file("numbers.txt")

print("Numbers 1 to 100 written to file successfully!")
