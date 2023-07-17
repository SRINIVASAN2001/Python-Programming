def isPrime(num):

    count=0

    i=1
    while i<num+1:
        if num%i==0:
            count+=1
        i+=1
    if count==2:
        print("Its a prime number:",num)
    else:
        print("Not a prime number:",num)



num=int(input("enter the number:"))
isPrime(num)
