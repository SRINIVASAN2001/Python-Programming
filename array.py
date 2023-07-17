import array as arr

number=arr.array('i',[1,2,3,4,5])
number.insert(5,8)
print(number)

del number[1]
print(number)

print(len(number))

print(number.buffer_info())

val=arr.array('i',[1,2,3,4,5])

newArr=arr.array(val.typecode, (a for a in val))
for x in newArr:
    print(newArr.index(x),"-->",x)

val.append(45)
val.insert(0,100)
print(val)
