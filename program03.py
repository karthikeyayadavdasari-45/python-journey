#REVERSE ALL WORDS 
A = ["HOE", "super","prand","notolo","runesrs"]
print(A[::-1])

#PALINDROME CHECKER
A = [ 1,2,1,3,1]
if A == A[::-1]:
    print("palindrome")
else:
    print("not palindrome")    

#reverse middle part only 
C = [10,15,18,2,65,20,58]
X = C[:2]+C[2:5][::-1]+C[5:]
print(X)

#remove first and last element
A = ["word", "yadav","quantun"]
Y=A[1:-1]
print(Y)

# adding 2 lists 
A = [50,100,150,200]
B = [300,500,700,2500]
U = A[:4] + B[:4]
print("adding 2 lists", U)