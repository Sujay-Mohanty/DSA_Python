n=int(input("Enter num : "))
ans=0
for i in range (2,int(n**0.5)+1):
    if(n%i==0):
        ans=1
if(ans==0):
    print("Prime")
else:
    print("Not Prime")

