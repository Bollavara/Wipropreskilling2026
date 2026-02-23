import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="database"
)

cursor = conn.cursor()
print("Connected successfully!\n")

# 1️⃣ Fetch employees with salary > 50000
print("Employees with salary > 50000:")

query_fetch = """
SELECT `employee id`, `employee name`, salary, department
FROM employee
WHERE salary > 50000
"""

cursor.execute(query_fetch)
results = cursor.fetchall()

for row in results:
    print(row)


# 2️⃣ Insert new employee
print("\nInserting new employee...")

query_insert = """
INSERT INTO employee (`employee id`, `employee name`, salary, department)
VALUES (%s, %s, %s, %s)
"""

new_employee = (105, "Verma", 80000, "IT")

cursor.execute(query_insert, new_employee)
conn.commit()

print("Inserted:", new_employee)


# 3️⃣ Update salary by 10%
print("\nUpdating salary by 10% for employee id = 105...")

query_update = """
UPDATE employee
SET salary = salary * 1.10
WHERE `employee id` = %s
"""

cursor.execute(query_update, (105,))
conn.commit()

print("Salary updated successfully!")

cursor.close()
conn.close()

print("\nConnection closed.")
