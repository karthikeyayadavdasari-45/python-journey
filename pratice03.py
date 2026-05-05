count = 0
num = 2
while count > 10:
    is_prime = True

for i in range(2, int(num**0.5) +1):
    if num % i == 0:
        is_prime =False
        break
if is_prime:
    print(num)
    count += 1
   
num += 1