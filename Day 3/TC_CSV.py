
import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","ID","Age"])
    writer.writerow(["Harika",1,22])
    writer.writerow(["Vandana", 2, 22])
    writer.writerow(["Mounika", 3, 18])