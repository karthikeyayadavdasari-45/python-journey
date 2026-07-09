height = 9

for layer in range(3):
    for i in range(height):
        spaces = height - i + (2 - layer)
        stars = 2 * i + 1 + layer * 2

        print(" " * spaces + "*" * stars)

for i in range(3):
    print(" " * (height + 2) + "|||")