i = 1
while i <= 30:
    print(3*i)
    i += 1

heroes =["vikram", " venky","noman","dharu"]
idx = 0
while idx < len(heroes):
    print(heroes[idx])
    idx +=1


nums = (1,4,5,6,10,56,100,45)

x = 5

i = 0
while i < len(nums):
    if (nums[i] == x):
      print("found at idx", i)
    i = i+1

i = 2
while i<= 10:
    print(i)
    if (i == 6):
        break
    i = i + 2
print("end of loop")

i = 1
while i<=15:
    if(i%2 != 0):
        i = i + 1
        continue
    print(i)
    i = i + 1
    

    

