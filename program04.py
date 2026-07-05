#alphabet
n = 5
for i in range(n):
    ch = 65
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()

# Diamond pattern
n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))