a=int(input("Enter num 1: "))
b=int(input("Enter num 2: "))
while a !=b:
    if a>b:
        a-=b
    else:
        b-=a
print("The answer is: " + str(b))