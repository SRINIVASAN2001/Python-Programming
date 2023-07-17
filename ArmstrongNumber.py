import math


def count(n):

    l=n
    count=0
    while l>0:
        count+=1
        l=l//10
    return count

def Armstrong(n):

    temp=n
    digit=count(n)
    print("Enter the count of Digit:",digit)
    sum=0

    while temp>0:
        rem=temp%10
        sum=sum+math.pow(rem,digit)
        temp=temp//10

    return sum

n=int(input("Enter the number:\n"))
print("Your number:",n)
res=Armstrong(n)

if (res==n):
    print("Armstrong number")
else: print("Not a Armstrong number")

