#print largest element
arr = [ 20, 50,45,59,39]
max_val = arr[0]
for i in arr:
    if i > max_val:
        max_val = i
print("max=", max_val) 

#print smallest element
arr = [2007, 780,457,987,320]
min_val = arr[0]
for i in arr:
    if i < min_val:
        min_val = i

print("min=", min_val)
#count element
arr =[2,3,3,2,1,5,68,4,6,4,82,2,2,2,2]
num = 3
count = 0
for i in arr:
    if i == num:
        count += 1
print("countnum=", count)        