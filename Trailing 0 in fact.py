num=int(input("Enter the number: "))
fact=1
mod=10**9+7
ans=0
for i in range (2,num+1):
    fact*=i%mod
    if(fact>10):
        while(fact%10==0):
            fact=fact//10
            ans+=1
            
print("answer is:" + str(ans))
