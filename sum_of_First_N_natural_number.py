def squares(num):

    sum=0

    i=1
    while i<num+1:
        sum=sum+i**2
        i+=1
    return sum

num=int(input("Enter the natural number:\n"))
res=squares(num)
print(res)
