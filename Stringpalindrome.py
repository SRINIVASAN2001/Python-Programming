def isPalindrome(a):
    b=[]
    l=len(a)

    for i in range(l-1,0,-1):
        b.append(a[i])
    b.append(a[0])
    return b



a="string"
res=isPalindrome(a)
if res==a:
    print("Palindrome")
else:print("Not a Palindrome")
print(res)

