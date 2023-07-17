from numpy.core.defchararray import endswith

a="Ramu is my friend"

words=a.split()

l=len(words)-1
b=""

i=l
j=1
while i>=0:
        b=b+words[i]
        if i!=0:
            b=b+'*'*j
        i-=1
        j+=1
print(b)

