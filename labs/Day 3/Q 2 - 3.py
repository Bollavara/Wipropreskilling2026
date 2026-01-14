def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as file:
            for i in range(1, 11):
                file.write(str(i) + "\n")

        print("File written successfully")

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print("Unexpected error:", e)

write_numbers_to_file("numbers.txt")
