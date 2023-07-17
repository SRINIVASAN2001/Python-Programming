arr=[3,7,1,4,5]

for i in range(len(arr)-1):
    for j in range(i+1):
        if arr[j]>arr[j+1]:

            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
