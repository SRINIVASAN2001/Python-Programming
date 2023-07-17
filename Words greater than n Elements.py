def ExtractWords(a,n):

    b=a.split()
    print(b)

    res =[x for x in b if len(x)>n]

    for w in res:
        print(w)


a="India is my country"
n=int(input("Enter the length:"))
ExtractWords(a,n)