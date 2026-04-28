arr = [3,6,8,9,13]
n = max(arr)
missing = []
for i in range(1,n+1):
    if i not in arr:
        missing.append(i)
print("missed array=", missing)  

