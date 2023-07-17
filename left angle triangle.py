n=int(input("Enter the number:\n"))

for row in range(1,n+1):

    k=n-row+1
    for space in range(1,k):
        print(" ",end="")

    for col in range(1,row+1):
        print("*",end="")
    print()