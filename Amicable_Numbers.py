n=int(input())
q=int(input())
s=0
p=0
for i in range(1,n):
    if n%i==0:
        s+=i
for j in range(1,q):
    if q%j==0:
        p+=j
if n==p and q==s:
    print("Amicable")
else:
    print("Not Amicable")