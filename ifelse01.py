##
num = int(input("enter a number:"))

if num%2 == 0:
    print("even")
else:
    print("odd")


##
n = int(input("enter a number:"))
if n > 0:
    print("positive")    
elif n < 0:
    print("negative")    
else:
    print("zero")


##
marks = int(input("enter a marks: "))
if marks > 90:
    print("grade A")
elif marks > 75:
    print("grade B")
elif marks > 35:
    print("grade c")  
else:
    print("fail")     

#checking vowels
ch = "lowl"
if ch in "aeiou":
    print("vowels")
else:
    print("constants")   

###
num = 90
if num%5 ==0:
    print("divisible by 5")
else:
    print("not divisble by 5") 

###
num = 30
if num%3 == 0 and num%10 == 0:
    print("divisble by 3 and 10")
else:
    print("not divisble by both")  


temp = 30
if temp < 30:
    print("hot")
elif temp == 30:
    print("normal temp") 
else:
    print("cold")       



