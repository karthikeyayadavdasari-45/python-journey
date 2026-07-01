rows = 10
for i  in range(rows):
    for j in range(rows -i -1):
        print("L", end="")
    for j in range(2*i +1):
        print("*", end="")
    print()    

# butterfly pattren
row = 7 
for i in range(1, row + 1):
    print("*" *i + ""*(2*(row -i)) + "*"*i)
for i in range(rows,0,-1):
    print("*"*i+""*(2*(rows -i))+"*"*i)    
