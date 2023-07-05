a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))

def pow(x,y):
    res=1
    while y>0:
        if y%2 != 0:
            res=res*y
        x=x*x
        y=y//2
    return res

print("The result is:"+str(pow(a,b)))