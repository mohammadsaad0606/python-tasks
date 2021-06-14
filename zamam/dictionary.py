data = {"Scott":1,"John Wick":2,"Klaus":3,"Bruce":4,"Justice League":{"Clark":1,"Bruce":2,"Diana":3,"Barry":4,"Arthur":5}}

for i in data:
    print(i)

for i in data.keys():
    print(i)

for i in data.values():
    print(i)

for i in data.items():
    print(i)

for i,j in data.items():
    print(f"{i} is {j} GOAT")

faraz = {key:value for (key,value) in data.items()}

print(faraz)
