import file_writer

filename = "numbers.txt"
try:
    file_writer.write_numbers_to_file(filename)
    with open(filename, "r") as file:
        print("File Content:\n")
        print(file.read())

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

except Exception as e:
    print("Unexpected error:", e)
