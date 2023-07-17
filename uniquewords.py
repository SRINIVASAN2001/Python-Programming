def uniquewords(a):
    temp= []
    words=a.split()

    for w in words:
        if w not in temp:
            temp.append(w)

    return temp



a="hello is world hello"
res=uniquewords(a)

print(res,len(res))


