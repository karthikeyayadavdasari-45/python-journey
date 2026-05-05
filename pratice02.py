#prime number
num = int(input("enter a number:"))
if num > 1:
    for i in range(2, int(num**0.5) +1):
        if num % i == 0:
            print("not prime")
            break
    else:
            print("prime")
else:
        print("not prime")        



