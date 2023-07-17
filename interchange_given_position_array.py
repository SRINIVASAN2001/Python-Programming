def interchange(arr,first,second):
    arr[first-1],arr[second-1]=arr[second-1],arr[first-1]
    return arr




first_pos=int(input("number1:"))
second_pos=int(input("number2:"))
arr=[1,2,3,4,5]

arr=interchange(arr,first_pos,second_pos)
print(arr)

