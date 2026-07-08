#zig zag 
n = 9
for i in range(3):
    for j in range(n):
        if ((i + j) % 4 == 0) or (i == 1 and j % 4 == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 14

# Upper Part
for i in range(n // 2, n + 1, 2):
    for j in range(1, n - i + 1, 2):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end="")

    for j in range(1, n - i + 1):
        print(" ", end="")

    for j in range(1, i + 1):
        print("*", end="")

    print()

# Lower Part
for i in range(n, 0, -1):
    for j in range(i, n):
        print(" ", end="")

    for j in range(1, (i * 2)):
        print("*", end="")

    print()