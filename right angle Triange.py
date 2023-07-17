n=int(input("Enter the no.of Rows:\n"))

for row in range(n):
    for col in range(row+1):
        print("*",end="")
    print()
