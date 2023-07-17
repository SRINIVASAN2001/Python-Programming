def fibonacci(num):
    a=0
    b=1
    c=0
    temp=num

    if num==0:
        print(a)
    elif num==1:
        print(b)
    else:
        num = num - 2
        while num>0:
            c=a+b
            a=b
            b=c
            num-=1
    print("The Fibonacci value of",temp,"is:",c)
num=int(input("Enter the number:\n"))
fibonacci(num)