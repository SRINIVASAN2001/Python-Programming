def N_max_elements(arr,num):
    arr.sort()
    print(arr)
    brr=[]
    i=1
    l=len(arr)
    while i<num+1:
        brr.append(arr[l-i])
        i+=1
    print(brr)

arr=[1,2,3,5,7,1.5,10,16]
num=int(input("enter the number"))

N_max_elements(arr,num)