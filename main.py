import math
def isArmstrong(n):
    sqrt=math.sqrt(n)
    temp=n
    count=0

    while(n>0):
        count+=1
        n=n//10

    sum=0
    for x in range(sqrt):
        sum=sum+math.pow(n%10,count)

n=int(input("Enter the number"))
res=isArmstrong(n)