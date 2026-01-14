import json

data={
    "name":"Harika",
    "Age":22,
    "Skills":["python","java"]
}

with open("data.json","w") as file:
    json.dump(data,file,indent=4)