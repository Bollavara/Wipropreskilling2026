import re
emp_id="EMP123"
result=re.match(r"^EMP\d{3}",emp_id)
if result:
    print("Valid Employee ID")
else:
    print("Invalid Employee ID")

text=