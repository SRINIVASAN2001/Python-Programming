def longestword(string):

    words=string.split(" ")
    l=0
    w=""
    for word in words:
        if len(word)>l:
            w=word
            l=len(word)
    return w,l

string="Hello world srinivasan"
w,l=longestword(string)

print(f"word-->{w} and its length-->{l}")