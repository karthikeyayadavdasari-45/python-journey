#square pattern
rows = 5
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()    

#right triangle pattern
for i in range(7):
    for j in range(i + 1):
        print("+", end= "")
    print()    