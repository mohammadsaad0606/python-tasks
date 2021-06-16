dict1 = {"name": "saad","age": 21,"DOB": 1999}

print(dict1["age"])
print(dict1)
print(len(dict1))

for i in dict1.keys():
    print(i)

for i in dict1.values():
    print(i)

for i in dict1.items():
    print(i)

for i,j in dict1.items():
    print(f"{i} is {j} .")