i = 3
j = 5

i_values = []
j_values = []

while i <= 50:
    i_values.append(i)
    i = i + 1

while j <= 25:
    j_values.append(j)
    j = j + 2

print("i values:", i_values)
print("j values:", j_values)


if i % 2 != 0:
    print("Final i is ODD")
else:
    print("Final i is EVEN")
    

