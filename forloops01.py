nums = [ 1,4,9,16,25,36,49,64,81,100]
for vals in nums:
    print(vals)

tups = [ 1,4,9,16,25,36,49,64,81,100,25]
x = 25

idx = 0
for vals in tups:
    if (vals == x):
        print("tups found at idx", idx)
    idx += 1
